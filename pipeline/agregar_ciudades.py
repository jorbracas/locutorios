#!/usr/bin/env python3
"""
Calcula los datos agregados de cada localidad.

POR QUE ESTE FICHERO EXISTE
---------------------------
Las 803 paginas de localidad son el punto debil del directorio. Un parrafo de
plantilla con el nombre intercambiado ("En [ciudad] encontraras [N] locutorios
donde podras realizar envios...") es el patron que mejor detectan los sistemas
de contenido util de Google: misma estructura, mismo orden, solo cambia el
sustantivo. Y a diferencia de las fichas, aqui no hay resenas de las que sacar
variacion natural.

La salida no es redaccion, son hechos. Que en Getafe los 15 establecimientos
acepten tarjeta, que 7 abran domingo y que se repartan en 5 codigos postales
son datos que ninguna otra localidad reproduce igual. Eso diferencia la pagina
sin escribir una sola frase, y ademas responde al long-tail real por el que se
puede competir: "locutorio abierto domingo en X", "locutorio que acepte tarjeta
en X".

Uso:  python3 agregar_ciudades.py ./data
"""

import json
import sys
from collections import Counter, defaultdict
from math import cos, radians
from pathlib import Path

# Un atributo solo se publica si lo tiene al menos este porcentaje del total.
# Por debajo describe una excepcion, no la localidad.
UMBRAL_ATRIBUTO = 0.25

# Numero minimo de fichas con datos de actividad para que la media signifique
# algo. Con dos locales, "la hora punta" es ruido.
MINIMO_ACTIVIDAD = 3

DIAS_ORDEN = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def franja_legible(hora_inicio: int, hora_fin: int) -> str:
    return f"{hora_inicio}:00 a {hora_fin}:00"


def agregar_actividad(fichas: list[dict]) -> dict | None:
    """Combina las curvas de afluencia de la localidad en una sola lectura."""
    con_datos = [f for f in fichas if f.get("actividad")]
    if len(con_datos) < MINIMO_ACTIVIDAD:
        return None

    # Suma de afluencia por hora, sobre todos los locales y todos los dias.
    horas = [0] * 24
    abren_domingo = 0
    con_cierre_mediodia = 0

    for ficha in con_datos:
        domingo_activo = False
        partido = False
        for dia in ficha["actividad"]["dias"]:
            if dia["dia"] == "domingo" and dia["tramos"]:
                domingo_activo = True
            if len(dia["tramos"]) > 1:
                partido = True
            for hora, valor in enumerate(dia["curva"]):
                horas[hora] += valor
        if domingo_activo:
            abren_domingo += 1
        if partido:
            con_cierre_mediodia += 1

    if not any(horas):
        return None

    # Franja punta: las tres horas consecutivas con mayor afluencia acumulada.
    mejor_inicio, mejor_suma = 0, -1
    for inicio in range(0, 22):
        suma = sum(horas[inicio:inicio + 3])
        if suma > mejor_suma:
            mejor_inicio, mejor_suma = inicio, suma

    # Franja tranquila: la de menor afluencia dentro del horario comercial.
    peor_inicio, peor_suma = 9, None
    for inicio in range(9, 19):
        suma = sum(horas[inicio:inicio + 2])
        if peor_suma is None or suma < peor_suma:
            peor_inicio, peor_suma = inicio, suma

    return {
        "muestra": len(con_datos),
        "franjaPunta": franja_legible(mejor_inicio, mejor_inicio + 3),
        "franjaTranquila": franja_legible(peor_inicio, peor_inicio + 2),
        "abrenDomingo": abren_domingo,
        "cierreMediodia": con_cierre_mediodia,
    }


def agregar_atributos(fichas: list[dict]) -> list[dict]:
    """Atributos presentes en una proporcion significativa de la localidad."""
    conteo: Counter = Counter()
    for ficha in fichas:
        vistos = set()
        for grupo in ficha["atributos"]:
            for valor in grupo["valores"]:
                clave = (grupo["grupo"], valor)
                if clave not in vistos:
                    vistos.add(clave)
                    conteo[clave] += 1

    total = len(fichas)
    salida = []
    for (grupo, valor), cantidad in conteo.most_common():
        if cantidad / total < UMBRAL_ATRIBUTO:
            continue
        salida.append({
            "grupo": grupo,
            "valor": valor,
            "cantidad": cantidad,
            "total": total,
            "todos": cantidad == total,
        })
    return salida[:8]


def distancia_km(a: dict, b: dict) -> float:
    """Aproximacion plana, suficiente a escala provincial."""
    dlat = (a["lat"] - b["lat"]) * 111.0
    dlng = (a["lng"] - b["lng"]) * 111.0 * cos(radians(a["lat"]))
    return (dlat ** 2 + dlng ** 2) ** 0.5


def construir(directorio: Path) -> None:
    geo = json.loads((directorio / "geo.json").read_text(encoding="utf-8"))

    # Indice de todas las localidades con coordenadas, para calcular vecinas.
    todas = []
    for provincia in geo["provincias"]:
        for ciudad in provincia["ciudades"]:
            todas.append({
                "slugProvincia": provincia["slug"],
                "provincia": provincia["nombre"],
                "slug": ciudad["slug"],
                "nombre": ciudad["nombre"],
                "total": ciudad["total"],
                "lat": ciudad["lat"],
                "lng": ciudad["lng"],
            })

    agregados: dict[str, dict] = {}

    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas_provincia = json.loads(archivo.read_text(encoding="utf-8"))
        por_ciudad: dict[str, list[dict]] = defaultdict(list)
        for ficha in fichas_provincia:
            por_ciudad[ficha["slugCiudad"]].append(ficha)

        slug_provincia = archivo.stem

        for slug_ciudad, fichas in por_ciudad.items():
            total = len(fichas)
            tipos = Counter(f["tipo"] for f in fichas)

            codigos = sorted({f["codigoPostal"] for f in fichas if f["codigoPostal"]})
            con_telefono = sum(1 for f in fichas if f["telefono"])
            cerrados = sum(1 for f in fichas if f["cerradoTemporalmente"])

            # Localidad vecina con mas oferta, util sobre todo cuando esta
            # solo tiene uno o dos establecimientos.
            actual = next(
                (c for c in todas
                 if c["slug"] == slug_ciudad and c["slugProvincia"] == slug_provincia),
                None,
            )
            vecinas = []
            if actual:
                candidatas = [
                    {**c, "distancia": round(distancia_km(actual, c), 1)}
                    for c in todas
                    if not (c["slug"] == actual["slug"]
                            and c["slugProvincia"] == actual["slugProvincia"])
                ]
                candidatas = [c for c in candidatas if c["distancia"] <= 35]
                candidatas.sort(key=lambda c: (-c["total"], c["distancia"]))
                vecinas = [
                    {
                        "nombre": c["nombre"],
                        "slug": c["slug"],
                        "slugProvincia": c["slugProvincia"],
                        "total": c["total"],
                        "distancia": c["distancia"],
                    }
                    for c in candidatas[:4]
                ]

            agregados[f"{slug_provincia}/{slug_ciudad}"] = {
                "total": total,
                "tipos": {
                    "locutorio": tipos.get("locutorio", 0),
                    "envio": tipos.get("envio", 0),
                    "otros": tipos.get("otros", 0),
                },
                "conTelefono": con_telefono,
                "cerradosTemporalmente": cerrados,
                "codigosPostales": codigos,
                "atributos": agregar_atributos(fichas),
                "actividad": agregar_actividad(fichas),
                "vecinas": vecinas,
            }

    (directorio / "agregados-ciudad.json").write_text(
        json.dumps(agregados, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    con_actividad = sum(1 for a in agregados.values() if a["actividad"])
    con_atributos = sum(1 for a in agregados.values() if a["atributos"])
    print(f"Localidades agregadas: {len(agregados)}")
    print(f"  con lectura de actividad: {con_actividad}")
    print(f"  con atributos significativos: {con_atributos}")
    print(f"  con localidades vecinas: {sum(1 for a in agregados.values() if a['vecinas'])}")
    print(f"\nEscrito en {directorio / 'agregados-ciudad.json'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    construir(Path(sys.argv[1]))
