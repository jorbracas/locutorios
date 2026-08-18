#!/usr/bin/env python3
"""
Corrige los errores de geografia del dataset.

EL PROBLEMA
-----------
El origen trae fichas mal ubicadas, y eso no es un fallo cosmetico: genera
paginas de localidad enteras en sitios equivocados. Dos ejemplos reales:

  - "Locutorio Miguel Hernandez", CP 28018, direccion en Puente de Vallecas,
    catalogado en la ciudad de Fuengirola. La direccion que trae Google ya viene
    corrupta ("28018 Fuengirola, Madrid"). Creaba una pagina /madrid/fuengirola
    fantasma, ademas de existir la Fuengirola real en Malaga.
  - Un "MoneyGram" de Vitoria-Gasteiz catalogado en Bizkaia, cuando Vitoria es
    Alava.

LA REFERENCIA
-------------
En Espana los dos primeros digitos del codigo postal determinan la provincia sin
ambiguedad. Eso da una verificacion objetiva para la provincia, y una heuristica
solida para la ciudad: si un CP concentra sus fichas en una localidad y aparece
una suelta en otra, la suelta casi siempre esta mal.

PRUDENCIA
---------
No todas las discrepancias son errores. "Lejona" y "Leioa" son la misma
localidad en castellano y euskera; Puente Tocinos es una pedania de Murcia;
Vecindario pertenece al municipio de Santa Lucia de Tirajana. Por eso la fusion
automatica solo se aplica cuando la localidad de origen es residual (2 fichas o
menos) y la de destino la triplica. El resto se anota en el informe para
revision manual, sin tocar.

Uso:  python3 sanear_geografia.py ./data [--simular]
"""

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# Los dos primeros digitos del CP fijan la provincia.
CP_PROVINCIA = {
    "01": "araba-alava", "02": "albacete", "03": "alicante", "04": "almeria",
    "05": "avila", "06": "badajoz", "07": "illes-balears", "08": "barcelona",
    "09": "burgos", "10": "caceres", "11": "cadiz", "12": "castellon",
    "13": "ciudad-real", "14": "cordoba", "15": "a-coruna", "16": "cuenca",
    "17": "girona", "18": "granada", "19": "guadalajara", "20": "gipuzkoa",
    "21": "huelva", "22": "huesca", "23": "jaen", "24": "leon", "25": "lleida",
    "26": "la-rioja", "27": "lugo", "28": "madrid", "29": "malaga",
    "30": "murcia", "31": "navarra", "32": "ourense", "33": "asturias",
    "34": "palencia", "35": "las-palmas", "36": "pontevedra", "37": "salamanca",
    "38": "santa-cruz-de-tenerife", "39": "cantabria", "40": "segovia",
    "41": "sevilla", "42": "soria", "43": "tarragona", "44": "teruel",
    "45": "toledo", "46": "valencia", "47": "valladolid", "48": "bizkaia",
    "49": "zamora", "50": "zaragoza", "51": "ceuta", "52": "melilla",
}

NOMBRE_PROVINCIA = {
    "a-coruna": "A Coruña", "araba-alava": "Araba/Álava", "avila": "Ávila",
    "caceres": "Cáceres", "cadiz": "Cádiz", "castellon": "Castellón",
    "ciudad-real": "Ciudad Real", "cordoba": "Córdoba", "illes-balears": "Illes Balears",
    "jaen": "Jaén", "la-rioja": "La Rioja", "las-palmas": "Las Palmas",
    "leon": "León", "malaga": "Málaga", "ourense": "Ourense",
    "santa-cruz-de-tenerife": "Santa Cruz de Tenerife",
}

# La localidad de origen debe ser residual y la de destino, claramente mayor.
MAX_FICHAS_ORIGEN = 2
FACTOR_DESTINO = 3


def titulizar(slug: str) -> str:
    if slug in NOMBRE_PROVINCIA:
        return NOMBRE_PROVINCIA[slug]
    minusculas = {"de", "del", "la", "las", "el", "los", "y", "i", "a", "d"}
    partes = slug.split("-")
    return " ".join(
        parte if indice > 0 and parte in minusculas else parte.capitalize()
        for indice, parte in enumerate(partes)
    )


def prefijo(codigo: str) -> str | None:
    limpio = re.sub(r"\D", "", codigo or "")
    if len(limpio) < 4:
        return None
    # Los CP de una sola cifra inicial llegan sin el cero.
    limpio = limpio.zfill(5)
    return limpio[:2] if limpio[:2] in CP_PROVINCIA else None


def cargar(directorio: Path) -> tuple[dict[str, list[dict]], list[dict]]:
    por_archivo = {}
    todas = []
    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        por_archivo[archivo.stem] = fichas
        todas.extend(fichas)
    return por_archivo, todas


def procesar(directorio: Path, simular: bool) -> None:
    por_archivo, todas = cargar(directorio)
    informe = {"provincia": [], "ciudad": [], "revisar": []}

    total_ciudad = Counter((f["slugProvincia"], f["slugCiudad"]) for f in todas)

    # ------------------------------------------------------------------
    # 0. Articulo pospuesto
    #
    # El origen escribe algunas localidades con el articulo al final, a la
    # manera de los indices oficiales: "Hospitalet de Llobregat, L'" acaba
    # como `hospitalet-de-llobregat-l`. Si en la misma provincia existe ya la
    # forma con el articulo delante, son la misma localidad y deben unirse:
    # de lo contrario se publican dos paginas competiendo entre si.
    # ------------------------------------------------------------------
    ARTICULOS = ("l", "el", "la", "los", "las", "els", "les", "a", "o")
    existentes = {clave for clave in total_ciudad}

    for ficha in todas:
        partes = ficha["slugCiudad"].rsplit("-", 1)
        if len(partes) != 2 or partes[1] not in ARTICULOS:
            continue
        candidato = f"{partes[1]}-{partes[0]}"
        destino = (ficha["slugProvincia"], candidato)
        if destino not in existentes:
            continue
        informe["ciudad"].append({
            "nombre": ficha["nombre"],
            "codigoPostal": ficha["codigoPostal"],
            "de": f"{ficha['slugProvincia']}/{ficha['slugCiudad']}",
            "a": f"{destino[0]}/{destino[1]}",
            "fichasOrigen": total_ciudad[(ficha["slugProvincia"], ficha["slugCiudad"])],
            "fichasDestino": total_ciudad[destino],
            "motivo": "artículo pospuesto",
            "direccion": ficha["direccion"][:90],
        })
        if not simular:
            ficha["slugCiudad"] = candidato
            ficha["ciudad"] = titulizar(candidato)

    total_ciudad = Counter((f["slugProvincia"], f["slugCiudad"]) for f in todas)

    # ------------------------------------------------------------------
    # 1. Provincia contra el codigo postal
    # ------------------------------------------------------------------
    for ficha in todas:
        pref = prefijo(ficha["codigoPostal"])
        if not pref:
            continue
        correcta = CP_PROVINCIA[pref]
        if correcta != ficha["slugProvincia"]:
            informe["provincia"].append({
                "nombre": ficha["nombre"],
                "ciudad": ficha["ciudad"],
                "codigoPostal": ficha["codigoPostal"],
                "de": ficha["slugProvincia"],
                "a": correcta,
            })
            if not simular:
                ficha["slugProvincia"] = correcta
                ficha["provincia"] = titulizar(correcta)

    # ------------------------------------------------------------------
    # 2. Ciudad contra la localidad dominante de su codigo postal
    # ------------------------------------------------------------------
    por_cp: dict[str, Counter] = defaultdict(Counter)
    for ficha in todas:
        if prefijo(ficha["codigoPostal"]):
            por_cp[ficha["codigoPostal"]][(ficha["slugProvincia"], ficha["slugCiudad"])] += 1

    for ficha in todas:
        codigo = ficha["codigoPostal"]
        if codigo not in por_cp or len(por_cp[codigo]) < 2:
            continue

        actual = (ficha["slugProvincia"], ficha["slugCiudad"])
        destino, cuantas_destino = por_cp[codigo].most_common(1)[0]
        if destino == actual:
            continue

        origen_total = total_ciudad[actual]
        destino_total = total_ciudad[destino]

        entrada = {
            "nombre": ficha["nombre"],
            "codigoPostal": codigo,
            "de": f"{actual[0]}/{actual[1]}",
            "a": f"{destino[0]}/{destino[1]}",
            "fichasOrigen": origen_total,
            "fichasDestino": destino_total,
            "direccion": ficha["direccion"][:90],
        }

        # Solo se fusiona lo claramente residual. Lo demas puede ser una
        # pedania legitima o una variante de nombre que conviene mirar a mano.
        if origen_total <= MAX_FICHAS_ORIGEN and destino_total >= origen_total * FACTOR_DESTINO:
            informe["ciudad"].append(entrada)
            if not simular:
                ficha["slugProvincia"] = destino[0]
                ficha["slugCiudad"] = destino[1]
                ficha["provincia"] = titulizar(destino[0])
                ficha["ciudad"] = titulizar(destino[1])
        else:
            informe["revisar"].append(entrada)

    if simular:
        volcar_informe(directorio, informe, simular=True)
        return

    # ------------------------------------------------------------------
    # 3. Reescritura: las fichas cambian de provincia, luego de fichero
    # ------------------------------------------------------------------
    reagrupadas: dict[str, list[dict]] = defaultdict(list)
    for ficha in todas:
        reagrupadas[ficha["slugProvincia"]].append(ficha)

    for antiguo in (directorio / "listings").glob("*.json"):
        antiguo.unlink()

    for slug, fichas in reagrupadas.items():
        fichas.sort(key=lambda f: (f["slugCiudad"], -f["_rating"], -f["_reviews"], f["nombre"]))
        (directorio / "listings" / f"{slug}.json").write_text(
            json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    reconstruir_geo(directorio, todas)
    volcar_informe(directorio, informe, simular=False)


def reconstruir_geo(directorio: Path, todas: list[dict]) -> None:
    """Rehace el indice geografico: los recuentos han cambiado."""
    provincias: dict[str, dict] = {}
    for ficha in todas:
        provincia = provincias.setdefault(ficha["slugProvincia"], {
            "slug": ficha["slugProvincia"],
            "nombre": ficha["provincia"],
            "total": 0,
            "ciudades": {},
        })
        provincia["total"] += 1
        ciudad = provincia["ciudades"].setdefault(ficha["slugCiudad"], {
            "slug": ficha["slugCiudad"],
            "nombre": ficha["ciudad"],
            "total": 0,
            "lat": 0.0,
            "lng": 0.0,
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

    geo = {
        "totalFichas": len(todas),
        "totalProvincias": len(provincias),
        "totalCiudades": sum(len(p["ciudades"]) for p in provincias.values()),
        "provincias": sorted(provincias.values(), key=lambda p: p["nombre"]),
    }
    (directorio / "geo.json").write_text(
        json.dumps(geo, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def volcar_informe(directorio: Path, informe: dict, simular: bool) -> None:
    (directorio / "informe-geografia.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("SIMULACION — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Provincias corregidas: {len(informe['provincia'])}")
    for e in informe["provincia"]:
        print(f"  {e['nombre'][:34]:34} CP {e['codigoPostal']}  {e['de']} -> {e['a']}")
    print(f"\nLocalidades fusionadas: {len(informe['ciudad'])}")
    for e in informe["ciudad"]:
        print(f"  {e['nombre'][:30]:30} CP {e['codigoPostal']}  "
              f"{e['de']} ({e['fichasOrigen']}) -> {e['a']} ({e['fichasDestino']})")
    print(f"\nPara revisar a mano: {len(informe['revisar'])}")
    for e in informe["revisar"][:12]:
        print(f"  {e['nombre'][:30]:30} CP {e['codigoPostal']}  "
              f"{e['de']} ({e['fichasOrigen']}) vs {e['a']} ({e['fichasDestino']})")
    print(f"\nInforme en {directorio / 'informe-geografia.json'}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
