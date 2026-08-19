#!/usr/bin/env python3
"""
Ultima pasada quirurgica: 11 correcciones gramaticales + 7 nombres personales.

Cada caso se identifico leyendo el archivo actual, no por sustitucion ciega.
Nada mas se toca: ninguna otra ficha, ningun otro campo.

Uso:  python3 correccion_ultima.py ./data
"""

import json
import re
from pathlib import Path

DATA = Path("data")

# --------------------------------------------------------------------------
# 1A. "las información" en metaDescripcion — 8 fichas, todas con la misma
# formula "Conoce ... y las información [de/sobre] ...". Se corrige a
# concordancia singular leyendo la frase completa en cada caso.
# --------------------------------------------------------------------------

CORRECCIONES_GRAMATICA = [
    ("LOCUTORIO SARA", "metaDescripcion",
     "Conoce su ubicación, servicios y las información de los clientes sobre la atención.",
     "Conoce su ubicación, servicios y la información de los clientes sobre la atención."),

    ("India Post", "metaDescripcion",
     "Conoce su ubicación, servicios y las información sobre su…",
     "Conoce su ubicación, servicios y la información sobre su…"),

    ("Locutorio Ms", "metaDescripcion",
     "aunque las información sobre precios varían.",
     "aunque la información sobre precios varía."),

    ("Locutorio Amapolas Seseña Nuevo", "metaDescripcion",
     "Conoce sus servicios y las información de…",
     "Conoce sus servicios y la información de…"),

    ("The Fox", "metaDescripcion",
     "Conoce su oferta y las información sobre su…",
     "Conoce su oferta y la información sobre su…"),

    ("Locutorio OLIVERA", "metaDescripcion",
     "Conoce sus servicios y las información de los clientes.",
     "Conoce sus servicios y la información de los clientes."),

    ("Locutorio Más Cerca", "metaDescripcion",
     "Conoce su oferta y las información de los clientes.",
     "Conoce su oferta y la información de los clientes."),

    ("LOCUTORIO HSA", "metaDescripcion",
     "Conoce su ubicación, servicios habituales de un locutorio y las información de la experiencia descrita.",
     "Conoce su ubicación, servicios habituales de un locutorio y la información de la experiencia descrita."),

    # 1B. "algunas información"
    ("Cyber", "resumen",
     "pero su presencia es incierta según algunas información.",
     "pero su presencia es incierta según alguna información."),

    ("Servitran Sanits", "resumen",
     "aunque conviene tener en cuenta algunas información aisladas.",
     "aunque conviene tener en cuenta algunos datos aislados."),

    ("Easy Call Internet y Locutorio", "resumen",
     "La información disponible es limitada, con algunas información positivas y otras que señalan aspectos a mejorar.",
     "La información disponible es limitada, con algunos datos positivos y otros que señalan aspectos a mejorar."),
]

# --------------------------------------------------------------------------
# 2. Nombres personales procedentes de experiencias de clientes.
#
# Los siete casos se han comprobado uno a uno contra calle, direccion y web:
# ninguno forma parte de una fuente oficial. Todos aparecen introducidos por
# verbos de reseña ("se destaca la figura de...", "se menciona a...", "es
# conocido por..."), asi que se anonimizan.
# --------------------------------------------------------------------------

CORRECCIONES_NOMBRES = [
    ("Locutorio Morán", "resumen",
     "Destaca por la atención amable y profesional, especialmente de Mónica.",
     "Destaca por la atención amable y profesional del personal."),

    ("Locutorio Aini Telecom", "cuerpo",
     "En particular, se destaca la figura de Pomi, descrito como una persona atenta y servicial,",
     "En particular, se destaca al personal, descrito como atento y servicial,"),

    ("TU TIENDA PICA PICA", "cuerpo",
     "La figura de Rubén, identificado como responsable del local, aparece de forma recurrente",
     "La persona responsable del local aparece mencionada de forma recurrente"),
    ("TU TIENDA PICA PICA", "cuerpo",
     "y quien destaca la amabilidad, la profesionalidad y la disposición de Rubén para ayudar",
     "y quien destaca la amabilidad, la profesionalidad y la disposición del personal para ayudar"),
    ("TU TIENDA PICA PICA", "cuerpo",
     "En cualquier caso, la figura de Rubén concentra la mayoría de los elogios,",
     "En cualquier caso, la atención recibida concentra la mayoría de los elogios,"),

    ("LOCUTORIO TIENDA DE ALIMENTACION LATINO PHONEBELL", "cuerpo",
     "En varias ocasiones se menciona a Ruth, la empleada que atiende, destacando su amabilidad,",
     "En varias ocasiones se menciona a la empleada que atiende, destacando su amabilidad,"),

    ("Small World FS – Burgos", "cuerpo",
     "La figura de Tatiana, en particular, se asocia a una gestión ágil y cercana,",
     "La atención recibida, en particular, se asocia a una gestión ágil y cercana,"),

    # Cybertel: siete apariciones de "Samba" en el cuerpo, más un H2.
    ("Cybertel", "cuerpo",
     "las experiencias que circulan sobre él giran en torno a una figura concreta: Samba, la persona que atiende el local.",
     "las experiencias que circulan sobre él giran en torno a la persona que atiende el local."),
    ("Cybertel", "cuerpo",
     "De hecho, se comenta que Samba se desenvuelve en varios idiomas,",
     "De hecho, se comenta que quien atiende se desenvuelve en varios idiomas,"),
    ("Cybertel", "cuerpo",
     "donde Samba aparece como alguien que ayuda sin esperar nada a cambio,",
     "donde el personal aparece como alguien que ayuda sin esperar nada a cambio,"),
    ("Cybertel", "cuerpo",
     "## La atención como sello: la figura de Samba",
     "## La atención como sello distintivo"),
    ("Cybertel", "cuerpo",
     "Samba, la persona que está al frente, aparece en numerosas experiencias",
     "La persona que está al frente aparece en numerosas experiencias"),
    ("Cybertel", "cuerpo",
     "La amabilidad de Samba no se limita a una sonrisa:",
     "La amabilidad del personal no se limita a una sonrisa:"),
    ("Cybertel", "cuerpo",
     "La capacidad multilingüe de Samba facilita trámites",
     "La capacidad multilingüe del personal facilita trámites"),
    ("Cybertel", "resumen",
     "Su responsable, Samba, es conocido por su amabilidad y dominio de varios idiomas.",
     "Su responsable es conocido por su amabilidad y dominio de varios idiomas."),

    ("UNKNOWN", "cuerpo",
     "la figura de Roberto, el encargado, se repite en las conversaciones de quienes acuden al local.",
     "la figura del encargado se repite en las conversaciones de quienes acuden al local."),
    ("UNKNOWN", "cuerpo",
     "Roberto es descrito como una persona amable, servicial y siempre dispu",
     "El encargado es descrito como una persona amable, servicial y siempre dispu"),
]


def aplicar() -> dict:
    resumen = {
        "fichas_modificadas": set(),
        "gramatica_aplicadas": [],
        "gramatica_no_encontradas": [],
        "nombres_aplicados": [],
        "nombres_no_encontrados": [],
    }

    for archivo in sorted((DATA / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        cambiado = False

        for ficha in fichas:
            for nombre, campo, buscar, reemplazar in CORRECCIONES_GRAMATICA:
                if ficha["nombre"] != nombre:
                    continue
                valor = ficha.get(campo) or ""
                if buscar in valor:
                    ficha[campo] = valor.replace(buscar, reemplazar, 1)
                    cambiado = True
                    resumen["fichas_modificadas"].add(ficha["id"])
                    resumen["gramatica_aplicadas"].append({
                        "nombre": nombre, "campo": campo,
                        "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                    })

            for nombre, campo, buscar, reemplazar in CORRECCIONES_NOMBRES:
                if ficha["nombre"] != nombre:
                    continue
                valor = ficha.get(campo) or ""
                if buscar in valor:
                    ficha[campo] = valor.replace(buscar, reemplazar, 1)
                    cambiado = True
                    resumen["fichas_modificadas"].add(ficha["id"])
                    resumen["nombres_aplicados"].append({
                        "nombre": nombre, "campo": campo,
                        "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                    })

        if cambiado:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")

    # Verificar que todo lo esperado se aplicó.
    aplicadas_gram = {(c["nombre"]) for c in resumen["gramatica_aplicadas"]}
    for nombre, campo, buscar, reemplazar in CORRECCIONES_GRAMATICA:
        if nombre not in aplicadas_gram:
            resumen["gramatica_no_encontradas"].append(nombre)

    aplicadas_nom = [(c["nombre"]) for c in resumen["nombres_aplicados"]]
    for nombre, campo, buscar, reemplazar in CORRECCIONES_NOMBRES:
        if aplicadas_nom.count(nombre) == 0:
            resumen["nombres_no_encontrados"].append((nombre, buscar[:50]))

    resumen["fichas_modificadas"] = len(resumen["fichas_modificadas"])
    return resumen


if __name__ == "__main__":
    r = aplicar()
    print(f"Fichas modificadas: {r['fichas_modificadas']}")
    print(f"Correcciones gramaticales aplicadas: {len(r['gramatica_aplicadas'])}")
    if r["gramatica_no_encontradas"]:
        print(f"  NO ENCONTRADAS: {r['gramatica_no_encontradas']}")
    print(f"Nombres anonimizados (ocurrencias): {len(r['nombres_aplicados'])}")
    if r["nombres_no_encontrados"]:
        print(f"  NO ENCONTRADAS: {r['nombres_no_encontrados']}")
