#!/usr/bin/env python3
"""
Reduce el riesgo reputacional de los textos editoriales.

EL PROBLEMA
-----------
El riesgo no es haber leido opiniones publicas, sino publicarlas reescritas como
afirmaciones propias sobre personas identificables. En un locutorio de barrio con
una sola persona tras el mostrador, "la dependienta es antipatica" identifica a
alguien concreto aunque no se diga su nombre: articulo 7.7 de la LO 1/1982,
juicios de valor que lesionan la dignidad. Y palabras como "estafa" o "fraude"
son tipos penales; afirmarlos sin sentencia puede ser calumnia (art. 205 CP).

EL ENFOQUE
----------
Un primer intento reescribio las frases con expresiones regulares y produjo
castellano roto ("resulta un trato poco cordial, seca y con un trato distante")
ademas de destrozar usos neutros: "prevenir el fraude" quedo como "prevenir el
discrepancias sobre el servicio prestado".

La leccion es que reescribir prosa mecanicamente no funciona. Este script hace
otra cosa, y por eso si es seguro:

  NIVEL A — Eliminar. Frases que imputan un delito, una infraccion sanitaria o
  un juicio duro sobre una persona identificable. Quitar una frase de un texto
  de 745 palabras no cuesta casi nada y el resultado siempre es gramatical, que
  es mas de lo que puede decirse de cualquier reescritura automatica.

  NIVEL B — Desentrecomillar. 115 fichas incluyen fragmentos de resena entre
  comillas. Las comillas son la huella de que el texto se copio de algun sitio,
  y eso es precisamente lo que no interesa exhibir. Las cortas pierden solo las
  comillas: las palabras se integran en la frase y dejan de parecer una cita.
  Las largas (mas de 60 caracteres) son resenas reproducidas y su frase entera
  se elimina.

  NO SE ATRIBUYE AUTOMATICAMENTE. Se probo anteponer "segun opiniones de
  clientes" a las criticas moderadas y la deteccion capturaba "bebidas frias",
  "frutos secos" y "la ausencia de quejas". Distinguir por lexico una critica
  de una descripcion no es viable, y una atribucion mal puesta estropea el texto
  sin reducir riesgo alguno.

  NEUTRO — No tocar. "Prevenir el fraude" o "medidas contra la estafa" son usos
  descriptivos del sector, no acusaciones.

Uso:  python3 despersonalizar.py ./data [--simular]
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------
# Vocabulario
# --------------------------------------------------------------------------

# Tipos penales e imputaciones sanitarias.
DELITO = re.compile(
    r"\b(estafa\w*|fraudulent\w+|timad\w+|timo|robaban?|robaron|ladron\w*|"
    r"sinvergüenza\w*|mentiros[oa]s?|delincuentes?|"
    r"caducad[oa]s?|insalubres?|racistas?|xenófob[oa]s?)\b",
    re.IGNORECASE,
)

# Usos neutros que contienen la misma palabra. Si aparece alguno, la frase no
# es una acusacion y se deja intacta.
NEUTRO = re.compile(
    r"\b(prevenir|prevenci[oó]n|evitar|antifraude|protecci[oó]n|proteger|"
    r"seguridad|normativ\w+|cumplimiento|verificaci[oó]n|blanqueo|control\w*|"
    r"riesgo de|contra el|contra la|frente al?|fecha de caducidad|"
    r"fechas de caducidad)\b",
    re.IGNORECASE,
)

# Referencias a una persona fisica concreta del negocio.
PERSONA = re.compile(
    r"\b(dependient[ae]s?|encargad[oa]s?|propietari[oa]s?|dueñ[oa]s?|"
    r"emplead[oa]s?|trabajador[ae]s?|la chica|el chico|la señora|el señor|"
    r"la mujer|el hombre|el personal|la persona que atiende)\b",
    re.IGNORECASE,
)

# Juicios duros sobre el trato.
JUICIO_DURO = re.compile(
    r"\b(antipátic[oa]s?|maleducad[oa]s?|groser[oa]s?|bordes?|"
    r"despectiv[oa]s?|desprecio|prepotentes?|arrogantes?|déspotas?|despotas?|"
    r"hostiles?|agresiv[oa]s?|impresentables?|nefast[oa]s?|vergonzos[oa]s?|"
    r"asquer[oa]s[oa]s?|falta de respeto|malos modos|falta de educación|"
    r"gritos|humillante|mugre|mendigando|mendigar|"
    r"habla mal|hablan mal|trata mal|tratan mal|trato mal|"
    r"como si estuvieran|se siente[nr]? humillad|menospreci\w+|"
    r"pone[nr]? mala cara|de mala gana|mala cara)\b",
    re.IGNORECASE,
)

# Fragmentos entre comillas: rastro de resena copiada.
ENTRECOMILLADO = re.compile(r"[«\"\u201c]([^«\"»\u201c\u201d]{2,400})[»\"\u201d]")

# A partir de aqui una cita deja de ser un giro y pasa a ser una resena entera.
LIMITE_CITA = 60


# --------------------------------------------------------------------------
# Clasificacion
# --------------------------------------------------------------------------

def clasificar(frase: str) -> str:
    """Devuelve 'eliminar', 'descomillar' o 'conservar'."""
    if DELITO.search(frase) and not NEUTRO.search(frase):
        return "eliminar"

    # Juicio duro, recaiga o no sobre una persona nombrada.
    if JUICIO_DURO.search(frase):
        return "eliminar"

    citas = ENTRECOMILLADO.findall(frase)
    if citas:
        # Una cita larga es una resena reproducida: fuera la frase entera.
        if any(len(cita) > LIMITE_CITA for cita in citas):
            return "eliminar"
        return "descomillar"

    return "conservar"


def descomillar(frase: str) -> str:
    """Quita las comillas y deja las palabras integradas en la frase."""
    return ENTRECOMILLADO.sub(lambda m: m.group(1), frase)


def procesar_parrafo(parrafo: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()

    if parrafo.lstrip().startswith("##"):
        return parrafo, marcador

    conservadas = []
    for frase in re.split(r"(?<=[.!?])\s+", parrafo.strip()):
        if not frase.strip():
            continue
        accion = clasificar(frase)

        if accion == "eliminar":
            marcador["frases_eliminadas"] += 1
            continue
        if accion == "descomillar":
            frase = descomillar(frase)
            marcador["citas_integradas"] += 1
        conservadas.append(frase)

    texto = " ".join(conservadas).strip()

    # Un parrafo que queda en un resto muy corto pierde sentido: fuera entero.
    if conservadas and len(texto.split()) < 12:
        marcador["parrafos_eliminados"] += 1
        return "", marcador

    return texto, marcador


def procesar_cuerpo(cuerpo: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()
    salida = []

    for parrafo in cuerpo.split("\n\n"):
        nuevo, parcial = procesar_parrafo(parrafo)
        marcador.update(parcial)
        if nuevo.strip():
            salida.append(nuevo)

    # Un encabezado que se queda sin texto debajo se elimina tambien.
    limpio = []
    for indice, bloque in enumerate(salida):
        if bloque.lstrip().startswith("##"):
            siguiente = salida[indice + 1] if indice + 1 < len(salida) else ""
            if not siguiente or siguiente.lstrip().startswith("##"):
                marcador["encabezados_huerfanos"] += 1
                continue
        limpio.append(bloque)

    return "\n\n".join(limpio), marcador


# --------------------------------------------------------------------------

def procesar(directorio: Path, simular: bool) -> None:
    total: Counter = Counter()
    informe = []
    fichas_tocadas = 0

    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        modificado = False

        for ficha in fichas:
            cuerpo_nuevo, marcador = procesar_cuerpo(ficha["cuerpo"])
            resumen_nuevo, marcador_resumen = procesar_parrafo(ficha["resumen"])
            marcador.update(marcador_resumen)

            if not marcador:
                continue

            informe.append({
                "nombre": ficha["nombre"],
                "ciudad": ficha["ciudad"],
                "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                "palabrasAntes": len(ficha["cuerpo"].split()),
                "palabrasDespues": len(cuerpo_nuevo.split()),
                "cambios": dict(marcador),
            })

            if not simular:
                ficha["cuerpo"] = cuerpo_nuevo
                # Si el resumen se vacia, se recompone con la primera frase del
                # cuerpo, que ya esta saneada.
                ficha["resumen"] = resumen_nuevo.strip() or (
                    re.split(r"(?<=[.!?])\s+", cuerpo_nuevo)[0] if cuerpo_nuevo else ""
                )
                ficha["revisadoRiesgo"] = True
                modificado = True

            total.update(marcador)
            fichas_tocadas += 1

        if modificado and not simular:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )

    (directorio / "informe-riesgo.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("SIMULACION — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fichas afectadas: {fichas_tocadas}")
    for clave, valor in total.most_common():
        print(f"  {clave}: {valor}")

    if informe:
        perdida = [i["palabrasAntes"] - i["palabrasDespues"] for i in informe]
        print(f"\nPalabras eliminadas: media {sum(perdida)/len(perdida):.0f}, max {max(perdida)}")
        print(f"Fichas que bajan de 400 palabras: "
              f"{sum(1 for i in informe if i['palabrasDespues'] < 400)}")
    print(f"\nInforme en {directorio / 'informe-riesgo.json'}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
