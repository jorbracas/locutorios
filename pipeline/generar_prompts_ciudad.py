#!/usr/bin/env python3
"""
Genera los prompts de redaccion para las paginas de localidad.

POR QUE NO SE REDACTAN LAS 803
------------------------------
El 55 % de las localidades tiene un unico establecimiento. Redactar 442 parrafos
sobre "el panorama de los locutorios en un pueblo con un locutorio" produce
exactamente el relleno que Google penaliza, y ademas cuesta dinero en tokens
para paginas que reciben visitas testimoniales.

Esas localidades ya quedan diferenciadas por los datos agregados y las preguntas
frecuentes, que son distintos en cada una porque salen de recuentos reales. El
texto redactado se reserva para donde hay volumen de busqueda que justifique el
esfuerzo.

COMO EVITA EL TEXTO DE PLANTILLA
--------------------------------
Cada prompt lleva incrustados los datos concretos de esa localidad: el reparto
por tipo, la franja punta, cuantos abren domingo, los codigos postales, las
localidades vecinas. Dos ciudades del mismo tamano generan textos distintos
porque parten de hechos distintos, no de un adjetivo cambiado.

El prompt tambien prohibe explicitamente inventar: sin nombres de operadores,
sin comisiones, sin horarios que no esten en los datos.

Uso:  python3 generar_prompts_ciudad.py ./data [--minimo 5] [--salida prompts.md]
"""

import argparse
import json
from pathlib import Path

# Por debajo de este numero de establecimientos, los datos agregados y las
# preguntas frecuentes ya diferencian la pagina de sobra.
MINIMO_POR_DEFECTO = 5

PLANTILLA = """\
### {nombre} ({provincia}) — `{clave}`

```
Escribe un texto de 180 a 240 palabras para la página de {nombre} de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE {nombre_mayus} (no uses ningún otro):
{datos}

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en {nombre}".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de {nombre}.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En {nombre} encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```
"""


def describir(clave: str, agregado: dict, nombre: str) -> str:
    lineas = []
    tipos = agregado["tipos"]
    lineas.append(f"- Total de establecimientos: {agregado['total']}")
    lineas.append(
        f"- Reparto: {tipos['locutorio']} locutorios, {tipos['envio']} "
        f"especializados en envío de dinero, {tipos['otros']} comercios con "
        f"servicios relacionados"
    )

    if agregado["codigosPostales"]:
        lineas.append(
            f"- Códigos postales cubiertos: {', '.join(agregado['codigosPostales'])}"
        )

    lineas.append(f"- Con teléfono publicado: {agregado['conTelefono']}")

    actividad = agregado.get("actividad")
    if actividad:
        lineas.append(
            f"- Franja de mayor afluencia: {actividad['franjaPunta']} "
            f"(estimación sobre {actividad['muestra']} locales)"
        )
        lineas.append(f"- Franja más tranquila: {actividad['franjaTranquila']}")
        if actividad["abrenDomingo"]:
            lineas.append(
                f"- Con actividad registrada en domingo: {actividad['abrenDomingo']} "
                f"de {actividad['muestra']}"
            )
        if actividad["cierreMediodia"]:
            lineas.append(
                f"- Con jornada partida (cierre al mediodía): "
                f"{actividad['cierreMediodia']} de {actividad['muestra']}"
            )

    for atributo in agregado["atributos"][:5]:
        cobertura = (
            f"los {atributo['total']}"
            if atributo["todos"]
            else f"{atributo['cantidad']} de {atributo['total']}"
        )
        lineas.append(f"- {atributo['valor']}: {cobertura}")

    if agregado["vecinas"]:
        vecinas = ", ".join(
            f"{v['nombre']} ({v['total']} establecimientos, a {v['distancia']} km)"
            for v in agregado["vecinas"][:3]
        )
        lineas.append(f"- Localidades cercanas con oferta: {vecinas}")

    return "\n".join(lineas)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datos", type=Path)
    parser.add_argument("--minimo", type=int, default=MINIMO_POR_DEFECTO)
    parser.add_argument("--salida", type=Path, default=Path("prompts-ciudades.md"))
    args = parser.parse_args()

    agregados = json.loads(
        (args.datos / "agregados-ciudad.json").read_text(encoding="utf-8")
    )
    geo = json.loads((args.datos / "geo.json").read_text(encoding="utf-8"))

    nombres = {}
    for provincia in geo["provincias"]:
        for ciudad in provincia["ciudades"]:
            nombres[f"{provincia['slug']}/{ciudad['slug']}"] = (
                ciudad["nombre"],
                provincia["nombre"],
            )

    seleccion = [
        (clave, dato)
        for clave, dato in agregados.items()
        if dato["total"] >= args.minimo
    ]
    seleccion.sort(key=lambda par: -par[1]["total"])

    bloques = [
        "# Prompts de redacción por localidad\n",
        f"{len(seleccion)} localidades con {args.minimo} o más establecimientos, "
        f"ordenadas de mayor a menor.\n",
        "Pega cada bloque en el modelo, y guarda la respuesta en "
        "`data/textos-ciudad.json` con la clave que aparece en el título:\n",
        '```json\n{\n  "madrid/getafe": "El texto devuelto…"\n}\n```\n',
        "---\n",
    ]

    for clave, dato in seleccion:
        nombre, provincia = nombres.get(clave, (clave, ""))
        bloques.append(
            PLANTILLA.format(
                nombre=nombre,
                nombre_mayus=nombre.upper(),
                provincia=provincia,
                clave=clave,
                datos=describir(clave, dato, nombre),
            )
        )

    args.salida.write_text("\n".join(bloques), encoding="utf-8")

    cubiertas = sum(dato["total"] for _, dato in seleccion)
    total_fichas = sum(dato["total"] for dato in agregados.values())
    print(f"{len(seleccion)} localidades seleccionadas (mínimo {args.minimo})")
    print(f"Cubren {cubiertas} de {total_fichas} fichas "
          f"({100 * cubiertas / total_fichas:.0f} % del directorio)")
    print(f"\nEscrito en {args.salida}")


if __name__ == "__main__":
    main()
