#!/usr/bin/env python3
"""Genera textos de localidad reproducibles a partir de datos agregados.

El generador no llama a un modelo y no añade conocimiento externo. Cada frase
sale de ``agregados-ciudad.json`` o explica cómo deben interpretarse esos datos.
Esto evita que una regeneración introduzca barrios, horarios, causas o servicios
que no constan en el proyecto.

Solo se redactan localidades con cinco o más establecimientos. Las demás ya
tienen el resumen numérico, el mapa, las preguntas y el listado de negocios; un
párrafo largo con tan pocos datos sería relleno.

Uso:
    python3 pipeline/escribir_textos_ciudad.py ./data
    python3 pipeline/escribir_textos_ciudad.py ./data --minimo 5
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


MINIMO_POR_DEFECTO = 5
MIN_PALABRAS = 180
MAX_PALABRAS = 240


def elegir(clave: str, grupo: str, opciones: list[str]) -> str:
    """Elige una variante de forma estable para una localidad."""
    digest = hashlib.sha256(f"{clave}:{grupo}".encode("utf-8")).digest()
    return opciones[int.from_bytes(digest[:4], "big") % len(opciones)]


def contar_palabras(texto: str) -> int:
    limpio = re.sub(r"^#{1,6}\s+", "", texto, flags=re.MULTILINE)
    return len(re.findall(r"\S+", limpio))


def enumerar(partes: list[str]) -> str:
    partes = [parte for parte in partes if parte]
    if len(partes) == 1:
        return partes[0]
    if len(partes) == 2:
        return f"{partes[0]} y {partes[1]}"
    return f"{', '.join(partes[:-1])} y {partes[-1]}"


def desglose_tipos(tipos: dict[str, int]) -> str:
    partes = []
    if tipos["locutorio"]:
        n = tipos["locutorio"]
        partes.append(f"{n} {'locutorio' if n == 1 else 'locutorios'}")
    if tipos["envio"]:
        n = tipos["envio"]
        partes.append(
            f"{n} {'punto especializado' if n == 1 else 'puntos especializados'} "
            "en envío de dinero"
        )
    if tipos["otros"]:
        n = tipos["otros"]
        partes.append(
            f"{n} {'comercio con servicios relacionados' if n == 1 else 'comercios con servicios relacionados'}"
        )
    return enumerar(partes)


def medias_atributos(agregados: dict[str, dict]) -> dict[str, float]:
    sumas: dict[str, int] = {}
    muestras: dict[str, int] = {}
    for agregado in agregados.values():
        for atributo in agregado.get("atributos", []):
            if atributo["total"] < 5:
                continue
            valor = atributo["valor"]
            sumas[valor] = sumas.get(valor, 0) + atributo["cantidad"]
            muestras[valor] = muestras.get(valor, 0) + atributo["total"]
    return {
        valor: sumas[valor] / muestras[valor]
        for valor in sumas
        if muestras[valor] >= 30
    }


def atributo_distintivo(agregado: dict, medias: dict[str, float]) -> dict | None:
    candidatos = []
    for atributo in agregado.get("atributos", []):
        media = medias.get(atributo["valor"])
        if media is None or atributo["total"] < 5:
            continue
        proporcion = atributo["cantidad"] / atributo["total"]
        candidatos.append((abs(proporcion - media), atributo))
    return max(candidatos, default=(0, None), key=lambda par: par[0])[1]


def frase_telefono(agregado: dict, clave: str) -> str:
    telefono = agregado["conTelefono"]
    total = agregado["total"]
    if telefono == 0:
        return (
            "No consta un teléfono publicado en estos registros, por lo que la "
            "disponibilidad de cada servicio debe comprobarse por otra vía."
        )
    opciones = [
        f"El teléfono figura publicado en {telefono} de los {total} establecimientos, lo que permite consultar el servicio antes de desplazarse.",
        f"Hay un número de contacto publicado para {telefono} de los {total} locales; puede utilizarse para confirmar cada trámite antes de ir.",
        f"De los {total} establecimientos, {telefono} muestran teléfono de contacto para verificar directamente el servicio buscado.",
        f"El directorio dispone de teléfono para {telefono} de los {total} negocios, aunque cada establecimiento debe confirmar sus servicios y horarios.",
    ]
    return elegir(clave, "telefono", opciones)


def parrafo_inicial(nombre: str, agregado: dict, clave: str) -> str:
    total = agregado["total"]
    codigos = len(agregado["codigosPostales"])
    reparto = desglose_tipos(agregado["tipos"])
    telefono = frase_telefono(agregado, clave)
    opciones = [
        (
            f"En {nombre} hay {total} establecimientos clasificados como locutorios o puntos de envío de dinero, "
            f"repartidos por {codigos} {'código postal' if codigos == 1 else 'códigos postales'}. "
            f"El reparto exacto es de {reparto}. {telefono}"
        ),
        (
            f"La oferta de locutorios en {nombre} reúne {total} establecimientos y alcanza "
            f"{codigos} {'código postal' if codigos == 1 else 'códigos postales'}. "
            f"Dentro de ese total aparecen {reparto}. {telefono}"
        ),
        (
            f"Quien busque locutorios en {nombre} puede comparar {total} establecimientos distribuidos en "
            f"{codigos} {'código postal' if codigos == 1 else 'códigos postales'}. "
            f"La clasificación distingue {reparto}. {telefono}"
        ),
        (
            f"{nombre} suma {total} establecimientos relacionados con locutorios y envío de dinero en "
            f"{codigos} {'código postal' if codigos == 1 else 'códigos postales'}. "
            f"La composición del listado es {reparto}. {telefono}"
        ),
    ]
    return elegir(clave, "inicio", opciones)


def parrafo_actividad(nombre: str, agregado: dict, clave: str) -> str:
    actividad = agregado.get("actividad")
    if not actividad:
        opciones = [
            (
                "No se publica una muestra suficiente de afluencia para señalar horas de mayor o menor movimiento. "
                "Por ese motivo no se atribuyen franjas de apertura ni se deduce actividad dominical: el horario debe confirmarse directamente con cada local."
            ),
            (
                "No hay una serie de afluencia suficiente para comparar tramos del día ni describir el domingo. Cualquier horario concreto debe proceder del propio establecimiento y no puede deducirse de la categoría del negocio."
            ),
            (
                "No se ofrece una franja agregada de afluencia para esta localidad. Sin esa referencia no es posible proponer una hora conveniente ni deducir horarios; la presencia de un negocio en el listado no confirma su apertura."
            ),
        ]
        return elegir(clave, "sin-actividad", opciones)

    muestra = actividad["muestra"]
    punta = actividad["franjaPunta"]
    tranquila = actividad["franjaTranquila"]
    domingo = actividad["abrenDomingo"]
    mediodia = actividad["cierreMediodia"]

    domingo_frase = (
        f"El domingo presenta actividad en {domingo} de esos {muestra} establecimientos."
        if domingo
        else f"En la muestra de {muestra} establecimientos no aparece actividad registrada en domingo."
    )
    mediodia_frase = (
        f"En {mediodia} de los {muestra} también se aprecia una caída al mediodía compatible con una pausa."
        if mediodia
        else "La serie agregada no muestra una caída de actividad al mediodía."
    )
    opciones = [
        (
            f"La muestra de afluencia cubre {muestra} establecimientos. En ese grupo, el tramo con más movimiento va de {punta}, "
            f"mientras que el más tranquilo es de {tranquila}. {domingo_frase} {mediodia_frase} "
            "Son observaciones de movimiento, no horarios oficiales ni una prueba de apertura."
        ),
        (
            f"Los datos de actividad disponibles proceden de {muestra} locales: la mayor afluencia se concentra de {punta} y la menor de {tranquila}. "
            f"{domingo_frase} {mediodia_frase} No es un horario: una franja sin movimiento tampoco demuestra la apertura del establecimiento."
        ),
        (
            f"Entre los {muestra} establecimientos con información de afluencia, {punta} es la franja de mayor movimiento y {tranquila} la más calmada. "
            f"{domingo_frase} {mediodia_frase} Estas estimaciones sirven para comparar actividad, pero deben separarse del horario declarado por cada negocio."
        ),
        (
            f"La lectura horaria se limita a una muestra de {muestra} locales. El pico agregado aparece de {punta} y el tramo con menos movimiento de {tranquila}. "
            f"{domingo_frase} {mediodia_frase} El resultado describe afluencia observada y no permite deducir el horario de apertura."
        ),
    ]
    return elegir(clave, "actividad", opciones)


def parrafo_servicios(nombre: str, clave: str) -> str:
    opciones = [
        (
            "Los locutorios ya no son solo cabinas de llamadas: el listado distingue locutorios, puntos de envío de dinero y comercios relacionados. "
            "Las recargas de móvil y la papelería deben confirmarse en cada establecimiento, pues la categoría no garantiza esos servicios."
        ),
        (
            "La palabra locutorio conserva el nombre de las cabinas de llamadas, aunque hoy incluye perfiles distintos. El listado separa los puntos de envío de dinero del resto. "
            "Para recargas de móvil, impresión o papelería, hay que consultar al negocio concreto."
        ),
        (
            "Los locutorios actuales no funcionan únicamente como cabinas para llamar. La clasificación separa los establecimientos generales, los dedicados al envío de dinero y otros comercios relacionados. "
            "Las recargas de móvil, las fotocopias y la papelería se verifican individualmente."
        ),
        (
            "En general, aunque el nombre procede de las cabinas de llamadas, el sector incluye locutorios, puntos especializados en enviar dinero y comercios relacionados. "
            "La disponibilidad de recargas de móvil, impresión o papelería cambia entre establecimientos y debe confirmarse."
        ),
    ]
    return elegir(clave, "servicios", opciones)


def parrafo_atributo(agregado: dict, atributo: dict | None, clave: str) -> str:
    if not atributo:
        return "No se añade una comparación de atributos porque la muestra disponible no permite destacar uno con suficiente base."
    cantidad = atributo["cantidad"]
    total = atributo["total"]
    valor = atributo["valor"].lower()
    opciones = [
        f"Entre los atributos publicados, {valor} consta en {cantidad} de {total} establecimientos; su ausencia en los demás no permite descartarlo.",
        f"Como referencia, {cantidad} de {total} establecimientos tienen publicado «{valor}»; en el resto no puede suponerse ni su presencia ni su ausencia.",
        f"Como dato adicional, «{valor}» aparece publicado en {cantidad} de {total} establecimientos; en los demás no puede descartarse.",
        f"En {cantidad} de {total} establecimientos figura «{valor}»; que no aparezca en los demás no demuestra que la característica falte.",
    ]
    return elegir(clave, "atributo", opciones)


def parrafo_vecinas(agregado: dict, clave: str) -> str:
    vecinas = agregado.get("vecinas", [])[:2]
    if not vecinas:
        return "No se muestra una alternativa cercana con oferta comparable; para ampliar el radio puede consultarse el índice de la provincia."

    partes = []
    for vecina in vecinas:
        distancia = str(vecina["distancia"]).replace(".", ",")
        total = vecina["total"]
        partes.append(
            f"{vecina['nombre']}, a {distancia} km, con {total} "
            f"{'establecimiento' if total == 1 else 'establecimientos'}"
        )
    lista = enumerar(partes)
    opciones = [
        f"Para ampliar la búsqueda, aparecen como alternativas {lista}.",
        f"El radio puede extenderse a {lista}, comparando antes el servicio concreto.",
        f"Entre las localidades cercanas con oferta figuran {lista}.",
        f"Como referencias próximas aparecen {lista}; sirven para ampliar opciones.",
    ]
    return elegir(clave, "vecinas", opciones)


def redactar(nombre: str, agregado: dict, clave: str, medias: dict[str, float]) -> str:
    if agregado.get("actividad"):
        encabezados = [
            f"## Cómo interpretar la oferta de {nombre}",
            f"## Afluencia y servicios en {nombre}",
            f"## Datos prácticos de los locutorios de {nombre}",
            f"## Qué conviene comprobar en {nombre}",
            f"## Movimiento observado en {nombre}",
        ]
    else:
        encabezados = [
            f"## Cómo interpretar la oferta de {nombre}",
            f"## Servicios que conviene confirmar en {nombre}",
            f"## Datos prácticos de los locutorios de {nombre}",
            f"## Qué conviene comprobar en {nombre}",
        ]
    atributo = atributo_distintivo(agregado, medias)
    parrafos = [
        parrafo_inicial(nombre, agregado, clave),
        parrafo_actividad(nombre, agregado, clave),
        elegir(clave, "encabezado", encabezados),
        parrafo_servicios(nombre, clave),
        " ".join(
            [
                parrafo_atributo(agregado, atributo, clave),
                parrafo_vecinas(agregado, clave),
            ]
        ),
    ]
    texto = "\n\n".join(parrafos)

    # La base suele quedar dentro del rango. Esta frase solo completa los casos
    # con nombres y datos excepcionalmente cortos; no introduce hechos nuevos.
    if contar_palabras(texto) < MIN_PALABRAS:
        texto += (
            " La dirección y el teléfono publicados permiten comparar opciones sin "
            "dar por hecho que dos establecimientos de la misma categoría ofrecen exactamente lo mismo."
        )

    palabras = contar_palabras(texto)
    if not MIN_PALABRAS <= palabras <= MAX_PALABRAS:
        raise ValueError(
            f"{clave}: {palabras} palabras; se esperaban {MIN_PALABRAS}-{MAX_PALABRAS}"
        )
    return texto


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datos", type=Path)
    parser.add_argument("--minimo", type=int, default=MINIMO_POR_DEFECTO)
    parser.add_argument("--salida", type=Path)
    args = parser.parse_args()

    salida = args.salida or args.datos / "textos-ciudad.json"
    agregados = json.loads(
        (args.datos / "agregados-ciudad.json").read_text(encoding="utf-8")
    )
    geo = json.loads((args.datos / "geo.json").read_text(encoding="utf-8"))
    medias = medias_atributos(agregados)

    nombres = {
        f"{provincia['slug']}/{ciudad['slug']}": ciudad["nombre"]
        for provincia in geo["provincias"]
        for ciudad in provincia["ciudades"]
    }
    seleccion = sorted(
        (
            (clave, agregado)
            for clave, agregado in agregados.items()
            if agregado["total"] >= args.minimo
        ),
        key=lambda par: (-par[1]["total"], par[0]),
    )

    textos = {}
    for clave, agregado in seleccion:
        nombre = nombres.get(clave)
        if not nombre:
            raise KeyError(f"{clave}: falta en geo.json")
        textos[clave] = redactar(nombre, agregado, clave, medias)

    salida.write_text(
        json.dumps(textos, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    palabras = [contar_palabras(texto) for texto in textos.values()]
    cubiertas = sum(agregado["total"] for _, agregado in seleccion)
    total_fichas = sum(agregado["total"] for agregado in agregados.values())
    print(f"{len(textos)} localidades redactadas")
    print(f"Cobertura: {cubiertas} de {total_fichas} fichas")
    print(f"Longitud: {min(palabras)}-{max(palabras)} palabras")
    print(f"Escrito en {salida}")


if __name__ == "__main__":
    main()
