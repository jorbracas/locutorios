#!/usr/bin/env python3
"""
Convierte imagenes a WebP en los dos anchos que usa el sitio.

Los PNG que salen de un generador de imagenes rondan los 2 MB cada uno. Sin
convertir, veinte imagenes son 44 MB y cada ficha arrastraria un lastre que se
nota en el LCP. En WebP a calidad 80 el conjunto baja a 4 MB sin diferencia
visible a los tamanos en que se muestran.

Uso:  python3 optimizar_imagenes.py <origen> <destino>
"""

import sys
from pathlib import Path

from PIL import Image

# 1400 para la portada, 720 para las bandas de ficha y de localidad.
ANCHOS = [(1400, ""), (720, "-720")]
EXTENSIONES = {".png", ".jpg", ".jpeg", ".webp"}


def optimizar(origen: Path, destino: Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    convertidas = 0

    for archivo in sorted(origen.iterdir()):
        if archivo.suffix.lower() not in EXTENSIONES:
            continue

        base = archivo.stem.replace("locutorio_", "")
        imagen = Image.open(archivo).convert("RGB")
        ancho_original, alto_original = imagen.size

        for ancho, sufijo in ANCHOS:
            if ancho > ancho_original:
                # No se amplia: solo se degradaria la imagen.
                redimensionada = imagen
            else:
                alto = round(alto_original * ancho / ancho_original)
                redimensionada = imagen.resize((ancho, alto), Image.LANCZOS)
            redimensionada.save(destino / f"{base}{sufijo}.webp", "WEBP",
                                quality=80, method=6)
        convertidas += 1
        print(f"  {archivo.name} -> {base}.webp / {base}-720.webp")

    peso = sum(f.stat().st_size for f in destino.glob("*.webp")) / 1_048_576
    print(f"\n{convertidas} imagenes convertidas · {peso:.1f} MB en total")
    print("Recuerda actualizar POR_TIPO y DESCRIPCION en "
          "src/components/Ilustracion.tsx con los nombres nuevos.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    optimizar(Path(sys.argv[1]), Path(sys.argv[2]))
