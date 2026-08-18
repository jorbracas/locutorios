#!/usr/bin/env python3
"""
Amplia las fichas que quedaron cortas tras la limpieza.

REGLA UNICA
-----------
Solo se escribe a partir de datos que ya estan en la ficha: categoria,
direccion, telefono, web, atributos declarados, tipo de establecimiento y, con
mucha prudencia, actividad observada. Nada de suponer servicios, horarios,
comisiones ni caracteristicas del entorno.

Lo que si esta permitido es explicar PARA QUE sirve un servicio confirmado.
Decir que la impresion resuelve tramites que aun piden copia fisica no
atribuye nada nuevo al negocio: describe el servicio, que ya consta.

QUE NO HACE
-----------
  - No toca las fichas que ya llegan a 500 palabras.
  - No reescribe lo existente: solo anade secciones que falten.
  - No rellena con opiniones de clientes para ganar longitud.
  - No repite el mismo consejo en cuatro parrafos: cada bloque aporta algo
    distinto y las formulaciones rotan segun la ficha.
  - No fuerza las 500 palabras. Si un establecimiento tiene pocos datos, se
    queda corto antes que inventar.

Uso:  python3 ampliar_fichas.py ./data [--simular] [--objetivo 520]
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

OBJETIVO = 520
MINIMO = 500


def variante(opciones: list[str], semilla: str) -> str:
    """Elige de forma estable pero repartida, para no repetir la misma frase."""
    valor = 0
    for caracter in semilla:
        valor = (valor * 31 + ord(caracter)) & 0xFFFFFFFF
    return opciones[valor % len(opciones)]


def encabezados(cuerpo: str) -> set[str]:
    return {h.strip().lower() for h in re.findall(r"(?m)^##\s*(.+)$", cuerpo)}


def tiene(cuerpo: str, *claves: str) -> bool:
    texto = cuerpo.lower()
    return any(clave in texto for clave in claves)


# --------------------------------------------------------------------------
# Servicios confirmados
# --------------------------------------------------------------------------

def servicios_confirmados(ficha: dict) -> list[str]:
    """Lee servicios de la categoria y de los atributos. Nunca los deduce."""
    fuentes = " ".join([
        ficha.get("categoria", ""),
        " ".join(ficha.get("categorias", []) or []),
    ]).lower()

    encontrados = []
    mapa = [
        ("envio", ["transferencia", "envío de dinero", "envio de dinero", "money", "remesa", "giro"]),
        # "envios" queda fuera a proposito: en este sector suele referirse a
        # envio de dinero, no a paqueteria.
        ("paqueteria", ["paquete", "mensajer", "logística", "logistica"]),
        ("impresion", ["copister", "imprenta", "fotocopia", "impresión", "impresion", "papeler"]),
        # "locutorio" NO implica puestos de internet: es el nombre generico del
        # tipo de negocio y deducir de el un servicio concreto es especular.
        ("internet", ["cibercafé", "cibercafe", "internet"]),
        ("telefonia", ["telefon", "móvil", "movil", "teléfono", "sim"]),
        ("reparacion", ["reparación", "reparacion", "servicio técnico", "servicio tecnico"]),
        ("alimentacion", ["alimentación", "alimentacion", "supermercado", "tienda de alimentación"]),
        ("divisa", ["cambio de divisa", "casa de cambio"]),
    ]
    for clave, marcas in mapa:
        if any(marca in fuentes for marca in marcas):
            encontrados.append(clave)
    return encontrados


EXPLICACION_SERVICIO = {
    "envio": [
        "El envío de dinero al extranjero es el servicio que más ha crecido en este tipo de "
        "establecimientos. Antes de acudir conviene tener claro el importe, el país de destino y "
        "la documentación de identidad, porque la comisión y el tipo de cambio varían según el "
        "operador y el corredor concreto.",
        "Para tramitar una remesa hace falta un documento de identidad en vigor y los datos "
        "completos del destinatario. La comisión no es uniforme: depende del operador, del país "
        "al que se envía y de si el pago se hace en efectivo o con tarjeta, así que preguntar el "
        "importe final antes de cerrar la operación evita sorpresas.",
    ],
    "paqueteria": [
        "Como punto de paquetería, permite recoger y entregar envíos sin depender del horario de "
        "una oficina de reparto. Conviene llevar el código o el aviso de entrega y un documento "
        "de identidad, y confirmar el plazo durante el que guardan el paquete antes de devolverlo.",
        "El servicio de paquetería resulta práctico para quien no puede recibir envíos en casa "
        "durante la jornada laboral. Cada operador logístico tiene sus propias condiciones de "
        "recogida y sus plazos de custodia, que merece la pena consultar al dejar o retirar un envío.",
    ],
    "impresion": [
        "El servicio de impresión y fotocopias sigue siendo necesario para trámites que aún exigen "
        "copia física: formularios de la administración, justificantes, contratos o billetes. "
        "Suele admitirse el archivo en memoria USB o enviado por correo electrónico.",
        "Imprimir, escanear o fotocopiar continúa haciendo falta para gestiones administrativas, "
        "matrículas o documentación laboral. Preguntar por el precio por página y por si admiten "
        "color evita malentendidos, sobre todo en trabajos de varias hojas.",
    ],
    "internet": [
        "Los puestos de acceso a internet cubren un hueco real para quien no dispone de ordenador "
        "en casa o necesita completar una gestión concreta: una cita previa, una solicitud "
        "telemática o la descarga de un documento oficial.",
        "El acceso a internet por horas resulta útil para trámites que no se resuelven bien desde "
        "el móvil, como rellenar formularios largos, adjuntar documentación escaneada o gestionar "
        "citas con la administración.",
    ],
    "telefonia": [
        "Las recargas de móvil y la venta de tarjetas SIM prepago son habituales en este tipo de "
        "local. Para quien llama con frecuencia al extranjero, comparar tarifas entre operadores "
        "antes de contratar suele marcar una diferencia apreciable.",
        "La venta de tarjetas SIM y las recargas de saldo permiten mantener línea sin contrato ni "
        "permanencia, algo práctico para estancias temporales o para quien prefiere controlar el "
        "gasto mes a mes.",
    ],
    "reparacion": [
        "El servicio de reparación de terminales cubre averías corrientes como pantallas, baterías "
        "o conectores de carga. Conviene pedir presupuesto previo y preguntar por la garantía de "
        "la reparación y por el origen de las piezas.",
    ],
    "alimentacion": [
        "La combinación de alimentación con servicios de locutorio es frecuente en los comercios "
        "de barrio, y permite resolver varias gestiones en un mismo desplazamiento.",
    ],
    "divisa": [
        "El cambio de divisa exige comprobar el tipo aplicado y si existe comisión añadida, porque "
        "la diferencia entre establecimientos puede ser notable en importes altos.",
    ],
}


# --------------------------------------------------------------------------
# Bloques
# --------------------------------------------------------------------------

def bloque_servicios(ficha: dict) -> str:
    servicios = servicios_confirmados(ficha)
    if not servicios:
        return ""

    parrafos = []
    for clave in servicios[:3]:
        opciones = EXPLICACION_SERVICIO.get(clave)
        if opciones:
            parrafos.append(variante(opciones, ficha["id"] + clave))

    if not parrafos:
        return ""
    return "## Servicios disponibles\n\n" + "\n\n".join(parrafos)


ETIQUETA_ATRIBUTO = {
    "Pagos": "las formas de pago admitidas",
    "Accesibilidad": "las condiciones de accesibilidad",
    "Opciones de servicio": "las modalidades de servicio",
    "Servicios": "los servicios complementarios",
    "Planificación": "la organización de la visita",
}


def bloque_practico(ficha: dict) -> str:
    frases = []

    calle = ficha.get("calle") or ""
    if calle:
        frases.append(
            f"El establecimiento se encuentra en {calle}, en "
            f"{ficha['ciudad']} ({ficha['provincia']})"
            + (f", código postal {ficha['codigoPostal']}." if ficha.get("codigoPostal") else ".")
        )

    if ficha.get("telefono"):
        frases.append(
            "Tiene teléfono publicado, lo que permite confirmar por adelantado si el "
            "servicio concreto que se necesita está disponible ese día."
        )

    if ficha.get("web"):
        frases.append("También dispone de página web propia con información adicional.")

    for grupo in ficha.get("atributos", [])[:3]:
        etiqueta = ETIQUETA_ATRIBUTO.get(grupo["grupo"], grupo["grupo"].lower())
        valores = ", ".join(v.lower() for v in grupo["valores"][:4])
        frases.append(f"Entre {etiqueta} constan: {valores}.")

    if len(frases) < 2:
        return ""
    return "## Información práctica\n\n" + " ".join(frases)


def bloque_antes_de_acudir(ficha: dict) -> str:
    servicios = servicios_confirmados(ficha)
    consejos = []

    if "envio" in servicios:
        consejos.append(
            "llevar el documento de identidad y los datos completos del destinatario, "
            "y preguntar la comisión aplicable al país de destino"
        )
    if "paqueteria" in servicios:
        consejos.append(
            "tener a mano el código de recogida y comprobar cuántos días guardan el envío"
        )
    if "impresion" in servicios:
        consejos.append("consultar el precio por página y si admiten impresión en color")
    if "telefonia" in servicios:
        consejos.append("comparar las tarifas de recarga antes de decidir operador")

    if not consejos:
        return ""

    actividad = ficha.get("actividad")
    cierre = ""
    if actividad:
        # La actividad observada no es un horario: se formula como tal.
        cierre = (
            " Esta ficha incluye además un registro de actividad observada, que da una idea "
            "aproximada de las franjas con más movimiento, aunque no sustituye al horario "
            "oficial del local."
        )

    apertura = variante([
        "Antes de desplazarse, conviene",
        "Para no hacer el viaje en balde, merece la pena",
        "Antes de acudir resulta útil",
    ], ficha["id"])

    return (
        "## Qué tener en cuenta antes de acudir\n\n"
        f"{apertura} {', '.join(consejos[:-1])}"
        + (f" y {consejos[-1]}." if len(consejos) > 1 else f"{consejos[0]}.")
        + " Los horarios de estos negocios cambian con frecuencia y no siempre se reflejan "
        "en internet, así que una llamada previa sigue siendo la forma más fiable de "
        "confirmarlos." + cierre
    )


def ampliar(ficha: dict, objetivo: int) -> tuple[str, Counter]:
    marcador: Counter = Counter()
    cuerpo = ficha["cuerpo"]
    if len(cuerpo.split()) >= MINIMO:
        return cuerpo, marcador

    titulos = encabezados(cuerpo)
    añadidos = []

    candidatos = [
        ("servicios disponibles", bloque_servicios, ("servicio", "ofrece")),
        ("información práctica", bloque_practico, ("se encuentra en", "código postal")),
        ("qué tener en cuenta antes de acudir", bloque_antes_de_acudir, ("antes de acudir",)),
    ]

    for titulo, constructor, marcas in candidatos:
        if len(cuerpo.split()) + sum(len(a.split()) for a in añadidos) >= objetivo:
            break
        if titulo in titulos:
            continue
        bloque = constructor(ficha)
        if not bloque:
            continue
        # No se repite contenido que ya estuviera expresado de otra forma.
        cuerpo_bajo = cuerpo.lower()
        if marcas and all(m in cuerpo_bajo for m in marcas):
            continue
        añadidos.append(bloque)
        marcador[f"bloque_{titulo.split()[0]}"] += 1

    if not añadidos:
        return cuerpo, marcador

    marcador["fichas_ampliadas"] += 1
    return cuerpo.rstrip() + "\n\n" + "\n\n".join(añadidos), marcador


def procesar(directorio: Path, simular: bool, objetivo: int) -> None:
    total: Counter = Counter()
    antes_cortas = 0
    despues_cortas = 0
    sin_datos: list[dict] = []

    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        modificado = False

        for ficha in fichas:
            palabras_antes = len(ficha["cuerpo"].split())
            if palabras_antes < MINIMO:
                antes_cortas += 1

            nuevo, marcador = ampliar(ficha, objetivo)
            total.update(marcador)

            if marcador and not simular:
                ficha["cuerpo"] = nuevo
                modificado = True

            palabras_despues = len(nuevo.split())
            if palabras_despues < MINIMO:
                despues_cortas += 1
                if palabras_antes < MINIMO:
                    sin_datos.append({
                        "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                        "nombre": ficha["nombre"],
                        "palabras": palabras_despues,
                        "categoria": ficha.get("categoria", ""),
                        "atributos": len(ficha.get("atributos", [])),
                    })

        if modificado and not simular:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )

    sin_datos.sort(key=lambda x: x["palabras"])
    (directorio / "informe-ampliacion.json").write_text(
        json.dumps({
            "cortasAntes": antes_cortas,
            "cortasDespues": despues_cortas,
            "recuentos": dict(total),
            "siguenCortas": sin_datos,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("SIMULACIÓN — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fichas por debajo de {MINIMO} palabras antes: {antes_cortas}")
    print(f"Fichas ampliadas: {total['fichas_ampliadas']}")
    print(f"Siguen por debajo de {MINIMO}: {despues_cortas}")
    for clave, valor in total.most_common():
        print(f"  {clave}: {valor}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datos", type=Path)
    parser.add_argument("--simular", action="store_true")
    parser.add_argument("--objetivo", type=int, default=OBJETIVO)
    args = parser.parse_args()
    procesar(args.datos, args.simular, args.objetivo)
