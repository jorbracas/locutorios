#!/usr/bin/env python3
"""
Repara el texto mutilado por un fallo en `limpiar_meta` (corregir_fichas.py).

EL FALLO
--------
La funcion `limpiar_meta`, escrita en una pasada anterior para quitar el marco
de resenas ("Conoce sus servicios y las experiencias..."), usaba esta regex:

    r"\\s*(y|e)\\s+(las\\s+)?(experiencias?|opiniones|valoraciones|rese[ñn]as)..."

Sin `\\b` delante de `(y|e)`, la regex no exige que sea una palabra suelta:
coincide con la ultima letra de cualquier palabra que termine en "e" o "y"
seguida de "experiencia(s)", "opiniones", "valoraciones" o "resenas". En
"anos de experiencia," la "e" de "de" hace de "e" conjuncion, y la regex se
come "e experiencia" entero, dejando "anos d." Lo mismo le pasa a cualquier
palabra que termine en esas letras: "familiar en el centro... con mas de 10
anos d." en vez de "anos de experiencia".

Afecto solo a los campos `resumen` y `metaDescripcion`, que son los dos que
pasaban por esa funcion. `titulo` y `metaTitulo` usaban una funcion distinta
con la palabra correctamente delimitada, y no estan afectados.

LA REPARACION
--------------
No se reescribe el texto: se reconstruye con precision.

  1. Se toma el snapshot previo a que `corregir_fichas.py` se ejecutara por
     primera vez (guardado en /tmp/data_pre_correcciones), que conserva el
     texto sin el fallo.
  2. Se simula la version con fallo y la version corregida (con `\\b`) sobre
     ese texto original, lo que da el fragmento exacto que el fallo daño y su
     forma correcta.
  3. Se busca ese fragmento daniado, literal, dentro del texto ACTUAL. Solo si
     sigue presente tal cual se sustituye por su forma correcta. Si un cambio
     posterior legitimo ya toco esa frase, no se tira una moneda: se deja para
     revision manual antes que arriesgar una sustitucion a ciegas.

Uso:  python3 reparar_texto_mutilado.py ./data [--simular]
"""

import json
import re
import sys
from pathlib import Path

BACKUP_PRE_BUG = Path("/tmp/data_pre_correcciones")


def limpiar_meta_con_fallo(texto: str) -> str:
    """Replica exacta de la funcion original, defectuosa a proposito."""
    if not texto:
        return texto
    texto = re.sub(
        r"\s*(y|e)\s+(las\s+)?(experiencias?|opiniones|valoraciones|rese[ñn]as)"
        r"( de (los\s+)?(clientes|usuarios))?\s*\.?",
        ".", texto, flags=re.IGNORECASE)
    texto = re.sub(
        r"\s*Conoce sus puntos fuertes y las experiencias[^.]*\.?", "",
        texto, flags=re.IGNORECASE)
    texto = re.sub(
        r"(?:^|\s)[^.]*\b(experiencias? de (los\s+)?(clientes|usuarios)|"
        r"opiniones divididas|luces y sombras|puntos fuertes y d[eé]biles|"
        r"lo que (opinan|dicen) (los|sus) (clientes|usuarios))\b[^.]*\.",
        " ", texto, flags=re.IGNORECASE)
    texto = re.sub(r"\s{2,}", " ", texto).strip()
    texto = re.sub(r"\s+\.", ".", texto)
    texto = re.sub(r"\.{2,}", ".", texto)
    return texto


def paso1_bug(texto: str) -> str:
    """Solo la primera regex, defectuosa: sin limite de palabra."""
    return re.sub(
        r"\s*(y|e)\s+(las\s+)?(experiencias?|opiniones|valoraciones|rese[ñn]as)"
        r"( de (los\s+)?(clientes|usuarios))?\s*\.?",
        ".", texto, flags=re.IGNORECASE)


def paso1_fix(texto: str) -> str:
    """La misma regex, con el limite de palabra que faltaba."""
    return re.sub(
        r"\s*\b(y|e)\b\s+(las\s+)?(experiencias?|opiniones|valoraciones|rese[ñn]as)"
        r"( de (los\s+)?(clientes|usuarios))?\s*\.?",
        ".", texto, flags=re.IGNORECASE)


def paso_2_y_3(texto: str) -> str:
    """Las regex siguientes, identicas con o sin el fallo del paso 1."""
    texto = re.sub(
        r"\s*Conoce sus puntos fuertes y las experiencias[^.]*\.?", "",
        texto, flags=re.IGNORECASE)
    texto = re.sub(
        r"(?:^|\s)[^.]*\b(experiencias? de (los\s+)?(clientes|usuarios)|"
        r"opiniones divididas|luces y sombras|puntos fuertes y d[eé]biles|"
        r"lo que (opinan|dicen) (los|sus) (clientes|usuarios))\b[^.]*\.",
        " ", texto, flags=re.IGNORECASE)
    texto = re.sub(r"\s{2,}", " ", texto).strip()
    texto = re.sub(r"\s+\.", ".", texto)
    texto = re.sub(r"\.{2,}", ".", texto)
    return texto


def limpiar_meta_con_fallo(texto: str) -> str:
    return paso_2_y_3(paso1_bug(texto))


# Umbral de palabras: por encima, el tercer paso (que borra frases enteras de
# marco de resenas) esta eliminando algo mas que el simple envoltorio y se
# esta llevando por delante una critica operativa real, que la tarea pide
# conservar. Se descubrio comparando los 56 casos reales: en 4 de ellos el
# paso 3, aplicado sobre el texto ya sin el fallo del paso 1, borraba hasta 36
# palabras de contenido sustantivo (en un caso dejaba el resumen vacio).
UMBRAL_PERDIDA_ADICIONAL = 3


def reconstruir(texto_original: str) -> str:
    """
    Corrige solo el fallo del paso 1. Si el paso 3 borraria ademas contenido
    sustantivo que no tiene relacion con el fallo, se omite ese paso y se
    conserva la critica operativa intacta, solo con la gramatica reparada.
    """
    solo_paso1 = paso1_fix(texto_original)
    completo = paso_2_y_3(solo_paso1)

    perdida = len(solo_paso1.split()) - len(completo.split())
    if perdida > UMBRAL_PERDIDA_ADICIONAL:
        return solo_paso1
    return completo


def procesar(directorio: Path, simular: bool) -> None:
    if not BACKUP_PRE_BUG.exists():
        print(f"No se encuentra {BACKUP_PRE_BUG}: no hay texto de referencia "
              f"anterior al fallo. No se puede reparar con precisión.")
        sys.exit(1)

    backup = {
        ficha["id"]: ficha
        for archivo in BACKUP_PRE_BUG.glob("listings/*.json")
        for ficha in json.loads(archivo.read_text(encoding="utf-8"))
    }

    reparadas = 0
    detalle = []
    dudosas = []

    for archivo in sorted((directorio / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        modificado = False

        for ficha in fichas:
            original = backup.get(ficha["id"])
            if not original:
                continue

            for campo in ("resumen", "metaDescripcion"):
                texto_original = original.get(campo) or ""
                if not texto_original:
                    continue

                # El bug real solo existe si el paso 1 (la regex sin limite de
                # palabra) da un resultado DISTINTO al que da con el limite.
                # Si coinciden, la eliminacion fue correcta desde el principio
                # (un "y"/"e" suelto de verdad, no la ultima letra de otra
                # palabra) y no hay nada que reparar aqui.
                if paso1_bug(texto_original) == paso1_fix(texto_original):
                    continue

                dañado = limpiar_meta_con_fallo(texto_original)
                corregido = reconstruir(texto_original)
                if dañado == corregido:
                    continue

                actual = ficha.get(campo) or ""

                # Solo se repara cuando es matematicamente seguro: el texto
                # actual coincide EXACTAMENTE con lo que produjo el fallo sobre
                # el original. Si hubiera una diferencia adicional, una
                # correccion posterior legitima toco este mismo texto, y
                # sustituirlo a ciegas la perderia. En ese caso, a revision.
                if actual != dañado:
                    dudosas.append({
                        "nombre": ficha["nombre"],
                        "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                        "campo": campo,
                        "original": texto_original[:200],
                        "actual": actual[:200],
                    })
                    continue

                if not simular:
                    ficha[campo] = corregido
                    modificado = True

                reparadas += 1
                detalle.append({
                    "nombre": ficha["nombre"],
                    "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                    "campo": campo,
                    "antes": actual[:180],
                    "despues": corregido[:180],
                })

        if modificado and not simular:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")

    (directorio / "informe-reparacion-mutilado.json").write_text(
        json.dumps({"reparaciones": detalle, "dudosas": dudosas},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    print("SIMULACIÓN — no se ha escrito nada\n" if simular else "Aplicado\n")
    print(f"Fragmentos reparados: {reparadas}")
    print(f"Casos dudosos (edición posterior sobre el mismo texto): {len(dudosas)}")
    for entrada in detalle[:8]:
        print(f"  [{entrada['campo']}] {entrada['nombre'][:26]}")
        print(f"      antes:   …{entrada['antes'][-70:]}")
        print(f"      después: …{entrada['despues'][-70:]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    procesar(Path(sys.argv[1]), "--simular" in sys.argv)
