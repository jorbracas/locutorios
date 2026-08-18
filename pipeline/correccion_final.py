#!/usr/bin/env python3
"""
Ultima pasada quirurgica. Diez correcciones puntuales, nada mas.

Cada bloque actua sobre un defecto concreto y deja intacto todo lo demas.
Ninguna ficha correcta se reescribe.

  1. Acusaciones restantes en dos fichas nombradas.
  2. Anecdotas individuales en tres fichas nombradas.
  3. "Retencion de paquetes" -> "demoras/incidencias" cuando es operativo.
  4. Errores gramaticales por mayuscula intrusa y concordancia.
  5. Nombres personales de comentarios (no los del rotulo comercial).
  6. Restaurar "Bajo", "Posterior", "Local" en las direcciones.
  7. MoneyGram de Federico Garcia Lorca -> Montornes del Valles.
  8. Deduplicar valores de atributos conservando el orden.
  9. Quitar la frase inventada y variar los bloques repetidos.
 10. No tocar nada mas.

Uso:  python3 correccion_final.py ./data [--simular]
"""

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

DIR_ANTERIOR = Path("/tmp/data_pre_correcciones")

# --------------------------------------------------------------------------
# 1 y 2. Fichas nombradas
# --------------------------------------------------------------------------

# Frases que deben desaparecer, identificadas por un fragmento literal.
# Se listan una a una a proposito: son casos revisados a mano, no un patron.
FRASES_FUERA = [
    # Acusaciones graves
    "acusó al establecimiento de quedarse con dos productos",
    "caso de retención de dinero en un envío sin solución aparente",
    "no siempre se pide el DNI al recoger paquetes",
    "el personal acusó a un cliente de estar loco",
    "acusó al cliente de desconfiar",
    # Anecdotas individuales
    "en un caso extremo, la retención de cajas durante un largo periodo",
    "el hijo del dueño es una persona agradable",
    "al tener problemas con el lector de códigos de barras",
]

# --------------------------------------------------------------------------
# 3. Retencion -> incidencia, cuando es operativo
# --------------------------------------------------------------------------

RETENCION_OPERATIVA = [
    (r"\bretenci[oó]n de (paquetes?|env[ií]os?|cajas?)\b", "demoras en la entrega"),
    (r"\bretenci[oó]n del paquete\b", "demora en la entrega del paquete"),
    (r"\bpaquetes? retenidos?\b", "paquetes con demoras"),
    (r"\benv[ií]os? retenidos?\b", "envíos con demoras"),
    (r"\bretener (los |el |un )?(paquetes?|env[ií]os?)\b", "acumular demoras en los envíos"),
]

# --------------------------------------------------------------------------
# 4. Gramatica
# --------------------------------------------------------------------------

# Mayuscula intrusa a mitad de frase. Solo se corrigen las combinaciones
# detectadas, para no tocar nombres propios legitimos.
PALABRAS_INTRUSAS = [
    "Destaca", "Entre", "Se", "Valora", "Ofrece", "Cuenta", "Dispone",
    "Aunque", "Mientras", "Tambien", "También", "Además", "Ademas",
    "Algunos", "Varios", "Muchos", "Otros", "Este", "Esta", "Sus", "Su",
    "Los", "Las", "El", "La", "Un", "Una", "Con", "Por", "Para", "Sin",
]

ARREGLOS_GRAMATICA = [
    # "Mientras que Entre" y variantes de conector + mayuscula.
    (r"\b(que|y|o|pero|aunque|mientras|donde|cuando|si|como|del|de la|en el|en la)\s+"
     r"(" + "|".join(PALABRAS_INTRUSAS) + r")\b",
     lambda m: f"{m.group(1)} {m.group(2).lower()}"),
    # "Se valora" arrancando frase que no empieza: se resuelve por contexto abajo.
    (r"\blas informaci[oó]n\b", "la información"),
    (r"\bLas informaci[oó]n\b", "La información"),
    (r"\binformaci[oó]n mixtas\b", "información mixta"),
    (r"\bla informaci[oó]n son\b", "la información es"),
    (r"\binformaci[oó]n y informaci[oó]n\b", "información"),
    (r"\bdatos y datos\b", "datos"),
    (r"\bservicios y servicios\b", "servicios"),
    (r"\s+([,.;:])", r"\1"),
    (r"[ \t]{2,}", " "),
    (r"\(\s*\)", ""),
    (r",\s*,", ","),
]


def corregir_gramatica(texto: str) -> tuple[str, int]:
    cambios = 0
    for patron, reemplazo in ARREGLOS_GRAMATICA:
        texto, n = re.subn(patron, reemplazo, texto)
        cambios += n

    # "Se valora" a mitad de frase: solo si no abre oracion ni parrafo.
    def bajar(match: re.Match) -> str:
        return match.group(1) + match.group(2).lower()

    texto, n = re.subn(r"([^.!?\n]\s)(Se valora\b)", bajar, texto)
    cambios += n
    return texto, cambios


# --------------------------------------------------------------------------
# 5. Nombres personales procedentes de comentarios
# --------------------------------------------------------------------------

# Solo se toca cuando el nombre aparece detras de un rol y no forma parte del
# nombre comercial de la ficha. Un "Locutorio Jack" conserva su Jack.
# El separador entre rol y nombre no puede contener saltos de linea: sin esa
# restriccion el patron saltaba de parrafo y se llevaba por delante la palabra
# inicial del siguiente ("propietario\n\nComo" -> se comia el "Como").
ROL_MAS_NOMBRE = re.compile(
    r"\b(el|la|un|una)?[ \t]*(emplead[oa]|trabajador[ae]?|dependient[ae]|chic[oa]|"
    r"encargad[oa]|camarer[oa]|se[ñn]or[a]?|compa[ñn]er[oa]|due[ñn][oa]|propietari[oa])"
    r"[ \t]*(?:,[ \t]*)?(?:llamad[oa][ \t]+|de nombre[ \t]+)?"
    r"([A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,})\b"
)

CONECTORES = {
    "El", "La", "Los", "Las", "Un", "Una", "Este", "Esta", "Su", "Sus",
    "Que", "Como", "Para", "Por", "Con", "Sin", "Desde", "Hasta", "Entre",
    "Tambien", "También", "Ademas", "Además", "Aunque", "Pero", "Sino",
}


def quitar_nombres(texto: str, nombre_negocio: str) -> tuple[str, int]:
    tokens_negocio = {
        _normalizar(p) for p in re.split(r"[\s\-_/&]+", nombre_negocio) if p
    }
    cambios = 0

    def reemplazo(match: re.Match) -> str:
        nonlocal cambios
        articulo = (match.group(1) or "").strip()
        rol = match.group(2)
        nombre = match.group(3)

        # No se toca si es conector, ni si pertenece al rotulo comercial.
        if nombre in CONECTORES or _normalizar(nombre) in tokens_negocio:
            return match.group(0)

        cambios += 1
        return f"{articulo} {rol}".strip()

    return ROL_MAS_NOMBRE.sub(reemplazo, texto), cambios


def _normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = texto.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "", texto)


# --------------------------------------------------------------------------
# 9. Bloques repetidos entre fichas
# --------------------------------------------------------------------------

# Frase inventada que afirmaba una tendencia del sector sin respaldo.
FRASE_INVENTADA = re.compile(
    r"El env[ií]o de dinero al extranjero es el servicio que m[aá]s ha crecido[^.]*\.\s*",
    re.IGNORECASE,
)

# Variantes para los bloques que se repetian decenas de veces. El reparto es
# estable por ficha, asi que la misma ficha muestra siempre la misma version.
VARIANTES_ENVIO = [
    "Para tramitar una remesa hace falta un documento de identidad en vigor y los datos "
    "completos del destinatario. La comisión no es uniforme: depende del operador, del país "
    "al que se envía y de si el pago se hace en efectivo o con tarjeta.",

    "Antes de enviar dinero conviene tener a mano el documento de identidad y los datos del "
    "destinatario tal y como figuran en el suyo, porque cualquier discrepancia bloquea la "
    "operación. El importe final varía según el corredor y la forma de pago.",

    "En los envíos de dinero, el coste depende de tres factores: el operador con el que "
    "trabaje el local, el país de destino y el método de pago. Preguntar el total antes de "
    "confirmar la operación evita sorpresas al recoger el resguardo.",

    "La documentación de identidad es obligatoria para cursar una remesa, y los datos del "
    "destinatario deben coincidir con los de su documento. Las tarifas cambian de un corredor "
    "a otro, de modo que compensa consultarlas para el destino concreto.",
]

VARIANTES_PAGO = [
    "El establecimiento admite tarjetas de crédito y débito, además de pago móvil por NFC, "
    "de modo que no hace falta llevar efectivo para la mayoría de gestiones.",

    "Entre las formas de pago constan tarjeta de crédito, tarjeta de débito y pago con el "
    "teléfono mediante NFC. Aun así, para importes pequeños algunos locales prefieren efectivo.",

    "Se puede pagar con tarjeta o acercando el móvil al datáfono. Conviene confirmarlo de todos "
    "modos si la gestión implica una cantidad elevada.",

    "Acepta tarjeta y pago contactless desde el teléfono, algo práctico para quien no suele "
    "llevar dinero en metálico encima.",
]

VARIANTES_CONSEJO = [
    "Los horarios de estos negocios cambian con frecuencia y no siempre se reflejan en "
    "internet, así que una llamada previa sigue siendo la forma más fiable de confirmarlos.",

    "Conviene confirmar por teléfono la disponibilidad del servicio concreto que se necesita, "
    "porque no todos los locales mantienen la misma oferta a lo largo del año.",

    "Una llamada breve antes de salir de casa ahorra el desplazamiento si ese día no está "
    "disponible el servicio que se busca.",

    "Como la oferta de estos establecimientos varía, comprobar por adelantado que prestan el "
    "servicio que se necesita evita un viaje en balde.",
]


def variante(opciones: list[str], semilla: str) -> str:
    valor = 0
    for caracter in semilla:
        valor = (valor * 31 + ord(caracter)) & 0xFFFFFFFF
    return opciones[valor % len(opciones)]


# --------------------------------------------------------------------------
# 6. Restaurar el detalle de la direccion
#
# La pasada anterior trato "Bajo", "Posterior" y "Local" como artefactos de
# parseo y los elimino. Son parte legitima de la direccion: identifican la
# planta o el local dentro del portal, y sin ellos la ficha pierde precision.
# Se recuperan de la version previa salvo en las direcciones que si habia que
# corregir por geografia.
# --------------------------------------------------------------------------

DETALLES_VALIDOS = re.compile(
    r"\b(bajo|bajos|posterior|local|entresuelo|entlo|principal|"
    r"planta|piso|puerta|esc|escalera|interior|trasera)\b",
    re.IGNORECASE,
)


def restaurar_direccion(ficha: dict, anterior: dict | None) -> tuple[str, bool]:
    if not anterior:
        return ficha["direccion"], False

    original = anterior.get("direccion", "")
    actual = ficha["direccion"]
    if not original or original == actual:
        return actual, False

    # Solo se restaura si lo perdido es un detalle de planta o local y la
    # localidad de la direccion original ya era correcta.
    perdidos = [
        parte.strip() for parte in original.split(",")
        if DETALLES_VALIDOS.fullmatch(parte.strip()) and parte.strip() not in actual
    ]
    if not perdidos:
        return actual, False

    ciudad = ficha.get("ciudad", "")
    if ciudad and _normalizar(ciudad) not in _normalizar(original):
        # La direccion original tenia mal la localidad: se conserva la
        # corregida y solo se reinserta el detalle tras el numero.
        partes = actual.split(",")
        if len(partes) >= 2:
            partes.insert(2, f" {perdidos[0]}")
            return ",".join(partes), True
        return actual, False

    return original, True


# --------------------------------------------------------------------------
# 7. MoneyGram de Montornes del Valles
# --------------------------------------------------------------------------

CORRECCION_MONTORNES = {
    "codigoPostal": "08170",
    "calle_contiene": "Federico García Lorca",
    "slugProvincia": "barcelona",
    "slugCiudad": "montornes-del-valles",
    "ciudad": "Montornès del Vallès",
    "provincia": "Barcelona",
}


def corregir_montornes(ficha: dict) -> bool:
    if ficha.get("codigoPostal") != CORRECCION_MONTORNES["codigoPostal"]:
        return False
    if CORRECCION_MONTORNES["calle_contiene"] not in (ficha.get("calle", "") + ficha.get("direccion", "")):
        return False
    if ficha["slugCiudad"] == CORRECCION_MONTORNES["slugCiudad"]:
        return False

    ficha["slugCiudad"] = CORRECCION_MONTORNES["slugCiudad"]
    ficha["ciudad"] = CORRECCION_MONTORNES["ciudad"]
    ficha["provincia"] = CORRECCION_MONTORNES["provincia"]
    ficha["slug"] = "moneygram"

    # La cadena de direccion tambien decia Barcelona.
    ficha["direccion"] = re.sub(
        r"08170\s+[^,]+", f"08170 {CORRECCION_MONTORNES['ciudad']}", ficha["direccion"]
    )
    # Y el texto editorial.
    for campo in ("cuerpo", "resumen", "titulo", "metaTitulo", "metaDescripcion"):
        if ficha.get(campo):
            ficha[campo] = re.sub(
                r"\bBarcelona ciudad\b", CORRECCION_MONTORNES["ciudad"], ficha[campo]
            )
    return True


# --------------------------------------------------------------------------
# 8. Atributos duplicados
# --------------------------------------------------------------------------

def deduplicar_atributos(ficha: dict) -> int:
    quitados = 0
    for grupo in ficha.get("atributos", []):
        vistos = set()
        unicos = []
        for valor in grupo["valores"]:
            clave = _normalizar(valor)
            if clave in vistos:
                quitados += 1
                continue
            vistos.add(clave)
            unicos.append(valor)
        grupo["valores"] = unicos

    # Grupos repetidos con el mismo nombre: se fusionan conservando el orden.
    fusionados: dict[str, dict] = {}
    for grupo in ficha.get("atributos", []):
        clave = _normalizar(grupo["grupo"])
        if clave in fusionados:
            existentes = {_normalizar(v) for v in fusionados[clave]["valores"]}
            for valor in grupo["valores"]:
                if _normalizar(valor) not in existentes:
                    fusionados[clave]["valores"].append(valor)
                else:
                    quitados += 1
        else:
            fusionados[clave] = grupo
    ficha["atributos"] = list(fusionados.values())
    return quitados


# --------------------------------------------------------------------------
# Proceso
# --------------------------------------------------------------------------

def quitar_frases(cuerpo: str) -> tuple[str, int]:
    """Elimina las frases listadas a mano, dejando el parrafo bien formado."""
    quitadas = 0
    bloques = []
    for parrafo in cuerpo.split("\n\n"):
        if parrafo.strip().startswith("##"):
            bloques.append(parrafo)
            continue
        conservadas = []
        for frase in re.split(r"(?<=[.!?])\s+", parrafo.strip()):
            if any(marca.lower() in frase.lower() for marca in FRASES_FUERA):
                quitadas += 1
                continue
            conservadas.append(frase)
        texto = " ".join(conservadas).strip()
        if texto:
            bloques.append(texto)

    # Encabezado que se queda sin parrafo debajo.
    limpio = []
    for indice, bloque in enumerate(bloques):
        if bloque.lstrip().startswith("##"):
            siguiente = bloques[indice + 1] if indice + 1 < len(bloques) else ""
            if not siguiente or siguiente.lstrip().startswith("##"):
                continue
        limpio.append(bloque)
    return "\n\n".join(limpio), quitadas


def diversificar(cuerpo: str, semilla: str) -> tuple[str, int]:
    """Rompe la repeticion literal de los bloques anadidos al ampliar."""
    cambios = 0

    nuevo, n = FRASE_INVENTADA.subn("", cuerpo)
    cambios += n
    cuerpo = nuevo

    marca_envio = "Para tramitar una remesa hace falta un documento de identidad en vigor"
    if marca_envio in cuerpo:
        elegida = variante(VARIANTES_ENVIO, semilla)
        cuerpo = re.sub(
            re.escape(marca_envio) + r"[^\n]*?(?=\n|$)", elegida, cuerpo, count=1
        )
        cambios += 1

    marca_consejo = "Los horarios de estos negocios cambian con frecuencia"
    if marca_consejo in cuerpo:
        elegida = variante(VARIANTES_CONSEJO, semilla + "c")
        cuerpo = re.sub(
            re.escape(marca_consejo) + r"[^.]*\.", elegida, cuerpo, count=1
        )
        cambios += 1

    marca_pago = "En cuanto a los métodos de pago, el establecimiento acepta tarjetas de crédito"
    if marca_pago in cuerpo:
        elegida = variante(VARIANTES_PAGO, semilla + "p")
        cuerpo = re.sub(re.escape(marca_pago) + r"[^.]*\.[^.]*\.", elegida, cuerpo, count=1)
        cambios += 1

    for apertura in ("Antes de desplazarse, conviene",
                     "Para no hacer el viaje en balde, merece la pena",
                     "Antes de acudir resulta útil"):
        if apertura in cuerpo:
            nueva = variante([
                "Antes de desplazarse, conviene",
                "Para no hacer el viaje en balde, merece la pena",
                "Antes de acudir resulta útil",
                "Merece la pena, antes de ir,",
                "Como preparación, ayuda",
            ], semilla + "a")
            if nueva != apertura:
                cuerpo = cuerpo.replace(apertura, nueva, 1)
                cambios += 1
            break

    cuerpo = re.sub(r"\n{3,}", "\n\n", cuerpo)
    return cuerpo.strip(), cambios


def procesar(directorio: Path, simular: bool) -> None:
    total: Counter = Counter()
    tocadas = 0
    detalle: list[dict] = []

    anteriores: dict[str, dict] = {}
    if DIR_ANTERIOR.exists():
        for archivo in (DIR_ANTERIOR / "listings").glob("*.json"):
            for ficha in json.loads(archivo.read_text(encoding="utf-8")):
                anteriores[ficha["id"]] = ficha

    datos = {
        archivo.stem: json.loads(archivo.read_text(encoding="utf-8"))
        for archivo in sorted((directorio / "listings").glob("*.json"))
    }
    todas = [f for fichas in datos.values() for f in fichas]

    for ficha in todas:
        cambios: Counter = Counter()
        cuerpo = ficha["cuerpo"]

        # 1 y 2
        cuerpo, n = quitar_frases(cuerpo)
        cambios["frases_eliminadas"] += n

        # 3
        for patron, reemplazo in RETENCION_OPERATIVA:
            cuerpo, n = re.subn(patron, reemplazo, cuerpo, flags=re.IGNORECASE)
            cambios["retenciones_reformuladas"] += n

        # 9
        cuerpo, n = diversificar(cuerpo, ficha["id"])
        cambios["bloques_diversificados"] += n

        # 4
        cuerpo, n = corregir_gramatica(cuerpo)
        cambios["gramatica"] += n
        resumen, n2 = corregir_gramatica(ficha["resumen"])
        cambios["gramatica"] += n2

        # 5
        cuerpo, n = quitar_nombres(cuerpo, ficha["nombre"])
        cambios["nombres_eliminados"] += n

        # 8
        cambios["atributos_deduplicados"] += deduplicar_atributos(ficha)

        # 6 — se escribe ya en la ficha para que la correccion geografica
        # posterior trabaje sobre la direccion definitiva y no la pierda.
        direccion, restaurada = restaurar_direccion(ficha, anteriores.get(ficha["id"]))
        if restaurada:
            cambios["direcciones_restauradas"] += 1
            if not simular:
                ficha["direccion"] = direccion

        # 7 — va la ultima porque reescribe la cadena de direccion.
        if corregir_montornes(ficha):
            cambios["montornes"] += 1

        if not any(cambios.values()):
            continue

        if not simular:
            ficha["cuerpo"] = cuerpo
            ficha["resumen"] = resumen

        tocadas += 1
        total.update(cambios)
        if len(detalle) < 60:
            detalle.append({
                "nombre": ficha["nombre"],
                "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                "cambios": {k: v for k, v in cambios.items() if v},
            })

    # La ficha de Montornes cambia de ciudad: hay que reagrupar por provincia.
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
                encoding="utf-8",
            )

    (directorio / "informe-correccion-final.json").write_text(
        json.dumps({"fichasTocadas": tocadas, "recuentos": dict(total),
                    "muestra": detalle}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("SIMULACIÓN — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fichas tocadas: {tocadas}")
    for clave, valor in total.most_common():
        if valor:
            print(f"  {clave}: {valor}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
