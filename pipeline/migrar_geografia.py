#!/usr/bin/env python3
"""
Pasada final de correccion geografica quirurgica.

Aplica movimientos verificados uno a uno, nunca por proximidad al centroide.
Cada movimiento se ha comprobado contra los propios datos del proyecto (que
localidad tiene realmente ese codigo postal segun otras fichas ya presentes)
y, cuando hacia falta, contra una fuente externa (Salt/Girona CP 17190,
Castellon de la Plana CP 12006).

Genera:
  - data/listings/*.json actualizados
  - data/redirects.json: mapa origen -> destino para next.config.mjs
  - data/informe-migracion-geografica.json: detalle de cada caso

Uso:  python3 migrar_geografia.py ./data
"""

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

DATA = Path("data")

NOMBRE_PROVINCIA = {
    "a-coruna": "A Coruña", "araba-alava": "Araba/Álava", "avila": "Ávila",
    "caceres": "Cáceres", "cadiz": "Cádiz", "castellon": "Castellón",
    "ciudad-real": "Ciudad Real", "cordoba": "Córdoba", "illes-balears": "Illes Balears",
    "jaen": "Jaén", "la-rioja": "La Rioja", "las-palmas": "Las Palmas",
    "leon": "León", "malaga": "Málaga", "ourense": "Ourense",
    "santa-cruz-de-tenerife": "Santa Cruz de Tenerife",
}


def titulizar(slug: str) -> str:
    if slug in NOMBRE_PROVINCIA:
        return NOMBRE_PROVINCIA[slug]
    minusculas = {"de", "del", "la", "las", "el", "los", "y", "i", "a", "d"}
    return " ".join(
        p if i > 0 and p in minusculas else p.capitalize()
        for i, p in enumerate(slug.split("-"))
    )


def slugificar(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto or "")
    t = t.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


# --------------------------------------------------------------------------
# Definicion de movimientos. Cada entrada identifica la ficha por un criterio
# inequivoco (nombre + fragmento de direccion/CP) y declara el destino.
# --------------------------------------------------------------------------

MOVIMIENTOS = [
    dict(
        criterio=lambda x: x["nombre"] == "Badalinks",
        destino_provincia="barcelona", destino_ciudad="badalona",
        nombre_ciudad="Badalona",
        direccion_nueva="Av. d'Alfons XIII, 551, 08918 Badalona, Barcelona",
        motivo="El CP 08918 corresponde a Badalona, no a Santa Coloma de Gramenet.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "LOCUTORIO BAR CAFERTERIA",
        destino_provincia="bizkaia", destino_ciudad="basauri",
        nombre_ciudad="Basauri",
        direccion_nueva="Butroe Ibaia Kalea, 48970 Basauri, Bizkaia, España",
        motivo="Butroe Ibaia Kalea, CP 48970, corresponde a Basauri.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Besmi Allah",
        destino_provincia="bizkaia", destino_ciudad="leioa",
        nombre_ciudad="Leioa",
        direccion_nueva="Sabino Arana, 82, 48940 Leioa, Bizkaia, España",
        motivo="Sabino Arana 82, CP 48940, corresponde a Leioa, no a Elexalde.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Noshi Locutorio",
        destino_provincia="bizkaia", destino_ciudad="leioa",
        nombre_ciudad="Leioa",
        direccion_nueva="48940 Leioa, Bizkaia, España",
        motivo="Normalización de denominación: Lejona y Leioa son el mismo municipio.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "CIBER LOCUTORIO EL PUERTO",
        destino_provincia="cadiz", destino_ciudad="el-puerto-de-sta-maria",
        nombre_ciudad="El Puerto de Santa María",
        direccion_nueva="C. Villa de Rota, 13, 11500 El Puerto de Santa María, Cádiz",
        motivo="'El' no es una localidad válida; era un truncamiento de El Puerto de Santa María.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Prensa - Locutorio Paris-Tombuctú",
        destino_provincia="castellon", destino_ciudad="alcossebre",
        nombre_ciudad="Alcossebre",
        direccion_nueva=None,
        motivo="'alcossebre-castellon' duplicaba la localidad; se normaliza a 'alcossebre'.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Locutorio Euroenvia",
        destino_provincia="girona", destino_ciudad="salt",
        nombre_ciudad="Salt",
        direccion_nueva=None,
        motivo="El CP 17190 (Travessera de Sta. Eugènia) corresponde a Salt, no a Girona capital.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "MoneyGram"
        and "Sta. Eugènia, 40, 17190" in x["direccion"],
        destino_provincia="girona", destino_ciudad="salt",
        nombre_ciudad="Salt",
        direccion_nueva=None,
        motivo="Mismo punto (Travessera de Sta. Eugènia 40) que Locutorio Euroenvia: Salt.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Locutorio Kafoul"
        and x["slugCiudad"] == "santa-eulalia-del-rio",
        destino_provincia="illes-balears", destino_ciudad="santa-eularia-des-riu",
        nombre_ciudad="Santa Eulària des Riu",
        direccion_nueva=None,
        motivo="Normalización de denominación: mismo municipio en dos grafías.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Locutorio mundo"
        and x["codigoPostal"] == "30006",
        destino_provincia="murcia", destino_ciudad="puente-tocinos",
        nombre_ciudad="Puente Tocinos",
        direccion_nueva=None,
        motivo="El CP 30006 corresponde a Puente Tocinos (pedanía de Murcia).",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Locutorio Essallam"
        and x["codigoPostal"] == "30570",
        destino_provincia="murcia", destino_ciudad="beniajan",
        nombre_ciudad="Beniaján",
        direccion_nueva=None,
        motivo="El CP 30570 corresponde a Beniaján (pedanía de Murcia).",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "Locutorio Danish"
        and x["codigoPostal"] == "46920" and x["slugCiudad"] == "valencia",
        destino_provincia="valencia", destino_ciudad="mislata",
        nombre_ciudad="Mislata",
        direccion_nueva="C/ del Pare Llansol, 3B, 46920 Mislata, Valencia",
        motivo="El CP 46920 corresponde a Mislata, no a València capital.",
    ),
    dict(
        criterio=lambda x: x["nombre"] == "International Locutorio - Sanfer",
        destino_provincia="valencia", destino_ciudad="mislata",
        nombre_ciudad="Mislata",
        direccion_nueva="Avinguda Blasco Ibáñez, 6, 46920 Mislata, Valencia",
        motivo="El CP 46920 corresponde a Mislata, no a València capital.",
    ),
    # Fichas solitarias en localidades redundantes, movidas tras confirmar
    # en los propios datos que corresponden a la localidad principal.
    dict(
        criterio=lambda x: x["slugCiudad"] == "arizgoiti"
        and x["slugProvincia"] == "bizkaia",
        destino_provincia="bizkaia", destino_ciudad="basauri",
        nombre_ciudad="Basauri",
        direccion_nueva=None,
        motivo="Única ficha de 'arizgoiti'; su propio nombre comercial dice 'BASAURI'.",
    ),
    dict(
        criterio=lambda x: x["slugCiudad"] == "castellon"
        and x["slugProvincia"] == "castellon",
        destino_provincia="castellon", destino_ciudad="castellon-de-la-plana",
        nombre_ciudad="Castellón de la Plana",
        direccion_nueva=None,
        motivo="Única ficha de 'castellon' (CP 12006, Castellón de la Plana); localidad redundante.",
    ),
]

# Casos explícitamente excluidos: no se mueven, se registran como
# "falso_positivo_sin_cambio" o "manual_sin_cambio" en el informe.
NO_MOVER = [
    ("ABDEL Market", "almeria/el-parador-de-las-hortichuelas",
     "El detector proponía Aguadulce por proximidad; se mantiene la localidad actual."),
    ("LOCUTORIO LA SALUT 114A", "barcelona/santa-coloma-de-gramenet",
     "El detector proponía Badalona por proximidad; se mantiene Santa Coloma de Gramenet."),
    ("Ria Money Transfer Agent & Payout", "castellon/castellon-de-la-plana",
     "Dirección Av. de l'Alcora 138: permanece en Castellón de la Plana, no se mueve a 'castellon'."),
    ("Locutorio Universal Internet Recarga de Móviles", "malaga/fuengirola",
     "El detector proponía Las Lagunas de Mijas por proximidad; se mantiene Fuengirola."),
    ("LOCUTORIO FERRARA", "malaga/torrox-costa",
     "Torrox Costa es localidad válida y más precisa que Torrox para esta dirección."),
    ("Locutorio Alfafar", "valencia/alfafar",
     "El detector proponía Benetússer por proximidad; se mantiene Alfafar."),
    ("Ria Money Transfer", "valencia/massanassa",
     "El detector proponía Catarroja por proximidad; se mantiene Massanassa."),
    ("LOCUTORIO QUART", "valencia/quart-de-poblet",
     "El detector proponía Manises por proximidad; se mantiene Quart de Poblet."),
    ("Locutorio Albufera", "valencia/sedavi",
     "El detector proponía Benetússer por proximidad; se mantiene Sedaví."),
]

MANUAL_SIN_CAMBIO = [
    ("Click World", "las-palmas/san-bartolome-de-tirajana",
     "La dirección está dentro del municipio de San Bartolomé de Tirajana; "
     "Maspalomas/San Fernando de Maspalomas depende del nivel administrativo "
     "usado y no hay evidencia concluyente para cambiar solo por proximidad."),
    ("LOCUTORIO ELEWUACUBA", "las-palmas/santa-lucia-de-tirajana",
     "Mismo problema de municipio/localidad que Click World; se mantiene sin cambio."),
]


def cargar_todas() -> tuple[dict[str, list[dict]], list[dict]]:
    datos = {
        a.stem: json.loads(a.read_text(encoding="utf-8"))
        for a in sorted((DATA / "listings").glob("*.json"))
    }
    todas = [f for fichas in datos.values() for f in fichas]
    return datos, todas


def aplicar() -> None:
    datos, todas = cargar_todas()
    redirects: list[dict] = []
    detalle_movidas: list[dict] = []
    detalle_falsos_positivos: list[dict] = []
    detalle_manual: list[dict] = []

    for entrada in NO_MOVER:
        nombre, ruta_actual, motivo = entrada
        detalle_falsos_positivos.append({
            "nombre": nombre, "url_actual": f"/{ruta_actual}", "motivo": motivo,
        })
    for entrada in MANUAL_SIN_CAMBIO:
        nombre, ruta_actual, motivo = entrada
        detalle_manual.append({
            "nombre": nombre, "url_actual": f"/{ruta_actual}", "motivo": motivo,
        })

    for movimiento in MOVIMIENTOS:
        for ficha in todas:
            if not movimiento["criterio"](ficha):
                continue

            url_antigua = f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}"
            provincia_antigua = ficha["slugProvincia"]
            ciudad_antigua = ficha["slugCiudad"]
            ciudad_antigua_nombre = ficha["ciudad"]

            # Actualizar campos estructurados.
            ficha["slugProvincia"] = movimiento["destino_provincia"]
            ficha["slugCiudad"] = movimiento["destino_ciudad"]
            ficha["provincia"] = titulizar(movimiento["destino_provincia"])
            ficha["ciudad"] = movimiento["nombre_ciudad"]

            if movimiento["direccion_nueva"]:
                ficha["direccion"] = movimiento["direccion_nueva"]
            elif ciudad_antigua_nombre and ciudad_antigua_nombre != movimiento["nombre_ciudad"]:
                # Sustituir la localidad antigua por la nueva dentro de la
                # cadena de direccion, solo si aparece literalmente.
                ficha["direccion"] = re.sub(
                    re.escape(ciudad_antigua_nombre),
                    movimiento["nombre_ciudad"],
                    ficha["direccion"],
                )

            # Textos: solo si mencionan explícitamente la localidad antigua.
            for campo in ("titulo", "metaTitulo", "metaDescripcion", "resumen", "cuerpo"):
                valor = ficha.get(campo) or ""
                if ciudad_antigua_nombre and ciudad_antigua_nombre in valor:
                    ficha[campo] = valor.replace(ciudad_antigua_nombre, movimiento["nombre_ciudad"])

            url_nueva = f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}"

            redirects.append({"source": url_antigua, "destination": url_nueva, "permanent": True})
            detalle_movidas.append({
                "nombre": ficha["nombre"],
                "url_anterior": url_antigua,
                "url_final": url_nueva,
                "direccion": ficha["direccion"],
                "accion": "movida",
                "motivo": movimiento["motivo"],
            })
            break  # cada movimiento identifica una única ficha

    # ------------------------------------------------------------------
    # Reagrupar por provincia (algunas fichas cambiaron de provincia) y
    # escribir. Las localidades de origen que se quedan sin fichas no
    # necesitan limpieza aparte: geo.json se reconstruye desde cero.
    # ------------------------------------------------------------------
    reagrupadas: dict[str, list[dict]] = defaultdict(list)
    for ficha in todas:
        reagrupadas[ficha["slugProvincia"]].append(ficha)

    for archivo in (DATA / "listings").glob("*.json"):
        archivo.unlink()
    for slug, fichas in reagrupadas.items():
        fichas.sort(key=lambda f: (f["slugCiudad"], -f.get("_rating", 0),
                                    -f.get("_reviews", 0), f["nombre"]))
        (DATA / "listings" / f"{slug}.json").write_text(
            json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8")

    # Redirects de página de ciudad, para las localidades que quedan vacías.
    ciudades_restantes = {(f["slugProvincia"], f["slugCiudad"]) for f in todas}
    ciudades_origen = {
        (m["destino_provincia"], slugificar(entrada.__self__)) for m in []  # placeholder, no usado
    }
    redirects_ciudad = []
    vaciadas = set()
    for movimiento, ficha_info in zip(MOVIMIENTOS, detalle_movidas):
        origen_prov, origen_ciudad = ficha_info["url_anterior"].strip("/").split("/")[:2]
        if (origen_prov, origen_ciudad) not in ciudades_restantes and (origen_prov, origen_ciudad) not in vaciadas:
            vaciadas.add((origen_prov, origen_ciudad))
            redirects_ciudad.append({
                "source": f"/{origen_prov}/{origen_ciudad}",
                "destination": f"/{movimiento['destino_provincia']}/{movimiento['destino_ciudad']}",
                "permanent": True,
            })

    todos_redirects = redirects + redirects_ciudad

    (DATA / "redirects.json").write_text(
        json.dumps(todos_redirects, ensure_ascii=False, indent=2), encoding="utf-8")

    informe = {
        "fichas_movidas": detalle_movidas,
        "falsos_positivos_geograficos": detalle_falsos_positivos,
        "revision_manual_sin_cambio": detalle_manual,
        "localidades_vaciadas": sorted(f"/{p}/{c}" for p, c in vaciadas),
        "redirects_creados": todos_redirects,
    }
    (DATA / "informe-migracion-geografica.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Fichas movidas: {len(detalle_movidas)}")
    for d in detalle_movidas:
        print(f"  {d['nombre'][:35]:35} {d['url_anterior']} -> {d['url_final']}")
    print(f"\nLocalidades vaciadas (redirect de ciudad): {len(vaciadas)}")
    for p, c in sorted(vaciadas):
        print(f"  /{p}/{c}")
    print(f"\nRedirects totales: {len(todos_redirects)}")
    print(f"Falsos positivos registrados sin cambio: {len(detalle_falsos_positivos)}")
    print(f"Revisión manual sin cambio: {len(detalle_manual)}")


if __name__ == "__main__":
    aplicar()
