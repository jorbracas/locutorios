#!/usr/bin/env python3
"""Valida cobertura, hechos y formato de ``textos-ciudad.json``.

El control es independiente del generador: vuelve a leer los agregados, limita
las cifras permitidas a cada localidad y rechaza residuos editoriales, lenguaje
que revele el origen interno de los datos y afirmaciones geográficas no
suministradas.

Uso:
    python3 pipeline/validar_textos_ciudad.py ./data
    python3 pipeline/validar_textos_ciudad.py ./data --informe ./data/INFORME-TEXTOS-CIUDAD.json
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import unicodedata
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


MINIMO_POR_DEFECTO = 5
MIN_PALABRAS = 180
MAX_PALABRAS = 240

PATRONES_PROHIBIDOS = {
    "origen de reseñas o scrapeo": re.compile(
        r"\b(reseñ\w*|opiniones?|comentarios?|scrap\w*|google|datos estructurados)\b",
        re.IGNORECASE,
    ),
    "terminología interna": re.compile(
        r"\b(fichas?|place[_ -]?id|json|csv|pipeline|archivo|informe)\b",
        re.IGNORECASE,
    ),
    "geografía urbana no suministrada": re.compile(
        r"\b(barrios?|distritos?|casco histórico|centro histórico|periferia|zona norte|zona sur|zona este|zona oeste)\b",
        re.IGNORECASE,
    ),
    "apertura inferida": re.compile(r"\b(abren|abre|cierran|cierra)\b", re.IGNORECASE),
    "calidad o marketing": re.compile(
        r"\b(excelente|inmejorable|mejor servicio|trato cercano|calidad del servicio|amplia variedad|todas tus necesidades)\b",
        re.IGNORECASE,
    ),
}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def contar_palabras(texto: str) -> int:
    limpio = re.sub(r"^#{1,6}\s+", "", texto, flags=re.MULTILINE)
    return len(re.findall(r"\S+", limpio))


def numeros(texto: object) -> set[Decimal]:
    encontrados: set[Decimal] = set()
    for coincidencia in re.finditer(r"\d+(?:[.,]\d+)?", str(texto)):
        bruto = coincidencia.group(0).replace(",", ".")
        try:
            encontrados.add(Decimal(bruto).normalize())
        except InvalidOperation:
            pass
    return encontrados


def numeros_permitidos(agregado: dict) -> set[Decimal]:
    permitidos: set[Decimal] = set()

    def incorporar(valor: object) -> None:
        permitidos.update(numeros(valor))

    incorporar(agregado["total"])
    incorporar(len(agregado["codigosPostales"]))
    incorporar(agregado["conTelefono"])
    for valor in agregado["tipos"].values():
        incorporar(valor)
    actividad = agregado.get("actividad")
    if actividad:
        for valor in actividad.values():
            incorporar(valor)
    for atributo in agregado.get("atributos", []):
        incorporar(atributo["cantidad"])
        incorporar(atributo["total"])
    for vecina in agregado.get("vecinas", []):
        incorporar(vecina["total"])
        incorporar(vecina["distancia"])
    return permitidos


def contiene_numero(texto: str, valor: object) -> bool:
    return bool(numeros(texto) & numeros(valor))


def validar_texto(
    clave: str,
    nombre: str,
    texto: str,
    agregado: dict,
) -> tuple[list[str], list[str], int]:
    errores: list[str] = []
    avisos: list[str] = []
    palabras = contar_palabras(texto)

    if not MIN_PALABRAS <= palabras <= MAX_PALABRAS:
        errores.append(f"longitud {palabras}; se esperaban {MIN_PALABRAS}-{MAX_PALABRAS}")

    encabezados = re.findall(r"^##\s+(.+)$", texto, flags=re.MULTILINE)
    if len(encabezados) != 1:
        errores.append(f"{len(encabezados)} encabezados H2; se exige exactamente 1")
    elif normalizar(nombre) not in normalizar(encabezados[0]):
        errores.append("el H2 no contiene el nombre de la localidad")

    if re.search(r"^#(?!#)\s", texto, flags=re.MULTILINE):
        errores.append("nota o encabezado H1 filtrado al contenido")
    if re.match(r"\s*(si estás buscando|en .+ encontrarás)", texto, flags=re.IGNORECASE):
        errores.append("apertura prohibida")

    for descripcion, patron in PATRONES_PROHIBIDOS.items():
        if patron.search(texto):
            errores.append(descripcion)

    conceptos = {
        "localidad": [nombre],
        "locutorio": ["locutorio"],
        "envío de dinero": ["envío de dinero", "enviar dinero", "remesa"],
        "cabinas o llamadas": ["cabina", "llamada"],
        "recargas": ["recarga"],
        "papelería o impresión": ["papelería", "impresión", "fotocopia"],
    }
    texto_normalizado = normalizar(texto)
    for concepto, variantes in conceptos.items():
        if not any(normalizar(variante) in texto_normalizado for variante in variantes):
            errores.append(f"falta el concepto obligatorio: {concepto}")

    requeridos = [
        agregado["total"],
        len(agregado["codigosPostales"]),
        agregado["conTelefono"],
        *agregado["tipos"].values(),
    ]
    for valor in requeridos:
        if valor == 0:
            continue
        if not contiene_numero(texto, valor):
            errores.append(f"falta cifra estructural: {valor}")

    actividad = agregado.get("actividad")
    if actividad:
        if actividad["franjaPunta"] not in texto:
            errores.append("falta la franja punta exacta")
        if actividad["franjaTranquila"] not in texto:
            errores.append("falta la franja tranquila exacta")
        for campo in ("muestra", "abrenDomingo", "cierreMediodia"):
            if not contiene_numero(texto, actividad[campo]):
                errores.append(f"falta actividad.{campo}: {actividad[campo]}")
        if "afluencia" not in texto_normalizado and "actividad" not in texto_normalizado:
            errores.append("no identifica la fuente como afluencia o actividad")
        if "horario" not in texto_normalizado:
            errores.append("falta la cautela que separa afluencia de horario")

    no_autorizados = numeros(texto) - numeros_permitidos(agregado)
    if no_autorizados:
        errores.append(
            "cifras no autorizadas: "
            + ", ".join(format(numero, "f") for numero in sorted(no_autorizados))
        )

    if "abierto" in texto_normalizado or "cerrado" in texto_normalizado:
        if not re.search(
            r"(no (?:permite )?(?:asegurar|confirmar|demuestra)|ni una confirmación|no confirma).{0,45}(abiert|cerrad)",
            texto,
            flags=re.IGNORECASE,
        ):
            avisos.append("menciona abierto/cerrado; revisar que sea una cautela y no una inferencia")

    return errores, avisos, palabras


def grupos_estructurales(textos: dict[str, str], nombres: dict[str, str]) -> list[list[str]]:
    grupos: dict[str, list[str]] = defaultdict(list)
    for clave, texto in textos.items():
        estructura = normalizar(texto)
        estructura = estructura.replace(normalizar(nombres[clave]), " ciudad ")
        estructura = re.sub(r"\b\d+(?:\s+\d+)*\b", " numero ", estructura)
        estructura = re.sub(r"\s+", " ", estructura).strip()
        grupos[estructura].append(clave)
    return [claves for claves in grupos.values() if len(claves) > 1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datos", type=Path)
    parser.add_argument("--textos", type=Path)
    parser.add_argument("--minimo", type=int, default=MINIMO_POR_DEFECTO)
    parser.add_argument("--informe", type=Path)
    args = parser.parse_args()

    textos_path = args.textos or args.datos / "textos-ciudad.json"
    agregados = json.loads(
        (args.datos / "agregados-ciudad.json").read_text(encoding="utf-8")
    )
    geo = json.loads((args.datos / "geo.json").read_text(encoding="utf-8"))
    textos = json.loads(textos_path.read_text(encoding="utf-8"))
    nombres = {
        f"{provincia['slug']}/{ciudad['slug']}": ciudad["nombre"]
        for provincia in geo["provincias"]
        for ciudad in provincia["ciudades"]
    }

    esperadas = {
        clave for clave, agregado in agregados.items() if agregado["total"] >= args.minimo
    }
    recibidas = set(textos)
    errores_globales = []
    if esperadas - recibidas:
        errores_globales.append(
            f"faltan {len(esperadas - recibidas)} localidades: "
            + ", ".join(sorted(esperadas - recibidas))
        )
    if recibidas - esperadas:
        errores_globales.append(
            f"sobran {len(recibidas - esperadas)} localidades: "
            + ", ".join(sorted(recibidas - esperadas))
        )

    resultados = []
    longitudes = []
    for clave in sorted(recibidas & esperadas):
        errores, avisos, palabras = validar_texto(
            clave, nombres[clave], textos[clave], agregados[clave]
        )
        longitudes.append(palabras)
        resultados.append(
            {"clave": clave, "palabras": palabras, "errores": errores, "avisos": avisos}
        )

    duplicados_exactos: dict[str, list[str]] = defaultdict(list)
    for clave, texto in textos.items():
        duplicados_exactos[normalizar(texto)].append(clave)
    grupos_exactos = [claves for claves in duplicados_exactos.values() if len(claves) > 1]
    grupos_plantilla = grupos_estructurales(textos, nombres)

    total_errores = len(errores_globales) + sum(
        len(resultado["errores"]) for resultado in resultados
    )
    total_avisos = sum(len(resultado["avisos"]) for resultado in resultados)
    informe = {
        "estado": "PASS" if total_errores == 0 else "FAIL",
        "localidadesEsperadas": len(esperadas),
        "localidadesValidadas": len(recibidas & esperadas),
        "fichasCubiertas": sum(agregados[clave]["total"] for clave in recibidas & esperadas),
        "fichasTotales": sum(agregado["total"] for agregado in agregados.values()),
        "palabrasMinimo": min(longitudes, default=0),
        "palabrasMaximo": max(longitudes, default=0),
        "palabrasMedia": round(statistics.mean(longitudes), 1) if longitudes else 0,
        "duplicadosExactos": grupos_exactos,
        "estructurasExactasRepetidas": grupos_plantilla,
        "erroresGlobales": errores_globales,
        "totalErrores": total_errores,
        "totalAvisos": total_avisos,
        "resultadosConProblemas": [
            resultado
            for resultado in resultados
            if resultado["errores"] or resultado["avisos"]
        ],
    }

    if args.informe:
        args.informe.write_text(
            json.dumps(informe, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(informe, ensure_ascii=False, indent=2))
    raise SystemExit(0 if informe["estado"] == "PASS" else 1)


if __name__ == "__main__":
    main()
