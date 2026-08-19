#!/usr/bin/env python3
"""
Correccion quirurgica de las fichas.

Este script NO reescribe fichas. Corrige defectos concretos y deja intacto
todo lo demas, siguiendo el principio de que una ficha correcta de 620
palabras no debe tocarse.

BLOQUES
-------
  1. Formato:      "## ##", encabezados vacios, dobles espacios.
  2. Gramatica:    "las informacion", "informacion mixtas", "la informacion son".
  3. Citas:        comillas simples que reproducen resenas.
  4. Personas:     nombres de empleados sacados de comentarios.
  5. Acusaciones:  imputaciones graves, siempre fuera.
  6. Anecdotas:    relatos individuales muy concretos.
  7. Geografia:    cadenas de direccion incoherentes con las coordenadas.
  8. Slugs:        colisiones de URL dentro de una misma ciudad.
  9. Metas:        titulo, resumen y metaDescripcion con marco de resenas.

LO QUE NO HACE
--------------
No elimina criticas operativas normales. "Algunos usuarios mencionan esperas
en horas punta" es informacion util para quien va a desplazarse, y borrarla
seria blanquear la ficha. Solo caen los relatos individuales, las acusaciones
y las citas.

Uso:  python3 corregir_fichas.py ./data [--simular]
"""

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# 5. Acusaciones graves — siempre fuera, diga lo que diga la coletilla
# --------------------------------------------------------------------------

ACUSACION = re.compile(
    r"\b(estafa\w*|estaf[oó]\b|fraude\w*|fraudulent\w+|timo\b|timad\w+|"
    r"rob[oa]s?\b|robad[oa]s?|roband\w+|hurto\w*|sustra[ií]d\w+|sustraer|"
    r"apropiaci[oó]n|se qued[oó] con (el|mi|su)|"
    r"acoso|acosad\w+|abus[oa]s?\b|pederast\w+|"
    r"racis\w+|racial\w*|xen[oó]fob\w+|homof[oó]b\w+|discriminaci[oó]n|"
    r"amenaz\w+|agresi[oó]n\w*|agredi\w+|violen\w+|"
    r"falsificaci[oó]n|falsificad\w+|billete falso|dinero B|"
    r"retenci[oó]n (intencionada|deliberada) de fondos|"
    r"denunci\w+|acusaci[oó]n\w*|acusad[oa]s?|acusan?\b|"
    r"delit\w+|ilegal\w*|chinches|[aá]caros|insalubr\w+|"
    r"no se les permiti[oó] el acceso|no permit\w+ (el|la) (acceso|entrada))\b",
    re.IGNORECASE,
)

# Lenguaje regulatorio y servicios administrativos: no son acusaciones.
CONTEXTO_NEUTRO = re.compile(
    r"\b(prevenir|prevenci[oó]n|evitar|antifraude|normativ\w+|cumplimiento|"
    r"verificaci[oó]n|blanqueo|regulaci\w+|contra el|contra la|frente al?|"
    r"protecci[oó]n|seguridad|identificaci[oó]n|obligatori\w+|requisit\w+|"
    r"cita[s]? (para|de|relacionad)|extranjer[ií]a|estafeta|"
    r"declaraci[oó]n de la renta|"
    # "espacio seguro", "libre de discriminacion" y "no discriminacion" son
    # atributos declarados del local, justo lo contrario de una acusacion.
    r"no discriminaci[oó]n|sin discriminaci[oó]n|libre de discriminaci[oó]n|"
    r"espacios? seguros?|amigable con|inclusi[vó]\w*|diversidad|"
    r"sin temor a|acceso para sillas)\b",
    re.IGNORECASE,
)

# --------------------------------------------------------------------------
# 6. Anecdota individual frente a tendencia generalizada
#
# La diferencia decisiva. "Algunos usuarios mencionan esperas" describe una
# tendencia y se queda; "una persona espero una llamada que nunca llego" es
# el relato de un caso y se va. El detector de origen marco 1.505 frases sin
# separar ambas cosas, asi que aqui se separan.
# --------------------------------------------------------------------------

# Marcas de caso individual.
CASO_INDIVIDUAL = re.compile(
    r"\b(en una ocasi[oó]n|en un caso|un caso (aislado|concreto|puntual)|"
    r"una experiencia (puntual|concreta|aislada)|la [uú]nica experiencia|"
    r"un cliente|una clienta|un usuario|una usuaria|una persona|un comprador|"
    r"alguien (que|acudi|lleg|cont)|otra persona|otro cliente|otra encontr\w+|"
    r"un par de ocasiones|una vez que|cierta ocasi[oó]n|"
    r"lleg[oó] a (afirmar|decir|denunciar)|relat[oó]|asegur[oó] que|afirm[oó] que|"
    r"(una|alguna) (queja|experiencia|incidencia|opini[oó]n) (aislada|puntual|concreta|negativa)|"
    r"un (comentario|testimonio) (aislado|puntual))\b",
    re.IGNORECASE,
)

# Verbo de suceso relatado. Sin el, una mencion individual suele ser un caso
# de uso ilustrativo ("para una persona recien llegada...") y no un incidente.
VERBO_DE_SUCESO = re.compile(
    r"\b(afirm[oó]|asegur[oó]|report[oó]|relat[oó]|denunci[oó]|cont[oó]|"
    r"mencion[oó]|se[ñn]al[oó]|se (ha )?(registrado|report[oó]|produjo)|"
    r"tuvo|sufri[oó]|encontr[oó]|esper[oó]|acudi[oó]|reclam[oó]|"
    r"perdi[oó]|le (cobraron|dijeron|negaron)|no (pudo|consigui[oó])|"
    r"hubo|se qued[oó]|quej[oó]|protest[oó])\b",
    re.IGNORECASE,
)

# Caso de uso hipotetico: describe para que sirve un servicio confirmado.
# Es contenido legitimo y no debe confundirse con el relato de un incidente.
CASO_HIPOTETICO = re.compile(
    r"(\bpor ejemplo\b|\bpara (una|un|alguien|quien|quienes)\b|"
    r"\bsi (trabajas|necesitas|realizas|eres|vives|prefieres)\b|"
    r"\bque (necesite|quiera|tenga|busque|desee|trabaje|viva|prefiera)\b|"
    r"\bpodr[ií]a (encontrar|resultar|servir|ser|aprovechar)\b|"
    r"\bpuede (necesitar|resultar|servir|ahorrar|marcar)\b|"
    r"\bcasos? de uso\b)",
    re.IGNORECASE,
)

# Detalles que solo delatan una anecdota si acompanan a un incidente:
# una hora exacta o una duracion. Los importes quedan fuera a proposito,
# porque suelen ser tarifas confirmadas del propio establecimiento.
DETALLE_CONCRETO = re.compile(
    r"(\b\d{1,2}[:.]\d{2}\b|"
    r"\bdurante (m[aá]s de )?(un|dos|tres|varios|varias)\s"
    r"(mes|meses|semana|semanas|d[ií]as?|horas?)\b|"
    r"\bm[aá]s de un mes\b)",
    re.IGNORECASE,
)

# Formulaciones ya generalizadas: se conservan.
GENERALIZADO = re.compile(
    r"\b(algunos|algunas|varios|varias|ciertos|ciertas|parte de los|"
    r"en (algunos|varios) casos|hay quien|no faltan quienes|"
    r"diversas experiencias|distintas experiencias|"
    r"experiencias variadas|opiniones variadas|de forma recurrente)\b",
    re.IGNORECASE,
)

# --------------------------------------------------------------------------
# 3 y 4. Citas y nombres de personas
# --------------------------------------------------------------------------

# La comilla simple de apertura no puede ir pegada a una letra por la
# izquierda: en catalan "Ctra. d'Europa" o "Carrer de l'Avet" llevan apostrofo
# de elision, que no es una cita y no debe tocarse.
CITA_SIMPLE = re.compile(
    r"(?<![\wÀ-ÿ])['‘]([^'‘’\n]{3,120})['’](?![\wÀ-ÿ])"
)
CITA_DOBLE = re.compile(r"[«\"\u201c]([^«\"»\u201c\u201d\n]{3,300})[»\"\u201d]")
LIMITE_CITA = 60

NOMBRE_PERSONA = re.compile(
    r"\b(emplead[oa]|trabajador[ae]?|dependient[ae]|chic[oa]|se[ñn]or[a]?|"
    r"encargad[oa]|camarer[oa]|compa[ñn]er[oa])\s+(?:llamad[oa]\s+)?"
    r"([A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,})\b"
)

# --------------------------------------------------------------------------
# 9. Marco de resenas en metadatos
# --------------------------------------------------------------------------

FRAMING_META = re.compile(
    r"\s*(y|e)?\s*(las\s+)?(experiencias?( de (los\s+)?(clientes|usuarios))?|"
    r"opiniones( de (los\s+)?(clientes|usuarios))?|valoraciones|rese[ñn]as|"
    r"puntos? fuertes?( y d[eé]biles)?|luces y sombras|"
    r"lo que (opinan|dicen) (los|sus) (clientes|usuarios))\b\.?",
    re.IGNORECASE,
)

FRAMING_TITULO = re.compile(
    r"\s*[:,–—-]\s*[^:,–—-]*\b(experiencias?|opiniones|valoraciones|rese[ñn]as|"
    r"cautela|matices|luces y sombras|polémic\w+|controvertid\w+|"
    r"puntos? fuertes?|lo que se (valora|critica)|variad\w+|divididas)\b[^:,–—-]*$",
    re.IGNORECASE,
)

SENSACIONALISTA = re.compile(
    r"\b(luces y sombras|experiencias pol[eé]micas|opiniones divididas|"
    r"atenci[oó]n controvertida|acusaciones|pol[eé]mica|posible estafa|"
    r"experiencias contrastadas|con la cautela de)\b",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------
# Clasificacion de frases del cuerpo
# --------------------------------------------------------------------------

# Acusacion atribuida a terceros. Tiene prioridad sobre el contexto neutro:
# "algunos lo han calificado de estafa, aunque no hay verificacion legal"
# contiene la palabra "verificacion", que de otro modo la habria salvado.
# La coletilla de cautela no atenua nada, solo publica la imputacion.
ACUSACION_ATRIBUIDA = re.compile(
    r"\b(califican?|han calificado|acusan?|han acusado|tachan?|"
    r"consideran?|denuncian?|hablan) (la pr[aá]ctica |el negocio |al? \w+ )?"
    r"(de|como|una|un)\s*"
    r"(estafa|fraude|robo|timo|delito|acoso|racismo|discriminaci[oó]n)\b"
    r"|\b(negativa a|negaron a|se neg[oó] a) falsificar\b"
    r"|\bfalsificar un documento\b",
    re.IGNORECASE,
)


def clasificar(frase: str) -> str:
    """'acusacion', 'anecdota', 'descomillar' o 'conservar'."""
    if ACUSACION_ATRIBUIDA.search(frase):
        return "acusacion"

    if not CONTEXTO_NEUTRO.search(frase) and ACUSACION.search(frase):
        return "acusacion"

    # Un relato individual solo se elimina si ademas narra un suceso. Asi se
    # distingue "una persona afirmo que le cobraron de mas" (anecdota) de
    # "para una persona recien llegada, este servicio puede ser util" (caso de
    # uso). Y si la frase ya esta generalizada, se conserva: es una tendencia.
    if not CASO_HIPOTETICO.search(frase) and not GENERALIZADO.search(frase):
        individual = CASO_INDIVIDUAL.search(frase) or DETALLE_CONCRETO.search(frase)
        if individual and VERBO_DE_SUCESO.search(frase):
            return "anecdota"

    citas = CITA_SIMPLE.findall(frase) + CITA_DOBLE.findall(frase)
    if citas:
        if any(len(c) > LIMITE_CITA for c in citas):
            return "anecdota"
        return "descomillar"

    return "conservar"


def descomillar(frase: str) -> str:
    frase = CITA_SIMPLE.sub(lambda m: m.group(1), frase)
    return CITA_DOBLE.sub(lambda m: m.group(1), frase)


def quitar_nombres(frase: str) -> tuple[str, int]:
    """Deja el rol y elimina el nombre propio."""
    nuevo, n = NOMBRE_PERSONA.subn(lambda m: m.group(1), frase)
    return nuevo, n


# --------------------------------------------------------------------------
# Limpieza de formato y gramatica
# --------------------------------------------------------------------------

ARREGLOS_GRAMATICA = [
    (r"\bl[aa]s informaci[oó]n\b", "la información"),
    (r"\bLas informaci[oó]n\b", "La información"),
    (r"\binformaci[oó]n mixtas\b", "información mixta"),
    (r"\bla informaci[oó]n son\b", "la información es"),
    (r"\bLa informaci[oó]n son\b", "La información es"),
    (r"\bdatos es\b", "datos son"),
    (r"\s+([,.;:])", r"\1"),
    (r"[ \t]{2,}", " "),
]


def limpiar_formato(texto: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()

    antes = texto
    # Encabezados vacios: "## ##", "##" suelto, "## " sin titulo.
    texto = re.sub(r"(?m)^##\s*##\s*$", "", texto)
    texto = re.sub(r"(?m)^##\s*$", "", texto)
    texto = re.sub(r"##\s*##", "", texto)
    if texto != antes:
        marcador["encabezados_vacios"] += 1

    for patron, reemplazo in ARREGLOS_GRAMATICA:
        texto, n = re.subn(patron, reemplazo, texto)
        if n:
            marcador["gramatica"] += n

    # Barrido final de comillas. Alguna cita corta sobrevive cuando la frase
    # que la contiene se conserva por otra via; aqui se le quitan las comillas
    # sin tocar el resto, que es lo que corresponde a una cita breve.
    antes_citas = texto
    texto = CITA_DOBLE.sub(lambda m: m.group(1) if len(m.group(1)) <= LIMITE_CITA else m.group(0), texto)
    texto = CITA_SIMPLE.sub(lambda m: m.group(1), texto)
    if texto != antes_citas:
        marcador["citas_integradas"] += 1

    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip(), marcador


# --------------------------------------------------------------------------
# Procesado del cuerpo
# --------------------------------------------------------------------------

def procesar_parrafo(parrafo: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()
    limpio = parrafo.strip()
    if not limpio:
        return "", marcador

    if limpio.startswith("##"):
        partes = limpio.split("\n", 1)
        if len(partes) == 2 and partes[1].strip():
            cuerpo, parcial = procesar_parrafo(partes[1].strip())
            marcador.update(parcial)
            return (f"{partes[0]}\n\n{cuerpo}" if cuerpo else ""), marcador
        return limpio, marcador

    conservadas = []
    for frase in re.split(r"(?<=[.!?])\s+", limpio):
        if not frase.strip():
            continue
        accion = clasificar(frase)

        if accion == "acusacion":
            marcador["acusaciones_eliminadas"] += 1
            continue
        if accion == "anecdota":
            marcador["anecdotas_eliminadas"] += 1
            continue
        if accion == "descomillar":
            frase = descomillar(frase)
            marcador["citas_integradas"] += 1

        frase, n = quitar_nombres(frase)
        if n:
            marcador["nombres_eliminados"] += n

        marcador["criticas_conservadas"] += 1 if _es_critica(frase) else 0
        conservadas.append(frase)

    texto = " ".join(conservadas).strip()
    if conservadas and len(texto.split()) < 10:
        marcador["parrafos_eliminados"] += 1
        return "", marcador
    return texto, marcador


CRITICA_NORMAL = re.compile(
    r"\b(espera\w*|cola[s]?|demora\w*|retraso\w*|incidencia\w*|queja\w*|"
    r"cr[ií]tica\w*|mejorable\w*|irregular\w*|inconsistent\w*|"
    r"menos favorable\w*|puntos? d[eé]bil\w*)\b",
    re.IGNORECASE,
)


def _es_critica(frase: str) -> bool:
    return bool(CRITICA_NORMAL.search(frase))


ENCABEZADO_SENSACIONAL = re.compile(
    r"^##\s.*\b(experiencias contrastadas|luces y sombras|lo que se critica|"
    r"opiniones divididas|pol[eé]mic\w+|controvertid\w+)\b",
    re.IGNORECASE,
)


def procesar_cuerpo(cuerpo: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()
    cuerpo, parcial = limpiar_formato(cuerpo)
    marcador.update(parcial)

    bloques = []
    for parrafo in cuerpo.split("\n\n"):
        if parrafo.strip().startswith("##") and ENCABEZADO_SENSACIONAL.match(parrafo.strip()):
            # Se neutraliza el titular, no la seccion: el contenido puede
            # seguir siendo util una vez depurado.
            parrafo = re.sub(r"^##\s.*", "## Lo que destacan los usuarios", parrafo.strip(), count=1)
            marcador["encabezados_neutralizados"] += 1
        nuevo, parcial = procesar_parrafo(parrafo)
        marcador.update(parcial)
        if nuevo.strip():
            bloques.append(nuevo)

    # Encabezados que se quedan sin parrafo debajo.
    limpio = []
    for indice, bloque in enumerate(bloques):
        if bloque.lstrip().startswith("##"):
            siguiente = bloques[indice + 1] if indice + 1 < len(bloques) else ""
            if not siguiente or siguiente.lstrip().startswith("##"):
                marcador["encabezados_huerfanos"] += 1
                continue
        limpio.append(bloque)

    return "\n\n".join(limpio), marcador


# --------------------------------------------------------------------------
# Metadatos
# --------------------------------------------------------------------------

def limpiar_meta(texto: str) -> tuple[str, int]:
    """Quita el marco de resenas dejando la parte descriptiva."""
    if not texto:
        return texto, 0
    original = texto

    # "Conoce sus servicios y experiencias." -> "Conoce sus servicios."
    #
    # CORREGIDO: la version original de esta regex no exigia limite de
    # palabra antes de (y|e), asi que "e" podia coincidir con la ultima letra
    # de CUALQUIER palabra que terminase en "e" (de, aunque, sobre...) seguida
    # de "experiencia". Eso convertia "20 anos de experiencia" en "20 anos d."
    # Detectado y reparado en pipeline/reparar_texto_mutilado.py sobre 56
    # fichas ya publicadas; \b aqui evita que vuelva a pasar.
    texto = re.sub(
        r"\s*\b(y|e)\b\s+(las\s+)?(experiencias?|opiniones|valoraciones|rese[ñn]as)"
        r"( de (los\s+)?(clientes|usuarios))?\s*\.?",
        ".", texto, flags=re.IGNORECASE)

    texto = re.sub(
        r"\s*Conoce sus puntos fuertes y las experiencias[^.]*\.?", "",
        texto, flags=re.IGNORECASE)

    # Frases completas de marco de resenas.
    texto = re.sub(
        r"(?:^|\s)[^.]*\b(experiencias? de (los\s+)?(clientes|usuarios)|"
        r"opiniones divididas|luces y sombras|puntos fuertes y d[eé]biles|"
        r"lo que (opinan|dicen) (los|sus) (clientes|usuarios))\b[^.]*\.",
        " ", texto, flags=re.IGNORECASE)

    texto = re.sub(r"\s{2,}", " ", texto).strip()
    texto = re.sub(r"\s+\.", ".", texto)
    texto = re.sub(r"\.{2,}", ".", texto)
    return texto, int(texto != original)


def limpiar_titulo(titulo: str) -> tuple[str, int]:
    if not titulo:
        return titulo, 0
    original = titulo
    titulo = FRAMING_TITULO.sub("", titulo).strip(" :,–—-")
    titulo = SENSACIONALISTA.sub("", titulo).strip(" :,–—-")
    titulo = re.sub(r"\s{2,}", " ", titulo)
    return titulo, int(titulo != original)


# --------------------------------------------------------------------------
# 7. Geografia: la cadena de direccion
#
# El saneamiento anterior corrigio `ciudad` y `slugCiudad`, pero dejo intacta
# la cadena `direccion`, que sigue arrastrando el error de origen. Una ficha
# de Puente de Vallecas no puede seguir diciendo "28018 Fuengirola, Madrid"
# aunque su ciudad estructurada ya sea Madrid.
# --------------------------------------------------------------------------

ARTEFACTOS_DIRECCION = {
    "bajo", "baji", "bajó", "el", "la", "los", "las", "posterior",
    "cochabamba", "taco", "fraile", "guaza",
}


def reparar_direccion(ficha: dict) -> tuple[str, bool]:
    """Sustituye la localidad incrustada por la correcta de la ficha."""
    direccion = ficha.get("direccion") or ""
    ciudad = ficha.get("ciudad") or ""
    if not direccion or not ciudad:
        return direccion, False

    original = direccion
    codigo = ficha.get("codigoPostal") or ""

    if codigo and codigo in direccion:
        # Todo lo que sigue al CP hasta la coma siguiente es la localidad.
        patron = re.compile(
            re.escape(codigo) + r"\s+([^,]+)"
        )
        coincidencia = patron.search(direccion)
        if coincidencia:
            escrita = coincidencia.group(1).strip()
            if _normalizar(escrita) != _normalizar(ciudad):
                direccion = patron.sub(f"{codigo} {ciudad}", direccion, count=1)

    # Artefactos de parseo sueltos entre comas.
    partes = [p.strip() for p in direccion.split(",")]
    partes = [
        p for p in partes
        if p and p.lower() not in ARTEFACTOS_DIRECCION
    ]
    direccion = ", ".join(partes)

    # Localidad duplicada consecutiva.
    direccion = re.sub(r"\b([\wÁÉÍÓÚÑáéíóúñ' -]+), \1\b", r"\1", direccion)
    direccion = re.sub(r"\s{2,}", " ", direccion).strip(" ,")

    return direccion, direccion != original


def _normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = texto.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "", texto)


# --------------------------------------------------------------------------
# 8. Colisiones de URL
# --------------------------------------------------------------------------

PALABRAS_VIA = re.compile(
    r"^(calle|c/|c\.|avenida|avda|av\.|paseo|plaza|pl\.|carrer|ronda|"
    r"camino|travesia|travesía|rambla|via|vía|gran)\b\.?\s*", re.IGNORECASE
)


def slug_desde_calle(calle: str) -> str:
    """Slug corto a partir del nombre de la via, sin el tipo ni el numero."""
    limpio = PALABRAS_VIA.sub("", (calle or "").strip())
    limpio = re.sub(r"\d+.*$", "", limpio)  # fuera numero y todo lo posterior
    limpio = _slug(limpio)
    return "-".join(limpio.split("-")[:3])


def _slug(valor: str) -> str:
    texto = unicodedata.normalize("NFKD", valor or "")
    texto = texto.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", texto).strip("-")


def resolver_colisiones(fichas: list[dict]) -> tuple[int, list[dict]]:
    """
    Da URL unica a cada establecimiento. No se elimina ninguna ficha: dos
    oficinas distintas de la misma cadena son dos negocios reales, y la calle
    es lo que de verdad las distingue para quien busca.
    """
    grupos: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for ficha in fichas:
        grupos[(ficha["slugProvincia"], ficha["slugCiudad"], ficha["slug"])].append(ficha)

    resueltas = 0
    detalle = []
    for (provincia, ciudad, slug), grupo in grupos.items():
        if len(grupo) < 2:
            continue
        usados = {slug}
        for ficha in grupo[1:]:
            sufijo = slug_desde_calle(ficha.get("calle", ""))
            candidato = f"{slug}-{sufijo}" if sufijo else slug
            contador = 2
            while candidato in usados or not sufijo:
                candidato = f"{slug}-{contador}"
                contador += 1
            usados.add(candidato)
            detalle.append({
                "nombre": ficha["nombre"],
                "ciudad": ficha["ciudad"],
                "de": f"/{provincia}/{ciudad}/{ficha['slug']}",
                "a": f"/{provincia}/{ciudad}/{candidato}",
            })
            ficha["slug"] = candidato
            resueltas += 1
    return resueltas, detalle


# --------------------------------------------------------------------------
# 11. Negocios sin nombre
# --------------------------------------------------------------------------

def nombre_invalido(nombre: str) -> bool:
    limpio = (nombre or "").strip().upper()
    return limpio in {"UNKNOWN", "N/A", "NA", "SIN NOMBRE", "-", ""}


# --------------------------------------------------------------------------
# Proceso
# --------------------------------------------------------------------------

def procesar(directorio: Path, simular: bool) -> None:
    total: Counter = Counter()
    modificadas = 0
    revision_manual: list[dict] = []
    sin_publicar: list[dict] = []

    archivos = sorted((directorio / "listings").glob("*.json"))
    datos = {a.stem: json.loads(a.read_text(encoding="utf-8")) for a in archivos}
    todas = [f for fichas in datos.values() for f in fichas]

    # --- 8. Colisiones de URL, antes de nada -----------------------------
    colisiones, detalle_colisiones = resolver_colisiones(todas)
    total["urls_desduplicadas"] = colisiones

    for ficha in todas:
        cambios: Counter = Counter()

        # --- 11. Nombre placeholder --------------------------------------
        if nombre_invalido(ficha["nombre"]):
            ficha["revisionManual"] = "nombre no identificable"
            ficha["noIndexar"] = True
            sin_publicar.append({
                "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                "ciudad": ficha["ciudad"],
                "direccion": ficha.get("direccion", "")[:80],
                "motivo": "nombre UNKNOWN; no se inventa un nombre comercial",
            })
            cambios["fichas_sin_nombre"] += 1

        # --- 1-6. Cuerpo --------------------------------------------------
        cuerpo, parcial = procesar_cuerpo(ficha["cuerpo"])
        cambios.update(parcial)

        # --- Resumen ------------------------------------------------------
        resumen, parcial_resumen = procesar_parrafo(ficha["resumen"])
        cambios.update(parcial_resumen)
        resumen, _ = limpiar_formato(resumen)
        resumen, n_meta = limpiar_meta(resumen)
        cambios["metas_limpiadas"] += n_meta

        if not resumen.strip() and cuerpo:
            resumen = re.split(r"(?<=[.!?])\s+", cuerpo.replace("##", "").strip())[0]

        # --- 9. Titulo y metaDescripcion ----------------------------------
        titulo, n_titulo = limpiar_titulo(ficha.get("titulo", ""))
        meta_titulo, n_mt = limpiar_titulo(ficha.get("metaTitulo", ""))
        meta_desc, n_md = limpiar_meta(ficha.get("metaDescripcion", ""))
        cambios["metas_limpiadas"] += n_titulo + n_mt + n_md

        # --- 7. Direccion --------------------------------------------------
        direccion, cambiada = reparar_direccion(ficha)
        if cambiada:
            cambios["direcciones_corregidas"] += 1

        if not cambios and not simular:
            continue

        if not simular:
            ficha["cuerpo"] = cuerpo
            ficha["resumen"] = resumen.strip()
            if titulo:
                ficha["titulo"] = titulo
            if meta_titulo:
                ficha["metaTitulo"] = meta_titulo
            if meta_desc:
                ficha["metaDescripcion"] = meta_desc
            ficha["direccion"] = direccion

        if cambios:
            modificadas += 1
            total.update(cambios)

    # --- Escritura --------------------------------------------------------
    if not simular:
        for slug, fichas in datos.items():
            (directorio / "listings" / f"{slug}.json").write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )

    # --- Informe ----------------------------------------------------------
    cortas = [
        {
            "url": f"/{f['slugProvincia']}/{f['slugCiudad']}/{f['slug']}",
            "nombre": f["nombre"],
            "palabras": len(f["cuerpo"].split()),
        }
        for f in todas if len(f["cuerpo"].split()) < 500
    ]
    cortas.sort(key=lambda x: x["palabras"])

    informe = {
        "fichasModificadas": modificadas,
        "recuentos": dict(total),
        "urlsDesduplicadas": detalle_colisiones,
        "sinPublicar": sin_publicar,
        "fichasBajo500": len(cortas),
        "revisionManual": revision_manual,
        "listaCortas": cortas[:40],
    }
    (directorio / "informe-correcciones.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("SIMULACIÓN — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fichas modificadas: {modificadas}")
    for clave, valor in total.most_common():
        if valor:
            print(f"  {clave}: {valor}")
    print(f"\nFichas por debajo de 500 palabras: {len(cortas)}")
    print(f"Informe en {directorio / 'informe-correcciones.json'}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
