#!/usr/bin/env python3
"""
Corrige la concordancia rota de "informacion" con adjetivos y verbos en plural.

ORIGEN
------
El fallo no lo introdujo ninguna pasada de este proyecto: esta en el CSV
original. El generador de resumen/metaDescripcion produjo sistematicamente
frases del tipo "la atencion al cliente genera informacion divididas" o "la
informacion son mixtas", donde "informacion" (femenino singular) queda
forzada junto a un adjetivo o verbo en plural.

LA REPARACION
--------------
El significado que la frase intenta transmitir siempre es el mismo: opiniones
de clientes que no coinciden. "opiniones divididas" y "opiniones encontradas"
son ademas expresiones idiomaticas naturales del espanol, mas naturales que
forzar la concordancia a "informacion dividida". Sustituir el sustantivo
"informacion" por "opiniones" resuelve la concordancia y mejora la redaccion
en el mismo movimiento, sin cambiar el sentido de la frase.

Se cubren tres formas:
  A. "informacion" + adjetivo plural cercano (divididas, encontradas, mixtas...)
  B. "la informacion ... son/estan ..." -> concordancia de articulo y verbo
  C. "informacion y informacion" (duplicacion) y demas casos sueltos, resueltos
     uno a uno tras inspeccion manual.

Uso:  python3 reparar_concordancia_informacion.py ./data [--simular]
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------
# A. "información" + adjetivo plural, con o sin verbo intermedio.
#
# Un unico patron cubre las variantes reales encontradas:
#   "información divididas"                  (adjetivo pegado)
#   "la información ... divididas"           (articulo + hueco + adjetivo)
#   "la información es variadas"             (verbo singular + adjetivo plural)
#   "la información son/están mixtas"        (verbo ya en plural)
# Se reconstruye articulo (las), sustantivo (opiniones) y verbo (son/están)
# a la vez, para no dejar una concordancia rota en el sentido contrario.
# --------------------------------------------------------------------------

ADJETIVOS_PLURAL = (
    r"divididas|encontradas|mixtas|variadas|dispares|desiguales|"
    r"distintas|diferentes|contradictorias"
)

# Dos patrones separados, no uno con artículo opcional. La razón: con el
# artículo opcional, cuando no hay artículo, el \b inicial ancla justo
# después de la palabra anterior ("genera") y el \s* siguiente se come el
# espacio — que luego no se restituye en la reconstrucción, dejando
# "generaopiniones". Separando los casos, el patrón sin artículo empieza
# exactamente en "información" y nunca toca el espacio que lo precede.

PATRON_CON_ARTICULO = re.compile(
    r"\b(la|las|una|un)\s+informaci[oó]n\b\s*"
    r"(es|son|est[aá]n)?"
    r"((?:(?!\.|informaci[oó]n).){0,40}?)\b(" + ADJETIVOS_PLURAL + r")\b",
    re.IGNORECASE,
)

PATRON_SIN_ARTICULO = re.compile(
    r"\binformaci[oó]n\b\s*"
    r"(es|son|est[aá]n)?"
    r"((?:(?!\.|informaci[oó]n).){0,40}?)\b(" + ADJETIVOS_PLURAL + r")\b",
    re.IGNORECASE,
)


def _verbo_plural(verbo: str | None) -> str | None:
    if not verbo:
        return None
    return {"es": "son", "está": "están", "esta": "estan"}.get(verbo.lower(), verbo)


def reparar(texto: str) -> tuple[str, int]:
    if not texto or "informaci" not in texto.lower():
        return texto, 0

    cambios = 0

    def con_articulo(m: re.Match) -> str:
        nonlocal cambios
        cambios += 1
        inicio_frase = bool(re.search(r"(^|[.\n]\s*)$", texto[:m.start()]))
        articulo = "Las" if inicio_frase else "las"
        verbo = _verbo_plural(m.group(2))
        resto = m.group(3).strip()
        piezas = [articulo, "opiniones"]
        if verbo:
            piezas.append(verbo)
        if resto:
            piezas.append(resto)
        piezas.append(m.group(4))
        return " ".join(piezas)

    texto = PATRON_CON_ARTICULO.sub(con_articulo, texto)

    def sin_articulo(m: re.Match) -> str:
        nonlocal cambios
        cambios += 1
        verbo = _verbo_plural(m.group(1))
        resto = m.group(2).strip()
        piezas = ["opiniones"]
        if verbo:
            piezas.append(verbo)
        if resto:
            piezas.append(resto)
        piezas.append(m.group(3))
        return " ".join(piezas)

    texto = PATRON_SIN_ARTICULO.sub(sin_articulo, texto)
    return texto, cambios


# --------------------------------------------------------------------------
# B. "la información ... son/están ..." con el adjetivo mas lejos del limite
#    de 40 caracteres del patron principal, o sin adjetivo de la lista (p.ej.
#    "escasas y contradictorias"). Se cubre aparte, con articulo y verbo.
# --------------------------------------------------------------------------

PATRON_B = re.compile(
    r"\b(la|las)\s+informaci[oó]n\b((?:(?!\.).){0,60}?)\b(son|están)\b",
    re.IGNORECASE,
)


def reparar_b(texto: str) -> tuple[str, int]:
    if not texto or "informaci" not in texto.lower():
        return texto, 0
    cambios = 0

    def sustituir(m: re.Match) -> str:
        nonlocal cambios
        cambios += 1
        inicio_frase = bool(re.search(r"(^|[.\n]\s*)$", texto[:m.start()]))
        articulo = "Las" if inicio_frase else "las"
        resto = m.group(2).strip()
        piezas = [articulo, "opiniones"]
        if resto:
            piezas.append(resto)
        piezas.append(m.group(3))
        return " ".join(piezas)

    texto = PATRON_B.sub(sustituir, texto)
    return texto, cambios


# --------------------------------------------------------------------------
# C. Casos sueltos que no encajan en el patrón general.
#
# Se listan tras inspeccion manual del texto completo de cada ficha, porque
# la reformulacion no es un simple cambio de sustantivo.
# --------------------------------------------------------------------------

CASOS_MANUALES = [
    # Doble "información" en metaTitulo — se reduce a un único término.
    ("Locutorio Afih", "metaTitulo",
     "Locutorio Afih en Sevilla - Información y información",
     "Locutorio Afih en Sevilla - Servicios y ubicación"),
    ("Locutorio Girona", "metaTitulo",
     "Locutorio Girona en Barcelona: información y información",
     "Locutorio Girona en Barcelona: servicios y ubicación"),

    # "las pocas información disponibles son favorables" — mezcla artículo
    # plural, sustantivo singular y adjetivo plural en la misma frase.
    ("Locutorio PUNJAB PUÇOL", "resumen",
     "aunque las pocas información disponibles son favorables",
     "aunque las pocas opiniones disponibles son favorables"),

    # "la información de los clientes son escasas y contradictorias"
    ("Locutorio Touba Phone", "resumen",
     "La información de los clientes son escasas y contradictorias",
     "Las opiniones de los clientes son escasas y contradictorias"),
]


def aplicar_casos_manuales(fichas_por_nombre: dict) -> int:
    aplicados = 0
    for nombre, campo, buscar, reemplazar in CASOS_MANUALES:
        for ficha in fichas_por_nombre.get(nombre, []):
            valor = ficha.get(campo) or ""
            if buscar in valor:
                ficha[campo] = valor.replace(buscar, reemplazar)
                aplicados += 1
    return aplicados


# --------------------------------------------------------------------------

def procesar(directorio: Path, simular: bool) -> None:
    total: Counter = Counter()
    tocadas = 0
    detalle = []

    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        modificado = False

        fichas_por_nombre: dict[str, list] = {}
        for ficha in fichas:
            fichas_por_nombre.setdefault(ficha["nombre"], []).append(ficha)

        for ficha in fichas:
            cambios_ficha = 0
            for campo in ("cuerpo", "resumen", "titulo", "metaTitulo", "metaDescripcion"):
                valor = ficha.get(campo) or ""
                nuevo, n1 = reparar(valor)
                nuevo, n2 = reparar_b(nuevo)
                n = n1 + n2
                if n:
                    cambios_ficha += n
                    if not simular:
                        ficha[campo] = nuevo
                    detalle.append({
                        "nombre": ficha["nombre"],
                        "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                        "campo": campo,
                        "antes": valor[:150],
                        "despues": nuevo[:150],
                    })

            if cambios_ficha:
                total["reparaciones_patron"] += cambios_ficha
                tocadas += 1
                modificado = True

        aplicados = aplicar_casos_manuales(fichas_por_nombre)
        if aplicados:
            total["casos_manuales"] += aplicados
            modificado = True

        if modificado and not simular:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")

    (directorio / "informe-concordancia-informacion.json").write_text(
        json.dumps({"fichasTocadas": tocadas, "recuentos": dict(total),
                   "detalle": detalle}, ensure_ascii=False, indent=2),
        encoding="utf-8")

    print("SIMULACIÓN — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fichas tocadas: {tocadas}")
    for clave, valor in total.most_common():
        print(f"  {clave}: {valor}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
