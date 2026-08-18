#!/usr/bin/env python3
"""
Controles finales.

Nueve correcciones puntuales sobre la version actual. Ninguna reescribe fichas
completas: cada una actua sobre un defecto identificado y deja el resto igual.

  1. Ocho fichas nombradas: fuera la acusacion, dentro la critica operativa.
  2. "muchos se valora" -> "muchos valoran".
  3. Atributos repetidos dentro del cuerpo redactado.
  4. Nombres personales de resenas, respetando calles y rotulos.
  5. Encabezados con marco de sospecha.
  6. Titulos y metadescripciones con la misma formula.
  7. La frase del telefono, identica en 389 fichas.
  8. UNKNOWN fuera del indice y del sitemap.

Uso:  python3 controles_finales.py ./data [--simular]
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# 1. Fichas nombradas
#
# Se listan una a una porque cada caso se ha leido. La regla es la acordada:
# la acusacion desaparece; si detras hay un problema operativo recurrente, ese
# se queda, reformulado como tendencia y sin el relato individual.
# --------------------------------------------------------------------------

REEMPLAZOS_FRASE = [
    # Mehdi Telecom — "sospechas de copia de archivos" es una imputacion.
    # Queda la demora, que es el problema operativo real.
    (r"También se ha mencionado una experiencia negativa con el servicio de "
     r"impresión, con demoras y sospechas de copia de archivos, aunque se trata "
     r"de un caso aislado\.",
     "También se han mencionado demoras puntuales en el servicio de impresión."),

    # LOCUTORIOLAILA — "piezas no originales" acusa de fraude en la reparacion.
    (r"En concreto, se menciona un incidente en el que el cliente se sintió mal "
     r"atendido y además sospechó que se habían utilizado piezas no originales\.",
     "En concreto, se menciona alguna experiencia de atención poco satisfactoria "
     "en el servicio de reparación."),

    # Shafer y Anwar — "retenciones indebidas" imputa apropiacion. La
    # dificultad para localizar paquetes es operativa y se conserva.
    (r"Mientras que algunos clientes lo utilizan para recibir envíos de "
     r"plataformas como Amazon, otros han reportado problemas para localizar los "
     r"paquetes o incluso retenciones indebidas\.",
     "Aunque muchos clientes lo utilizan como punto de recogida de envíos, "
     "algunos mencionan dificultades para localizar los paquetes."),

    # Akash — trato discriminatorio por razon de sexo es una imputacion grave.
    (r"Algunas experiencias recientes describen situaciones de trato "
     r"discriminatorio hacia mujeres\.",
     "Algunas experiencias recientes describen un trato poco satisfactorio."),
    (r"Otro caso menciona que tuvo que regresar por un problema no especificado\.",
     ""),

    # Ciberb@dulake — "discriminatorio por parte de una empleada" senala a una
    # persona concreta. Queda la lentitud y el trato seco.
    (r"Por otro, existen testimonios que describen episodios de mal humor, "
     r"lentitud e incluso un trato percibido como discriminatorio por parte de "
     r"una empleada\.",
     "Por otro, algunos testimonios describen lentitud en la atención y un trato "
     "poco cordial."),

    # Pak Euro — "engaño a una persona mayor" imputa un delito y ademas
    # identifica a la victima por edad. Fuera entera.
    (r"Por otro lado, existe una queja sobre un posible engaño a una persona "
     r"mayor, un asunto delicado que conviene tener en cuenta\.", ""),

    # Juan Colombo (Parla) — el relato del trato individual desaparece; el
    # aviso general de que la atencion recibe criticas se mantiene.
    (r"La información disponible sobre la experiencia en el local es limitada, "
     r"pero existe una referencia que describe un trato poco amable por parte de[^.]*\.",
     "La información disponible sobre la experiencia en el local es limitada, "
     "aunque la atención ha recibido alguna crítica."),
    (r"Aunque se trata de un caso aislado, es un punto que el establecimiento "
     r"podría trabajar para mejorar la experiencia general\.", ""),

    (r"pero también se ha mencionado la posibilidad de que se utilicen piezas "
     r"no originales[^.]*\.",
     "aunque conviene consultar de antemano el presupuesto y la garantía."),

    (r"Esta práctica ha generado malestar entre algunos usuarios, que la "
     r"consideran injustificada y sospechosa\.",
     "Esta práctica ha generado malestar entre algunos usuarios."),

    (r"Varias personas han expresado su descontento, indicando que no se les "
     r"entregó ningún comprobante ni se registró la entrega[^.]*\.",
     "Varias personas han echado en falta un comprobante de la entrega."),
]

# --------------------------------------------------------------------------
# 2 y 3. Gramatica y repeticiones de atributos
# --------------------------------------------------------------------------

ARREGLOS = [
    # "un detalle que muchos se valora" -> "que muchos valoran"
    (r"\bque muchos se valora\b", "que muchos valoran"),
    (r"\bmuchos se valora\b", "muchos valoran"),
    (r"\bque muchos se valoran\b", "que muchos valoran"),

    # Listas de atributos con el mismo valor repetido.
    (r"tarjetas de cr[eé]dito, tarjetas de d[eé]bito, tarjetas de cr[eé]dito",
     "tarjetas de crédito y débito"),
    (r"tarjetas de cr[eé]dito, tarjetas de cr[eé]dito", "tarjetas de crédito"),
    (r"tarjetas de d[eé]bito, tarjetas de d[eé]bito", "tarjetas de débito"),
    (r"\bwi-?fi, wi-?fi\b", "wifi"),
    (r"\b(\w+), \1, \1\b", r"\1"),
    (r"\by y\b", "y"),
    (r"\by, y\b", "y"),
    (r",[ \t]*,", ","),
    # Ojo: [ \t] y no \s, porque \s incluye el salto de linea y colapsaria
    # los parrafos, dejando los encabezados a mitad de linea.
    (r"[ \t]{2,}", " "),
    (r"[ \t]+([,.;:])", r"\1"),
]

# --------------------------------------------------------------------------
# 4. Nombres personales
#
# La mayoria de coincidencias no son personas del local: "calle Antonio
# Burgos", "avenida de Eduardo Dato", "Locutorio El Rocio". Solo se elimina
# cuando el nombre aparece como la persona que atiende.
# --------------------------------------------------------------------------

NOMBRES_DE_RESENA = ["Mónica", "Patricia", "María", "Marynel", "Mariluz"]

# Si alguna de estas marcas precede al nombre, es un toponimo o un rotulo.
CONTEXTO_NO_PERSONAL = re.compile(
    r"(calle|c/|c\.|avenida|avda|av\.|paseo|plaza|pl\.|travesía|travesia|ronda|"
    r"carrer|camino|barrio|locutorio|ciber|multiservicios|centro|tienda|"
    r"parroquia|iglesia|colegio|hospital|mercado|puente|madre|santa|san)\s*$",
    re.IGNORECASE,
)

# Frases enteras que giran alrededor de la persona: se sustituyen por su
# equivalente generico en vez de dejar un hueco sintactico.
PERSONA_A_GENERICO = [
    (r"\bel nombre de (?:%s) aparece de forma recurrente como sinónimo de\b" % "|".join(NOMBRES_DE_RESENA),
     "la atención recibe menciones recurrentes por su"),
    (r"\bel nombre de (?:%s) aparece asociado a\b" % "|".join(NOMBRES_DE_RESENA),
     "la atención aparece asociada a"),
    (r"\bcon especial mención a (?:%s)\b" % "|".join(NOMBRES_DE_RESENA),
     "con menciones especialmente positivas"),
    (r"\b(?:la figura|La figura) de (?:%s)\b" % "|".join(NOMBRES_DE_RESENA),
     "La atención personalizada"),
    (r"\bdestaca la figura de (?:%s), la persona que atiende el local\b" % "|".join(NOMBRES_DE_RESENA),
     "destaca la atención de quien atiende el local"),
    (r"\bespecialmente de (?:%s), que atiende el local\b" % "|".join(NOMBRES_DE_RESENA),
     "de quien atiende el local"),
    (r"\bvalora especialmente el trato de (?:%s), describiéndola como una persona\b" % "|".join(NOMBRES_DE_RESENA),
     "valora especialmente el trato recibido, descrito como"),
    (r"\bla disposición de (?:%s) a ayudar\b" % "|".join(NOMBRES_DE_RESENA),
     "la disposición a ayudar"),
    (r"\bSe describe a esta empleada como\b", "Se describe la atención como"),
    (r"\bel trato de (?:%s)\b" % "|".join(NOMBRES_DE_RESENA), "el trato recibido"),
    (r"\bla atención de (?:%s)\b" % "|".join(NOMBRES_DE_RESENA), "la atención recibida"),
    (r"\bla amabilidad de (?:%s)\b" % "|".join(NOMBRES_DE_RESENA), "la amabilidad del personal"),
    (r"\bde (?:%s), con su trato cercano y su implicación,\b" % "|".join(NOMBRES_DE_RESENA),
     "del trato cercano y la implicación,"),
]

# --------------------------------------------------------------------------
# 5. Encabezados
# --------------------------------------------------------------------------

ENCABEZADO_MARCADO = re.compile(
    r"controversia|bajo sospecha|puntos? d[eé]bil|luces y sombras|"
    r"pol[eé]mic|lo que falla|aspectos? negativ|sombras|"
    r"entre la amabilidad y|fricci[oó]n|fricciones|limitaciones|"
    r"señales a considerar|reservas",
    re.IGNORECASE,
)

ENCABEZADOS_NEUTROS = [
    "Qué destacan los usuarios",
    "La experiencia de los clientes",
    "Servicio y atención",
    "Lo que cuentan quienes lo han usado",
    "Valoraciones de los usuarios",
]

# --------------------------------------------------------------------------
# 6. Metadatos
# --------------------------------------------------------------------------

# La formula aparece de dos maneras: como coletilla final ("…, pero con
# sombras en la atencion") y encajada a mitad de frase ("envios de dinero con
# un punto debil en el horario"). Se cubren las dos.
META_MARCADA = re.compile(
    r"\s*[,:]?\s*(pero |aunque |y )?(con |sin )?(un[ao]s? |algun[ao]s? |ciert[ao]s? )?"
    r"(sombras?|controversias?|puntos? d[eé]biles?|luces y sombras|"
    r"opiniones divididas|pol[eé]mica|reservas|matices|cautela|"
    r"limitaciones|fricci[oó]n(?:es)?)"
    r"[^.]*",
    re.IGNORECASE,
)

# Formulas encajadas a mitad de texto. Se sustituyen por su equivalente
# descriptivo en vez de recortar, porque detras suele venir informacion util
# ("un punto debil en el horario" -> "horarios limitados") y truncar la frase
# perderia ese dato.
META_PUNTUAL = [
    (r"\s*Un servicio esencial con un punto d[eé]bil en la atención al cliente\.?",
     " La atención al cliente recibe valoraciones desiguales."),
    (r",? aunque los horarios son un punto d[eé]bil\.?",
     ", con horarios limitados."),
    (r"\s*La atención al cliente es un punto d[eé]bil recurrente, aunque la "
     r"variedad de productos es valorada\.?",
     " La atención al cliente recibe valoraciones desiguales y la variedad de "
     "productos se menciona de forma positiva."),
    (r":\s*envíos de dinero con un punto d[eé]bil en el horario",
     ": envíos de dinero con horario limitado"),
    (r":\s*servicios de barrio con un punto d[eé]bil claro",
     ": servicios de barrio"),
    (r":\s*paquetería y atención cercana con un punto d[eé]bil en los horarios",
     ": paquetería y atención cercana, con horario limitado"),
]


# --------------------------------------------------------------------------
# 7. La frase del telefono
# --------------------------------------------------------------------------

FRASE_TELEFONO = (
    "Tiene teléfono publicado, lo que permite confirmar por adelantado si el "
    "servicio concreto que se necesita está disponible ese día."
)

VARIANTES_TELEFONO = [
    "El teléfono aparece publicado, de modo que se puede comprobar por "
    "adelantado si prestan el servicio que se busca.",

    "Al figurar el número de contacto, una llamada breve basta para confirmar "
    "disponibilidad antes de acercarse.",

    "Dispone de teléfono, lo que ahorra el desplazamiento cuando se necesita un "
    "servicio concreto y no se sabe si está operativo.",

    "El número de contacto está disponible en esta ficha, útil para resolver "
    "dudas sobre horarios o servicios antes de ir.",

    "Cuenta con teléfono publicado, la vía más rápida para confirmar que ese día "
    "atienden la gestión que se necesita.",

    "Tiene número de contacto, algo práctico en un tipo de negocio donde la "
    "oferta de servicios varía de un local a otro.",
]


def variante(opciones: list[str], semilla: str) -> str:
    valor = 0
    for caracter in semilla:
        valor = (valor * 31 + ord(caracter)) & 0xFFFFFFFF
    return opciones[valor % len(opciones)]


# --------------------------------------------------------------------------
# Procesado
# --------------------------------------------------------------------------

def limpiar_parrafos(cuerpo: str) -> str:
    """Recompone tras las sustituciones vacías, sin dejar huecos ni H2 sueltos."""
    bloques = []
    for parrafo in cuerpo.split("\n\n"):
        limpio = re.sub(r"[ \t]{2,}", " ", parrafo).strip()
        if limpio:
            bloques.append(limpio)

    limpio_final = []
    for indice, bloque in enumerate(bloques):
        if bloque.startswith("##"):
            siguiente = bloques[indice + 1] if indice + 1 < len(bloques) else ""
            if not siguiente or siguiente.startswith("##"):
                continue
        limpio_final.append(bloque)
    return "\n\n".join(limpio_final)


def quitar_nombres(texto: str, nombre_negocio: str) -> tuple[str, int]:
    cambios = 0

    for patron, reemplazo in PERSONA_A_GENERICO:
        texto, n = re.subn(patron, reemplazo, texto)
        cambios += n

    # Barrido de los restos: el nombre suelto referido a quien atiende.
    for nombre in NOMBRES_DE_RESENA:
        if nombre.lower() in nombre_negocio.lower():
            continue  # forma parte del rótulo
        for match in list(re.finditer(r"\b" + nombre + r"\b", texto)):
            anterior = texto[max(0, match.start() - 30):match.start()]
            if CONTEXTO_NO_PERSONAL.search(anterior):
                continue  # es una calle o un nombre de local
            posterior = texto[match.end():match.end() + 40]
            if re.match(r"\s*(Teresa|del|de la|de los)\b", posterior):
                continue  # topónimo compuesto
            # Solo si el contexto habla de atención a clientes.
            if not re.search(r"atien|trato|amabilidad|simpat|person|emplead|"
                             r"encargad|servicio", anterior + posterior, re.I):
                continue
            texto = texto[:match.start()] + "el personal" + texto[match.end():]
            cambios += 1
            break

    return texto, cambios


def neutralizar_encabezados(cuerpo: str, semilla: str) -> tuple[str, int]:
    cambios = 0
    lineas = []
    for linea in cuerpo.split("\n"):
        if linea.startswith("##") and ENCABEZADO_MARCADO.search(linea):
            lineas.append("## " + variante(ENCABEZADOS_NEUTROS, semilla + str(len(lineas))))
            cambios += 1
        else:
            lineas.append(linea)
    return "\n".join(lineas), cambios


def neutralizar_meta(texto: str, es_titulo: bool = False) -> tuple[str, int]:
    """Quita la formula de sospecha. Los titulos no llevan punto final."""
    if not texto:
        return texto, 0
    original = texto

    # Primero las formulas encajadas, que conservan el dato de detras.
    for patron, reemplazo in META_PUNTUAL:
        texto = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    if texto != original:
        texto = re.sub(r"[ \t]{2,}", " ", texto).strip()
        return texto, 1

    if not META_MARCADA.search(texto):
        return texto, 0
    texto = META_MARCADA.sub("", texto)
    texto = re.sub(r"[ \t]*[:,;]\s*$", "", texto).strip()
    texto = re.sub(r"[ \t]{2,}", " ", texto)
    texto = re.sub(r"[ \t]+([,.])", r"\1", texto)
    if not es_titulo and texto and not texto.endswith("."):
        texto += "."
    return texto, int(texto != original)


def procesar(directorio: Path, simular: bool) -> None:
    total: Counter = Counter()
    tocadas = 0

    datos = {
        archivo.stem: json.loads(archivo.read_text(encoding="utf-8"))
        for archivo in sorted((directorio / "listings").glob("*.json"))
    }
    todas = [f for fichas in datos.values() for f in fichas]

    for ficha in todas:
        cambios: Counter = Counter()
        cuerpo = ficha["cuerpo"]

        # 1
        for patron, reemplazo in REEMPLAZOS_FRASE:
            cuerpo, n = re.subn(patron, reemplazo, cuerpo)
            cambios["fichas_nombradas"] += n

        # 2 y 3
        for patron, reemplazo in ARREGLOS:
            cuerpo, n = re.subn(patron, reemplazo, cuerpo, flags=re.IGNORECASE)
            cambios["gramatica_y_repeticiones"] += n

        # 4
        cuerpo, n = quitar_nombres(cuerpo, ficha["nombre"])
        cambios["nombres_eliminados"] += n

        # 5
        cuerpo, n = neutralizar_encabezados(cuerpo, ficha["id"])
        cambios["encabezados_neutralizados"] += n

        # 7
        if FRASE_TELEFONO in cuerpo:
            cuerpo = cuerpo.replace(FRASE_TELEFONO, variante(VARIANTES_TELEFONO, ficha["id"]), 1)
            cambios["frase_telefono_diversificada"] += 1

        cuerpo = limpiar_parrafos(cuerpo)

        # 6
        resumen = ficha.get("resumen", "")
        for patron, reemplazo in ARREGLOS:
            resumen = re.sub(patron, reemplazo, resumen, flags=re.IGNORECASE)
        resumen, n1 = neutralizar_meta(resumen)
        titulo, n2 = neutralizar_meta(ficha.get("titulo", ""), es_titulo=True)
        meta_titulo, n3 = neutralizar_meta(ficha.get("metaTitulo", ""), es_titulo=True)
        meta_desc, n4 = neutralizar_meta(ficha.get("metaDescripcion", ""))
        cambios["metas_neutralizadas"] += n1 + n2 + n3 + n4

        # 8 — UNKNOWN fuera del índice y del sitemap
        if ficha["nombre"].strip().upper() in {"UNKNOWN", "N/A", ""}:
            if not ficha.get("noIndexar") or not ficha.get("excluirSitemap"):
                cambios["unknown_desindexado"] += 1
            if not simular:
                ficha["noIndexar"] = True
                ficha["excluirSitemap"] = True

        if not any(cambios.values()):
            continue

        if not simular:
            ficha["cuerpo"] = cuerpo
            ficha["resumen"] = resumen
            if titulo:
                ficha["titulo"] = titulo
            if meta_titulo:
                ficha["metaTitulo"] = meta_titulo
            if meta_desc:
                ficha["metaDescripcion"] = meta_desc

        tocadas += 1
        total.update(cambios)

    if not simular:
        for slug, fichas in datos.items():
            (directorio / "listings" / f"{slug}.json").write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")

    (directorio / "informe-controles-finales.json").write_text(
        json.dumps({"fichasTocadas": tocadas, "recuentos": dict(total)},
                   ensure_ascii=False, indent=2), encoding="utf-8")

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
