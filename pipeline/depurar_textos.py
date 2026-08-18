#!/usr/bin/env python3
"""
Depura los textos editoriales. Sustituye a `despersonalizar.py`.

Cuatro niveles, todos por eliminacion de frase completa. Ninguno reescribe.

  A. ACUSACIONES GRAVES. Robo, acoso, racismo, amenazas, plagas, manipulacion
     de moviles robados, retencion de fondos. Un directorio no tiene por que
     arbitrar una acusacion penal porque alguien la escribiera en una resena.
     Las coletillas de "no verificado" o "de ser cierto" no protegen: la
     imputacion ya esta publicada y sigue siendo identificable el negocio.

  B. JUICIOS DUROS Y PERSONAS IDENTIFICABLES. Lo que ya cubria el script
     anterior: art. 7.7 de la LO 1/1982.

  C. ESPECULACION. "Es probable que cuente con fax", "al tratarse de un
     locutorio es posible que ofrezca...". Si no sabemos que tiene fax, hablar
     del fax no aporta. Añadir despues que no esta confirmado no arregla nada:
     el lector ya ha leido que hay fax.

  D. RELLENO DE ENTORNO. "De facil acceso", "trafico moderado", "a pocos
     minutos del centro". No procede de ningun dato calculado. En un directorio
     local vale mas menos texto y firme.

FALSOS POSITIVOS EVITADOS
-------------------------
El vocabulario se solapa con usos inocentes y hubo que acotarlo con casos
reales del propio corpus:

  - "el servicio mas demandado" no es una demanda judicial.
  - "prevenir el fraude", "normativa de blanqueo" son lenguaje regulatorio.
  - "las fricciones son menores" es un adjetivo, no un menor de edad.
  - "estafeta" es una oficina de correos.
  - "citas para extranjeria, policia, DNI" es un servicio del local.

Uso:  python3 depurar_textos.py ./data [--simular]
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------
# A. Acusaciones graves
# --------------------------------------------------------------------------

ACUSACION = re.compile(
    r"\b(acusaci[oó]n\w*|acusan?\b|acusad[oa]s?|denunci\w+|"
    r"rob[oa]s?\b|robad[oa]s?|hurto\w*|sustra[ií]d\w+|"
    r"acoso|acosad\w+|abus[oa]s?\b|abusad\w+|pederast\w+|"
    r"racis\w+|xen[oó]fob\w+|homof[oó]b\w+|"
    r"amenaz\w+|agresi[oó]n\w*|agredi\w+|violen\w+|"
    r"retenci[oó]n de fondos|reten\w+ el dinero|dinero B|billete falso|"
    r"chinches|[aá]caros|plagas?\b|insalubr\w+|"
    r"ilegal\w*|delit\w+|estafa\w*|estaf[oó]\b|fraude\w*|cobros indebidos|"
    r"piezas? (originales|falsas)|pr[aá]cticas poco honestas)\b",
    re.IGNORECASE,
)

# Contextos que desactivan la deteccion: normativa del sector y servicios
# administrativos que el propio local ofrece.
CONTEXTO_NEUTRO = re.compile(
    r"\b(prevenir|prevenci[oó]n|evitar|antifraude|normativ\w+|cumplimiento|"
    r"verificaci[oó]n|blanqueo|regulaci\w+|contra el|contra la|frente al?|"
    r"protecci[oó]n|seguridad|identificaci[oó]n|obligatori\w+|requisit\w+|"
    r"cita[s]? (para|de|relacionad)|extranjer[ií]a|estafeta)\b",
    re.IGNORECASE,
)

# "menores" solo cuenta como personas cuando lo introduce una preposicion.
MENORES_PERSONAS = re.compile(
    r"\b(hacia|contra|a|con|de|sobre) (los |las )?menores\b", re.IGNORECASE
)

# --------------------------------------------------------------------------
# B. Juicios duros sobre personas
# --------------------------------------------------------------------------

JUICIO_DURO = re.compile(
    r"\b(antipátic[oa]s?|maleducad[oa]s?|groser[oa]s?|bordes?|"
    r"despectiv[oa]s?|desprecio|prepotentes?|arrogantes?|déspotas?|despotas?|"
    r"hostiles?|impresentables?|nefast[oa]s?|vergonzos[oa]s?|"
    r"asquer[oa]s[oa]s?|falta de respeto|malos modos|falta de educación|"
    r"gritos|humillante|mugre|mendigando|mendigar|"
    r"habla mal|hablan mal|trata mal|tratan mal|"
    r"como si estuvieran|menospreci\w+|mala cara|de mala gana)\b",
    re.IGNORECASE,
)

# --------------------------------------------------------------------------
# C. Especulacion
# --------------------------------------------------------------------------

ESPECULACION = re.compile(
    r"\b(es probable que|probablemente|es posible que|posiblemente|"
    r"cabe (suponer|pensar|imaginar|esperar)|todo (apunta|indica) a|"
    r"es de suponer|presumiblemente|se puede intuir|"
    r"hay indicios de que|al tratarse de|por el tipo de (local|negocio|establecimiento)|"
    r"dado que se trata|podr[ií]a (contar|disponer|ofrecer|tener|incluir)|"
    r"sugiere que (el|la|podr)|"
    r"es com[uú]n que|es habitual que|suelen? (ofrecer|disponer|contar|incluir|tener)|"
    r"no se especifican|no se detallan|no consta|aunque no (se sabe|se conoce|hay constancia)|"
    r"lo habitual en este tipo|como en (cualquier|todo) locutorio|"
    r"cabe esperar|lo que cabe esperar|en (l[ií]neas|t[eé]rminos) generales)\b",
    re.IGNORECASE,
)

# Inferencia a partir del rotulo. Es la especulacion mas insidiosa porque
# suena razonada: "su nombre sugiere que podria ofrecer telefonia". Deducir
# servicios del letrero no es informacion, y ademas el texto suele reconocerlo
# a continuacion ("aunque no hay confirmacion"), lo que confirma que sobra.
INFERENCIA_DEL_NOMBRE = re.compile(
    r"\b(el|su|cuyo|cuya|propio|propia|la|las|los)?\s*"
    r"(nombre|denominaci[oó]n|r[oó]tulo|etiqueta|categor[ií]a|t[eé]rmino)s?\b"
    r"[^.]{0,80}\b(sugiere[n]?|apunta[n]?|indica[n]?|implica[n]?|evoca[n]?|"
    r"remite[n]?|hace[n]? pensar)\b",
    re.IGNORECASE,
)

# "posibilidades no verificadas" y similares anuncian que lo dicho no consta.
CAUTELA_VACIA = re.compile(
    r"\b(posibilidades no verificadas|no se puede afirmar con certeza|"
    r"de ser ciert[oa]|si esto fuera ciert[oa]|"
    r"aunque no (podemos|se puede) confirmar)\b",
    re.IGNORECASE,
)

# --------------------------------------------------------------------------
# D. Relleno de entorno
# --------------------------------------------------------------------------

RELLENO_ENTORNO = re.compile(
    r"\b(f[aá]cil acceso|bien comunicad\w+|tr[aá]fico moderado|"
    r"a pocos minutos (a pie|caminando|del centro)|caminando en pocos minutos|"
    r"zona (c[eé]ntrica|tranquila|animada|de paso)|"
    r"ambiente (tranquilo|animado|acogedor)|entorno (agradable|tranquilo|urbano)|"
    r"aparcar (con facilidad|sin problema)|"
    r"en pleno coraz[oó]n|punto neur[aá]lgico|arteria principal)\b",
    re.IGNORECASE,
)

# Rastro de resena copiada.
ENTRECOMILLADO = re.compile(r"[«\"\u201c]([^«\"»\u201c\u201d]{2,400})[»\"\u201d]")
LIMITE_CITA = 60


def clasificar(frase: str) -> str:
    neutro = bool(CONTEXTO_NEUTRO.search(frase))

    if not neutro and (ACUSACION.search(frase) or MENORES_PERSONAS.search(frase)):
        return "acusacion"

    if JUICIO_DURO.search(frase):
        return "juicio"

    if (ESPECULACION.search(frase) or INFERENCIA_DEL_NOMBRE.search(frase)
            or CAUTELA_VACIA.search(frase)):
        return "especulacion"

    if RELLENO_ENTORNO.search(frase):
        return "relleno"

    citas = ENTRECOMILLADO.findall(frase)
    if citas:
        if any(len(cita) > LIMITE_CITA for cita in citas):
            return "cita_larga"
        return "descomillar"

    return "conservar"


def descomillar(frase: str) -> str:
    return ENTRECOMILLADO.sub(lambda m: m.group(1), frase)


ELIMINAR = {"acusacion", "juicio", "especulacion", "relleno", "cita_larga"}


def procesar_parrafo(parrafo: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()
    limpio = parrafo.lstrip()
    if limpio.startswith("##"):
        # A veces el encabezado llega pegado a su primer parrafo. Se separa
        # para que ese texto pase igualmente por el filtro.
        partes = limpio.split("\n", 1)
        if len(partes) == 2 and partes[1].strip():
            cuerpo, parcial = procesar_parrafo(partes[1].strip())
            marcador.update(parcial)
            return (f"{partes[0]}\n\n{cuerpo}" if cuerpo else ""), marcador
        return parrafo, marcador

    conservadas = []
    for frase in re.split(r"(?<=[.!?])\s+", parrafo.strip()):
        if not frase.strip():
            continue
        accion = clasificar(frase)
        if accion in ELIMINAR:
            marcador[accion] += 1
            continue
        if accion == "descomillar":
            frase = descomillar(frase)
            marcador["citas_integradas"] += 1
        conservadas.append(frase)

    texto = " ".join(conservadas).strip()
    if conservadas and len(texto.split()) < 12:
        marcador["parrafos_eliminados"] += 1
        return "", marcador
    return texto, marcador


# Un encabezado tambien puede ser especulativo: "Que servicios podria ofrecer
# un locutorio como este?" anuncia justamente el relleno que se quiere evitar.
# En ese caso cae el encabezado y con el la seccion que introduce.
ENCABEZADO_ESPECULATIVO = re.compile(
    r"^##\s.*\b(podr[ií]a|podr[ií]an|cabe esperar|qu[eé] esperar|"
    r"suele|suelen|posible|probable|matices|"
    r"ambiente (acogedor|tranquilo|agradable)|bien comunicad\w+|"
    r"f[aá]cil acceso|zona (c[eé]ntrica|tranquila))\b",
    re.IGNORECASE,
)


def procesar_cuerpo(cuerpo: str) -> tuple[str, Counter]:
    marcador: Counter = Counter()
    bloques = []
    saltar_seccion = False

    for parrafo in cuerpo.split("\n\n"):
        es_encabezado = parrafo.lstrip().startswith("##")

        if es_encabezado:
            if ENCABEZADO_ESPECULATIVO.match(parrafo.strip()):
                marcador["secciones_especulativas"] += 1
                saltar_seccion = True
                continue
            saltar_seccion = False
        elif saltar_seccion:
            marcador["parrafos_de_seccion_especulativa"] += 1
            continue

        nuevo, parcial = procesar_parrafo(parrafo)
        marcador.update(parcial)
        if nuevo.strip():
            bloques.append(nuevo)

    limpio = []
    for indice, bloque in enumerate(bloques):
        if bloque.lstrip().startswith("##"):
            siguiente = bloques[indice + 1] if indice + 1 < len(bloques) else ""
            if not siguiente or siguiente.lstrip().startswith("##"):
                marcador["encabezados_huerfanos"] += 1
                continue
        limpio.append(bloque)

    return "\n\n".join(limpio), marcador


def procesar(directorio: Path, simular: bool) -> None:
    total: Counter = Counter()
    informe = []
    tocadas = 0

    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        modificado = False

        for ficha in fichas:
            cuerpo, marcador = procesar_cuerpo(ficha["cuerpo"])
            resumen, marcador_resumen = procesar_parrafo(ficha["resumen"])
            marcador.update(marcador_resumen)
            if not marcador:
                continue

            informe.append({
                "nombre": ficha["nombre"],
                "ciudad": ficha["ciudad"],
                "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                "palabrasAntes": len(ficha["cuerpo"].split()),
                "palabrasDespues": len(cuerpo.split()),
                "cambios": dict(marcador),
            })

            if not simular:
                ficha["cuerpo"] = cuerpo
                ficha["resumen"] = resumen.strip() or (
                    re.split(r"(?<=[.!?])\s+", cuerpo)[0] if cuerpo else ""
                )
                ficha["depurado"] = True
                modificado = True

            total.update(marcador)
            tocadas += 1

        if modificado and not simular:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )

    (directorio / "informe-depuracion.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("SIMULACION — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fichas afectadas: {tocadas}")
    for clave, valor in total.most_common():
        print(f"  {clave}: {valor}")

    if informe:
        perdida = [i["palabrasAntes"] - i["palabrasDespues"] for i in informe]
        cortas = [i for i in informe if i["palabrasDespues"] < 300]
        print(f"\nPalabras eliminadas: media {sum(perdida) / len(perdida):.0f}, "
              f"máx {max(perdida)}")
        print(f"Fichas por debajo de 300 palabras: {len(cortas)}")
        for i in sorted(cortas, key=lambda x: x["palabrasDespues"])[:5]:
            print(f"  {i['palabrasDespues']:4d} palabras · {i['url']}")
    print(f"\nInforme en {directorio / 'informe-depuracion.json'}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
