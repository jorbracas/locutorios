#!/usr/bin/env python3
"""
Corrige localidades mal asignadas y audita el resto por coordenadas.

POR QUE HACE FALTA OTRA COMPROBACION
------------------------------------
`sanear_geografia.py` valida la provincia con los dos primeros digitos del
codigo postal, que en Espana la determinan sin ambiguedad. Funciona bien, pero
tiene un punto ciego: da por bueno el propio codigo postal.

El caso que lo destapo fue India Post. Figuraba en La Adrada con CP 05430, y
ese CP es efectivamente de La Adrada, asi que la validacion no protesto. Pero
sus coordenadas caen a 500 m del casco de Sotillo de la Adrada y a 3,6 km del
de La Adrada, y la calle Carmen Rodriguez aparece en el callejero de Sotillo,
cuyo CP es 05420. El erroneo era el codigo postal.

La leccion: cuando el CP y las coordenadas discrepan, mandan las coordenadas.
Un CP se teclea mal; una latitud y una longitud vienen del propio mapa.

QUE HACE
--------
  1. Aplica las correcciones verificadas una a una (tabla CORRECCIONES).
  2. Audita todas las fichas comparando su posicion con el centroide de su
     localidad, y saca un listado de discrepancias para revision manual.
  3. Reconstruye geo.json, porque una localidad puede quedarse vacia.

Uso:  python3 corregir_localidades.py ./data [--simular]
"""

import json
import re
import sys
from collections import defaultdict
from math import asin, cos, radians, sin, sqrt
from pathlib import Path

# --------------------------------------------------------------------------
# Correcciones verificadas
#
# Cada entrada se ha comprobado a mano contra callejero y coordenadas. No se
# generan automaticamente: mover una ficha de municipio cambia su URL, y
# equivocarse crea una pagina fantasma.
# --------------------------------------------------------------------------

CORRECCIONES = [
    {
        "coincide": {"nombre": "India Post", "codigoPostal": "05430"},
        "motivo": "La calle Carmen Rodríguez pertenece al callejero de Sotillo "
                  "de la Adrada (CP 05420). Las coordenadas están a 0,5 km de "
                  "Sotillo y a 3,6 km de La Adrada. El CP de origen era erróneo.",
        "aplicar": {
            "slugProvincia": "avila",
            "slugCiudad": "sotillo-de-la-adrada",
            "ciudad": "Sotillo de la Adrada",
            "provincia": "Ávila",
            "codigoPostal": "05420",
        },
    },
    {
        "coincide": {"nombre": "Money Exchange Agente", "codigoPostal": "01400"},
        "motivo": "El CP 01400 corresponde a Laudio/Llodio. Estaba asignado a "
                  "Vitoria-Gasteiz, a 39 km de sus propias coordenadas.",
        "aplicar": {
            "slugProvincia": "araba-alava",
            "slugCiudad": "laudio-llodio",
            "ciudad": "Laudio / Llodio",
            "provincia": "Araba/Álava",
        },
    },
    {
        "coincide": {"nombre": "Locutorio", "codigoPostal": "08170"},
        "motivo": "El CP 08170 es de Montornès del Vallès, no de Barcelona "
                  "ciudad, de cuyo centro dista 17,6 km.",
        "aplicar": {
            "slugProvincia": "barcelona",
            "slugCiudad": "montornes-del-valles",
            "ciudad": "Montornès del Vallès",
            "provincia": "Barcelona",
        },
    },
    {
        "coincide": {"nombre": "LOCUTORIO REINA DEL CISNE", "codigoPostal": "46139"},
        "motivo": "El CP 46139 corresponde a La Pobla de Farnals. Las "
                  "coordenadas coinciden con esa localidad, a 12,5 km de "
                  "València capital.",
        "aplicar": {
            "slugProvincia": "valencia",
            "slugCiudad": "la-pobla-de-farnals",
            "ciudad": "La Pobla de Farnals",
            "provincia": "Valencia",
        },
    },
]

# Distancia a partir de la cual una ficha se considera descolocada.
UMBRAL_KM = 3.0


def distancia(a: tuple[float, float], b: tuple[float, float]) -> float:
    dlat = radians(b[0] - a[0])
    dlon = radians(b[1] - a[1])
    h = sin(dlat / 2) ** 2 + cos(radians(a[0])) * cos(radians(b[0])) * sin(dlon / 2) ** 2
    return 6371 * 2 * asin(sqrt(h))


def aplicar_correcciones(todas: list[dict], simular: bool) -> list[dict]:
    aplicadas = []
    for correccion in CORRECCIONES:
        criterio = correccion["coincide"]
        for ficha in todas:
            if not all(ficha.get(campo) == valor for campo, valor in criterio.items()):
                continue
            destino = correccion["aplicar"]
            if ficha["slugCiudad"] == destino["slugCiudad"]:
                continue

            antes = f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}"

            if not simular:
                for campo, valor in destino.items():
                    ficha[campo] = valor
                # La cadena de dirección arrastraba la localidad equivocada.
                if ficha.get("codigoPostal"):
                    ficha["direccion"] = re.sub(
                        r"\b\d{5}\s+[^,]+",
                        f"{ficha['codigoPostal']} {ficha['ciudad']}",
                        ficha["direccion"],
                        count=1,
                    )
                # Y los textos podían nombrarla.
                for campo in ("cuerpo", "resumen", "titulo", "metaTitulo", "metaDescripcion"):
                    if ficha.get(campo):
                        ficha[campo] = ficha[campo].replace("La Adrada", ficha["ciudad"]) \
                            if destino["slugCiudad"] == "sotillo-de-la-adrada" else ficha[campo]

            aplicadas.append({
                "nombre": ficha["nombre"],
                "de": antes,
                "a": f"/{destino['slugProvincia']}/{destino['slugCiudad']}/{ficha['slug']}",
                "motivo": correccion["motivo"],
            })
            break
    return aplicadas


def auditar(todas: list[dict]) -> list[dict]:
    """Compara cada ficha con el centroide de su localidad y de las vecinas."""
    centroides: dict[tuple[str, str], list] = defaultdict(lambda: [0.0, 0.0, 0, ""])
    for ficha in todas:
        clave = (ficha["slugProvincia"], ficha["slugCiudad"])
        entrada = centroides[clave]
        entrada[0] += ficha["lat"]
        entrada[1] += ficha["lng"]
        entrada[2] += 1
        entrada[3] = ficha["ciudad"]

    for entrada in centroides.values():
        entrada[0] /= entrada[2]
        entrada[1] /= entrada[2]

    sospechosas = []
    for ficha in todas:
        clave = (ficha["slugProvincia"], ficha["slugCiudad"])
        mio = centroides[clave]
        # Una localidad con una sola ficha es su propio centroide: no informa.
        if mio[2] < 2:
            continue
        d_propia = distancia((ficha["lat"], ficha["lng"]), (mio[0], mio[1]))
        if d_propia < UMBRAL_KM:
            continue

        mejor = None
        for (provincia, ciudad), datos in centroides.items():
            if provincia != ficha["slugProvincia"] or ciudad == ficha["slugCiudad"]:
                continue
            d = distancia((ficha["lat"], ficha["lng"]), (datos[0], datos[1]))
            if mejor is None or d < mejor[0]:
                mejor = (d, ciudad, datos[3])

        if mejor and mejor[0] < d_propia / 2:
            sospechosas.append({
                "nombre": ficha["nombre"],
                "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                "codigoPostal": ficha["codigoPostal"],
                "distanciaASuCiudadKm": round(d_propia, 1),
                "candidata": mejor[2],
                "distanciaACandidataKm": round(mejor[0], 1),
                "direccion": ficha["direccion"][:90],
            })

    sospechosas.sort(key=lambda s: -(s["distanciaASuCiudadKm"] - s["distanciaACandidataKm"]))
    return sospechosas


def reconstruir_geo(directorio: Path, todas: list[dict]) -> None:
    provincias: dict[str, dict] = {}
    for ficha in todas:
        provincia = provincias.setdefault(ficha["slugProvincia"], {
            "slug": ficha["slugProvincia"], "nombre": ficha["provincia"],
            "total": 0, "ciudades": {},
        })
        provincia["total"] += 1
        ciudad = provincia["ciudades"].setdefault(ficha["slugCiudad"], {
            "slug": ficha["slugCiudad"], "nombre": ficha["ciudad"],
            "total": 0, "lat": 0.0, "lng": 0.0,
        })
        ciudad["total"] += 1
        ciudad["lat"] += ficha["lat"]
        ciudad["lng"] += ficha["lng"]

    for provincia in provincias.values():
        lista = []
        for ciudad in provincia["ciudades"].values():
            ciudad["lat"] = round(ciudad["lat"] / ciudad["total"], 6)
            ciudad["lng"] = round(ciudad["lng"] / ciudad["total"], 6)
            lista.append(ciudad)
        lista.sort(key=lambda c: (-c["total"], c["nombre"]))
        provincia["ciudades"] = lista
        provincia["lat"] = round(sum(c["lat"] for c in lista) / len(lista), 6)
        provincia["lng"] = round(sum(c["lng"] for c in lista) / len(lista), 6)

    (directorio / "geo.json").write_text(json.dumps({
        "totalFichas": len(todas),
        "totalProvincias": len(provincias),
        "totalCiudades": sum(len(p["ciudades"]) for p in provincias.values()),
        "provincias": sorted(provincias.values(), key=lambda p: p["nombre"]),
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def procesar(directorio: Path, simular: bool) -> None:
    datos = {
        archivo.stem: json.loads(archivo.read_text(encoding="utf-8"))
        for archivo in sorted((directorio / "listings").glob("*.json"))
    }
    todas = [f for fichas in datos.values() for f in fichas]

    aplicadas = aplicar_correcciones(todas, simular)
    sospechosas = auditar(todas)

    if not simular:
        reagrupadas: dict[str, list[dict]] = defaultdict(list)
        for ficha in todas:
            reagrupadas[ficha["slugProvincia"]].append(ficha)
        for archivo in (directorio / "listings").glob("*.json"):
            archivo.unlink()
        for slug, fichas in reagrupadas.items():
            fichas.sort(key=lambda f: (f["slugCiudad"], -f.get("_rating", 0),
                                       -f.get("_reviews", 0), f["nombre"]))
            (directorio / "listings" / f"{slug}.json").write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")
        reconstruir_geo(directorio, todas)

    (directorio / "informe-localidades.json").write_text(json.dumps({
        "correccionesAplicadas": aplicadas,
        "revisionManual": sospechosas,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print("SIMULACIÓN — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Correcciones aplicadas: {len(aplicadas)}")
    for entrada in aplicadas:
        print(f"  {entrada['nombre'][:30]:30} {entrada['de']} -> {entrada['a']}")
    print(f"\nPara revisión manual: {len(sospechosas)}")
    for entrada in sospechosas[:10]:
        print(f"  {entrada['nombre'][:28]:28} CP{entrada['codigoPostal']:6} "
              f"{entrada['distanciaASuCiudadKm']:5.1f} km -> "
              f"{entrada['candidata'][:22]:22} {entrada['distanciaACandidataKm']:.1f} km")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
