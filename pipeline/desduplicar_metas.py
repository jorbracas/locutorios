#!/usr/bin/env python3
"""
Resuelve los 7 pares de metaTitulo duplicados y la metaDescripcion duplicada.

Diferencia por calle o numero, sin inventar servicios ni caracteristicas que
no consten en los datos.

Uso:  python3 desduplicar_metas.py ./data
"""

import json
import re
from pathlib import Path

DATA = Path("data")


def via_corta(calle: str) -> str:
    """Nombre de la via sin el tipo (Calle/Avenida) ni el numero."""
    limpio = re.sub(
        r"^(calle|c/|c\.|avenida|avda|av\.|paseo|plaza|pl\.|carrer|ronda)\s*",
        "", calle.strip(), flags=re.IGNORECASE,
    )
    limpio = re.sub(r",?\s*\d+.*$", "", limpio).strip()
    return limpio


# Cada entrada: criterio para localizar la ficha + sufijo con el que se
# diferencia su metaTitulo (y su metaDescripcion, si aplica).
CASOS = [
    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="bilbao",
         marca="Plaza Biribila", sufijo=" (Pl. Biribila)"),
    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="bilbao",
         marca="Zingira", sufijo=" (Zingira Kalea)"),

    dict(nombre="MoneyGram", ciudad="tortosa",
         marca="Francesc Gimeno", sufijo=None,
         meta_titulo="MoneyGram Tortosa (C. Francesc Gimeno) | Transferencias de dinero y más",
         meta_desc="MoneyGram en Carrer Francesc Gimeno 3, Tortosa: transferencias de "
                    "dinero, pago de facturas y otros servicios."),
    dict(nombre="MoneyGram", ciudad="tortosa",
         marca="Sant Vicent", sufijo=None,
         meta_titulo="MoneyGram Tortosa (C. Llarg de Sant Vicent) | Transferencias de dinero y más",
         meta_desc="MoneyGram en Carrer Llarg de Sant Vicent 55, Tortosa: transferencias "
                    "de dinero, pago de facturas y otros servicios."),

    dict(nombre="Ria Money Transfer Agent", ciudad="corral-de-almaguer",
         marca="C. Real, 145", sufijo=" (C. Real 145)"),
    dict(nombre="Ria Money Transfer Agent", ciudad="corral-de-almaguer",
         marca="C. Real, 101", sufijo=" (C. Real 101)"),

    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="talayuela",
         marca="Manuel Mas, 62", sufijo=" (C. Manuel Mas 62)"),
    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="talayuela",
         marca="Manuel Mas, 69", sufijo=" (C. Manuel Mas 69)"),

    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="cartagena",
         marca="Serreta", sufijo=" (C. de la Serreta)"),
    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="cartagena",
         marca="Arco de la Caridad", sufijo=" (C. Arco de la Caridad)"),

    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="valencia",
         marca="Trafalgar", sufijo=" (Carrer de Trafalgar)"),
    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="valencia",
         marca="Josep Grollo", sufijo=" (Carrer de Josep Grollo)"),

    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="callosa-de-segura",
         marca="Pedro Aragonés", sufijo=" (C. Pedro Aragonés)"),
    dict(nombre="Ria Money Transfer Agent & Payout", ciudad="callosa-de-segura",
         marca="Hermanos Parra", sufijo=" (C. Hermanos Parra)"),
]


def procesar() -> list[dict]:
    aplicadas = []
    for archivo in sorted((DATA / "listings").glob("*.json")):
        fichas = json.loads(archivo.read_text(encoding="utf-8"))
        cambiado = False

        for ficha in fichas:
            for caso in CASOS:
                if (
                    ficha["nombre"] != caso["nombre"]
                    or ficha["slugCiudad"] != caso["ciudad"]
                    or caso["marca"] not in ficha["direccion"]
                ):
                    continue

                antes_titulo = ficha["metaTitulo"]
                antes_desc = ficha.get("metaDescripcion", "")

                if caso.get("meta_titulo"):
                    ficha["metaTitulo"] = caso["meta_titulo"]
                elif caso.get("sufijo"):
                    ficha["metaTitulo"] = ficha["metaTitulo"] + caso["sufijo"]

                if caso.get("meta_desc"):
                    ficha["metaDescripcion"] = caso["meta_desc"]

                cambiado = True
                aplicadas.append({
                    "nombre": ficha["nombre"],
                    "url": f"/{ficha['slugProvincia']}/{ficha['slugCiudad']}/{ficha['slug']}",
                    "metaTituloAntes": antes_titulo,
                    "metaTituloDespues": ficha["metaTitulo"],
                    "metaDescripcionCambiada": bool(caso.get("meta_desc")),
                })
                break

        if cambiado:
            archivo.write_text(
                json.dumps(fichas, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")

    return aplicadas


if __name__ == "__main__":
    resultado = procesar()
    print(f"metaTitulo/metaDescripcion diferenciados: {len(resultado)}")
    for r in resultado:
        print(f"  {r['nombre'][:30]:30} {r['url']}")
        print(f"    -> {r['metaTituloDespues']}")
    (DATA / "informe-desduplicacion-metas.json").write_text(
        json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
