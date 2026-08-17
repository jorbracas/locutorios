#!/usr/bin/env python3
"""
Normaliza el CSV maestro de locutorios a JSON listo para consumir por Next.js.

Entrada:  CSV exportado del pipeline de scraping + redaccion.
Salida:   data/geo.json                  indice de provincias y ciudades
          data/listings/<provincia>.json fichas completas por provincia

El CSV original pesa ~170 MB y NO debe subirse al repositorio
(GitHub rechaza ficheros de mas de 100 MB). Este script se ejecuta en local
y solo se versiona su salida.

Uso:  python3 build_data.py <ruta_csv> <directorio_salida>
"""

import json
import re
import sys
import unicodedata
import collections
from collections import defaultdict
from pathlib import Path

import pandas as pd

# --------------------------------------------------------------------------
# Configuracion
# --------------------------------------------------------------------------

COLUMNAS = [
    "tipo", "revisar", "cierre_temporal", "name", "calle", "ciudad",
    "codigo_postal", "provincia", "latitud", "longitud", "phone", "website",
    "rating", "reviews", "main_category", "categorias", "atributos", "about",
    "slug_provincia", "slug_ciudad", "slug_negocio", "place_id", "link",
    "plus_code", "address", "tier", "titulo_editorial", "meta_title",
    "meta_description", "resumen_corto", "texto_editorial", "popular_times",
]

# Ceuta y Melilla son ciudades autonomas: en el CSV llegan sin provincia.
CIUDADES_AUTONOMAS = {"ceuta": "Ceuta", "melilla": "Melilla"}

# Nombres de provincia con la forma oficial, para titulos y breadcrumbs.
NOMBRES_PROVINCIA = {
    "a-coruna": "A Coruña", "araba-alava": "Araba/Álava",
    "illes-balears": "Illes Balears", "las-palmas": "Las Palmas",
    "santa-cruz-de-tenerife": "Santa Cruz de Tenerife",
    "ciudad-real": "Ciudad Real", "la-rioja": "La Rioja",
    "bizkaia": "Bizkaia", "gipuzkoa": "Gipuzkoa", "navarra": "Navarra",
    "asturias": "Asturias", "cantabria": "Cantabria",
}

# Provincias que en lenguaje natural piden articulo ("en A Coruña" vs "en el Bierzo").
TIPO_ETIQUETA = {
    "Locutorio": "locutorio",
    "Envío de dinero": "envio",
    "Por verificar": "otros",
}


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def slugify(valor: str) -> str:
    """Convierte texto a slug ASCII apto para URL."""
    if not valor:
        return ""
    texto = unicodedata.normalize("NFKD", str(valor))
    texto = texto.encode("ascii", "ignore").decode("ascii").lower()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-")


def titulizar(slug: str) -> str:
    """Reconstruye un nombre legible desde un slug, respetando minusculas de enlace."""
    if slug in NOMBRES_PROVINCIA:
        return NOMBRES_PROVINCIA[slug]
    minusculas = {"de", "del", "la", "las", "el", "los", "y", "i", "a", "d"}
    partes = slug.split("-")
    salida = []
    for indice, parte in enumerate(partes):
        if indice > 0 and parte in minusculas:
            salida.append(parte)
        else:
            salida.append(parte.capitalize())
    return " ".join(salida)


def texto(valor) -> str:
    """Normaliza un valor de pandas a cadena limpia."""
    if valor is None or (isinstance(valor, float) and pd.isna(valor)):
        return ""
    cadena = str(valor).strip()
    return "" if cadena.lower() in ("nan", "none", "not present", "[]", "{}") else cadena


def numero(valor):
    try:
        resultado = float(valor)
        return None if pd.isna(resultado) else resultado
    except (TypeError, ValueError):
        return None


def booleano(valor) -> bool:
    return texto(valor).lower() == "true"


def parsear_json(valor):
    crudo = texto(valor)
    if not crudo:
        return None
    try:
        return json.loads(crudo)
    except (json.JSONDecodeError, TypeError):
        return None


def formatear_telefono(crudo: str) -> dict | None:
    """Devuelve el telefono en formato legible y en formato tel: para el enlace."""
    limpio = texto(crudo)
    if not limpio:
        return None
    digitos = re.sub(r"[^\d+]", "", limpio)
    if not digitos:
        return None
    return {"visible": limpio, "enlace": digitos}


def normalizar_web(crudo: str) -> str:
    """Descarta webs que apunten a Google o a redes, no aportan al usuario."""
    url = texto(crudo)
    if not url:
        return ""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    dominios_excluidos = ("google.com", "google.es", "goo.gl", "business.site")
    if any(dominio in url.lower() for dominio in dominios_excluidos):
        return ""
    return url


def extraer_atributos(campo_about) -> list[dict]:
    """Convierte el JSON `about` de Google en grupos de atributos activos."""
    datos = parsear_json(campo_about)
    if not isinstance(datos, list):
        return []
    grupos = []
    for grupo in datos:
        if not isinstance(grupo, dict):
            continue
        opciones = [
            texto(opcion.get("name"))
            for opcion in grupo.get("options", []) or []
            if isinstance(opcion, dict) and opcion.get("enabled")
        ]
        opciones = [opcion for opcion in opciones if opcion]
        if opciones:
            grupos.append({"grupo": texto(grupo.get("name")), "valores": opciones})
    return grupos


def trocear_categorias(crudo: str) -> list[str]:
    limpio = texto(crudo)
    if not limpio:
        return []
    vistas, salida = set(), []
    for parte in re.split(r"\s*[|,]\s*", limpio):
        parte = parte.strip()
        if parte and parte.lower() not in vistas:
            vistas.add(parte.lower())
            salida.append(parte)
    return salida


# --------------------------------------------------------------------------
# Actividad observada
#
# El CSV no trae horarios: la columna `hours` viene vacia en las 3.050 fichas.
# Pero 1.238 si traen `popular_times`, la afluencia por hora que Google calcula
# a partir de senales de ubicacion. No es el horario de apertura, aunque se le
# parece mucho: un local con afluencia de 10 a 14 y de 17 a 21 esta describiendo
# su jornada partida, y uno con el domingo a cero esta describiendo su descanso.
#
# Se publica como "actividad observada", nunca como horario. La distincion
# importa: una afluencia de cero puede significar tanto que el local esta
# cerrado como que simplemente no habia nadie dentro.
# --------------------------------------------------------------------------

DIAS_SEMANA = [
    ("Monday", "lunes"),
    ("Tuesday", "martes"),
    ("Wednesday", "miércoles"),
    ("Thursday", "jueves"),
    ("Friday", "viernes"),
    ("Saturday", "sábado"),
    ("Sunday", "domingo"),
]


def agrupar_tramos(horas: list[int]) -> list[list[int]]:
    """Agrupa horas sueltas en tramos contiguos [inicio, fin_exclusivo]."""
    if not horas:
        return []
    ordenadas = sorted(set(horas))
    tramos = []
    inicio = anterior = ordenadas[0]
    for hora in ordenadas[1:]:
        if hora == anterior + 1:
            anterior = hora
        else:
            tramos.append([inicio, anterior + 1])
            inicio = anterior = hora
    tramos.append([inicio, anterior + 1])
    return tramos


def extraer_actividad(campo_popular) -> dict | None:
    datos = parsear_json(campo_popular)
    if not isinstance(datos, dict):
        return None

    dias = []
    hay_algo = False
    for clave_en, nombre_es in DIAS_SEMANA:
        bloques = datos.get(clave_en) or []
        if not isinstance(bloques, list):
            bloques = []

        # Curva de 24 valores para el grafico, y horas activas para los tramos.
        curva = [0] * 24
        activas = []
        for bloque in bloques:
            if not isinstance(bloque, dict):
                continue
            hora = bloque.get("hour_of_day")
            porcentaje = bloque.get("popularity_percentage") or 0
            if isinstance(hora, int) and 0 <= hora < 24:
                curva[hora] = int(porcentaje)
                if porcentaje > 0:
                    activas.append(hora)

        tramos = agrupar_tramos(activas)
        if tramos:
            hay_algo = True
        dias.append({"dia": nombre_es, "tramos": tramos, "curva": curva})

    if not hay_algo:
        return None

    # Hora punta global, util como dato de una linea.
    mejor_hora, mejor_valor = None, 0
    for dia in dias:
        for hora, valor in enumerate(dia["curva"]):
            if valor > mejor_valor:
                mejor_hora, mejor_valor = hora, valor

    return {"dias": dias, "horaPunta": mejor_hora}


def recortar(cadena: str, maximo: int) -> str:
    """Recorta respetando palabras, para meta description."""
    cadena = " ".join(cadena.split())
    if len(cadena) <= maximo:
        return cadena
    corte = cadena[:maximo].rsplit(" ", 1)[0]
    return corte.rstrip(".,;:") + "…"


# Google corta el titulo alrededor de los 60 caracteres. Como el nombre del
# sitio NO se concatena en las fichas, todo el presupuesto es para el negocio.
LIMITE_TITULO = 60


def construir_titulo(meta_original: str, nombre: str, ciudad: str) -> str:
    """
    Elige el titulo mas informativo que quepa en el limite.

    Los titulos del CSV traen a menudo la calle detras de una barra vertical
    ("Locutorio X Teruel | Comercio en C. Comandante Fortea, 2"). Esa cola es
    la primera candidata a desaparecer: la direccion ya sale en el snippet y
    en la propia pagina, y ocupa la mitad del titulo.
    """
    candidatos = []
    if meta_original:
        candidatos.append(meta_original)
        if "|" in meta_original:
            candidatos.append(meta_original.split("|")[0].strip())
    if nombre and ciudad:
        candidatos.append(f"{nombre} en {ciudad}")
    candidatos.append(nombre)

    for candidato in candidatos:
        candidato = " ".join(candidato.split())
        if candidato and len(candidato) <= LIMITE_TITULO:
            return candidato

    # Ninguno cabe: se recorta el mas corto sin puntos suspensivos, que en un
    # titulo de resultado quedan peor que un corte limpio por palabra.
    mas_corto = min((c for c in candidatos if c), key=len)
    return " ".join(mas_corto.split())[:LIMITE_TITULO].rsplit(" ", 1)[0].rstrip(".,;:|-")


# --------------------------------------------------------------------------
# Proceso principal
# --------------------------------------------------------------------------

def construir(ruta_csv: Path, ruta_salida: Path) -> None:
    print(f"Leyendo {ruta_csv} …")
    df = pd.read_csv(ruta_csv, usecols=COLUMNAS, dtype=str, encoding="utf-8-sig")
    print(f"  {len(df)} filas en bruto")

    fichas: list[dict] = []
    descartadas = defaultdict(int)
    slugs_usados: set[tuple[str, str, str]] = set()

    for _, fila in df.iterrows():
        nombre = texto(fila["name"])
        if not nombre:
            descartadas["sin nombre"] += 1
            continue

        # --- provincia -----------------------------------------------------
        slug_provincia = texto(fila["slug_provincia"])
        slug_ciudad = texto(fila["slug_ciudad"])
        ciudad = texto(fila["ciudad"])

        if not slug_provincia:
            # Ceuta y Melilla llegan sin provincia: son ciudad y provincia a la vez.
            candidato = slugify(ciudad)
            if candidato in CIUDADES_AUTONOMAS:
                slug_provincia = candidato
                slug_ciudad = candidato
            else:
                descartadas["sin provincia"] += 1
                continue

        if not slug_ciudad:
            descartadas["sin ciudad"] += 1
            continue

        # --- slug de negocio unico dentro de la ciudad ----------------------
        slug_negocio = texto(fila["slug_negocio"]) or slugify(nombre)
        if not slug_negocio:
            descartadas["sin slug"] += 1
            continue

        clave = (slug_provincia, slug_ciudad, slug_negocio)
        if clave in slugs_usados:
            sufijo = 2
            while (slug_provincia, slug_ciudad, f"{slug_negocio}-{sufijo}") in slugs_usados:
                sufijo += 1
            slug_negocio = f"{slug_negocio}-{sufijo}"
            clave = (slug_provincia, slug_ciudad, slug_negocio)
        slugs_usados.add(clave)

        # --- geo ------------------------------------------------------------
        latitud, longitud = numero(fila["latitud"]), numero(fila["longitud"])
        if latitud is None or longitud is None:
            descartadas["sin coordenadas"] += 1
            continue

        # --- editorial -------------------------------------------------------
        cuerpo = texto(fila["texto_editorial"])
        resumen = texto(fila["resumen_corto"])
        nombre_ciudad = titulizar(slug_ciudad) if not ciudad else ciudad
        nombre_provincia = titulizar(slug_provincia)

        meta_titulo = construir_titulo(
            texto(fila["meta_title"]), nombre, nombre_ciudad
        )
        meta_descripcion = texto(fila["meta_description"]) or resumen
        # Google trunca alrededor de 160 caracteres.
        meta_descripcion = recortar(meta_descripcion, 158)

        fichas.append({
            "id": texto(fila["place_id"]),
            "nombre": nombre,
            "slug": slug_negocio,
            "slugCiudad": slug_ciudad,
            "slugProvincia": slug_provincia,
            "ciudad": nombre_ciudad,
            "provincia": nombre_provincia,
            "tipo": TIPO_ETIQUETA.get(texto(fila["tipo"]), "otros"),
            "calle": texto(fila["calle"]),
            "codigoPostal": texto(fila["codigo_postal"]),
            "direccion": texto(fila["address"]),
            "plusCode": texto(fila["plus_code"]),
            "lat": round(latitud, 7),
            "lng": round(longitud, 7),
            "telefono": formatear_telefono(fila["phone"]),
            "web": normalizar_web(fila["website"]),
            "categoria": texto(fila["main_category"]),
            "categorias": trocear_categorias(fila["categorias"]),
            "atributos": extraer_atributos(fila["about"]),
            "actividad": extraer_actividad(fila["popular_times"]),
            "cerradoTemporalmente": booleano(fila["cierre_temporal"]),
            "sinVerificar": booleano(fila["revisar"]),
            "tier": texto(fila["tier"]),
            # `rating` y `reviews` se conservan solo para ordenar resultados.
            # No se muestran ni se marcan en Schema: son datos de Google.
            "_rating": numero(fila["rating"]) or 0,
            "_reviews": int(numero(fila["reviews"]) or 0),
            "enlaceMaps": texto(fila["link"]),
            "titulo": texto(fila["titulo_editorial"]) or f"{nombre} en {nombre_ciudad}",
            "metaTitulo": meta_titulo,
            "metaDescripcion": meta_descripcion,
            "resumen": resumen,
            "cuerpo": cuerpo,
        })

    print(f"  {len(fichas)} fichas validas")
    for motivo, cantidad in descartadas.items():
        print(f"  descartadas por {motivo}: {cantidad}")

    # ----------------------------------------------------------------------
    # Desambiguacion de titulos
    #
    # Las cadenas de remesas repiten nombre dentro de la misma ciudad
    # ("Ria Money Transfer Alcaniz" x2). Dos paginas con identico title
    # compiten entre si y Google acaba eligiendo una. Se les anade la calle,
    # que es lo que de verdad las distingue para quien busca.
    # ----------------------------------------------------------------------
    repetidos = collections.Counter(f["metaTitulo"] for f in fichas)
    ajustados = 0
    for ficha in fichas:
        if repetidos[ficha["metaTitulo"]] < 2:
            continue
        via = ficha["calle"].split(",")[0].strip()
        if not via:
            continue
        propuesta = f"{ficha['metaTitulo']} ({via})"
        if len(propuesta) <= LIMITE_TITULO + 12:
            ficha["metaTitulo"] = propuesta
            ajustados += 1
    print(f"  titulos desambiguados: {ajustados}")

    # ----------------------------------------------------------------------
    # Indice geografico
    # ----------------------------------------------------------------------
    provincias: dict[str, dict] = {}
    for ficha in fichas:
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
        lista_ciudades = []
        for ciudad in provincia["ciudades"].values():
            # Centroide de la ciudad, para centrar el mapa.
            ciudad["lat"] = round(ciudad["lat"] / ciudad["total"], 6)
            ciudad["lng"] = round(ciudad["lng"] / ciudad["total"], 6)
            lista_ciudades.append(ciudad)
        lista_ciudades.sort(key=lambda c: (-c["total"], c["nombre"]))
        provincia["ciudades"] = lista_ciudades
        provincia["lat"] = round(sum(c["lat"] for c in lista_ciudades) / len(lista_ciudades), 6)
        provincia["lng"] = round(sum(c["lng"] for c in lista_ciudades) / len(lista_ciudades), 6)

    geo = {
        "totalFichas": len(fichas),
        "totalProvincias": len(provincias),
        "totalCiudades": sum(len(p["ciudades"]) for p in provincias.values()),
        "provincias": sorted(provincias.values(), key=lambda p: p["nombre"]),
    }

    # ----------------------------------------------------------------------
    # Escritura
    # ----------------------------------------------------------------------
    directorio_listados = ruta_salida / "listings"
    directorio_listados.mkdir(parents=True, exist_ok=True)
    for antiguo in directorio_listados.glob("*.json"):
        antiguo.unlink()

    por_provincia: dict[str, list[dict]] = defaultdict(list)
    for ficha in fichas:
        por_provincia[ficha["slugProvincia"]].append(ficha)

    for slug, lista in por_provincia.items():
        # Mejor valoradas primero dentro de cada ciudad; el rating no se publica.
        lista.sort(key=lambda f: (f["slugCiudad"], -f["_rating"], -f["_reviews"], f["nombre"]))
        destino = directorio_listados / f"{slug}.json"
        destino.write_text(
            json.dumps(lista, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    (ruta_salida / "geo.json").write_text(
        json.dumps(geo, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    peso = sum(f.stat().st_size for f in ruta_salida.rglob("*.json")) / 1_048_576
    print(f"\nEscrito en {ruta_salida}")
    print(f"  {geo['totalProvincias']} provincias · {geo['totalCiudades']} ciudades "
          f"· {geo['totalFichas']} fichas")
    print(f"  {peso:.1f} MB de JSON")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    construir(Path(sys.argv[1]), Path(sys.argv[2]))
