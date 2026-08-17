# Prompts para generar imágenes de locutorios

Cuatro prompts maestros, diez variaciones cada uno. Cuarenta imágenes en total.

## Antes de empezar: qué falló en la primera tanda

La tanda actual tiene tres problemas que estos prompts corrigen.

**Ambientación equivocada.** Varias imágenes son claramente latinoamericanas o
estadounidenses: un rótulo de «Comida Criolla» al lado, carteles de «pagos de
biles», billetes que no son euros. Para un directorio español desentona y le
resta credibilidad al sitio.

**Equipamiento anticuado.** Una de las imágenes muestra monitores CRT de hace
veinte años. Eso describe el locutorio de 2005, no el de ahora.

**Marcas reales.** Si aparece un logotipo identificable de Western Union o Ria
estás usando una marca registrada sin licencia, y encima insinúas que ese
establecimiento concreto trabaja con ese operador.

Los prompts de abajo incorporan las tres correcciones. Van en inglés porque los
modelos de imagen responden bastante mejor, aunque el texto de los rótulos tiene
que ir en español.

---

## Reglas comunes a los cuatro prompts

Pega este bloque al final de cada prompt:

```
STYLE: Photorealistic documentary photography, natural available light, shot on
35mm, shallow-to-medium depth of field. Neutral color grading, no HDR, no
oversaturation. 4:3 aspect ratio.

MUST INCLUDE: Spanish urban context — European shopfront proportions, metal
roller shutter (persiana metálica), terrazzo or ceramic tile flooring, Spanish
street furniture, euro currency if money is visible.

MUST AVOID: No recognizable brand logos or trademarks of any company. No
identifiable human faces — people seen from behind, in profile, cropped, or
blurred only. No Latin American or US signage, food or products. No CRT monitors
or pre-2015 technology. No text in English. No AI-glossy look, no fake bokeh, no
cinematic teal-orange grade.

TEXT IN IMAGE: Keep signage to single short Spanish words only (LOCUTORIO,
ENVÍOS, RECARGAS, INTERNET, COPIAS, ABIERTO). Long sentences render as garbled
characters.
```

---

## Prompt 1 — Fachadas de día

> A street-level photograph of a small *locutorio* (call shop and money transfer
> business) in Spain, seen from the opposite pavement. The shopfront has a large
> window with a simple sign above it and a list of services painted on the glass.
> Ordinary residential building above, typical of a Spanish city.
>
> Generate 10 variations:
> 1. Narrow shopfront in a working-class Madrid neighbourhood, brick and tile façade, mid-morning light
> 2. Corner shop in a Barcelona *eixample* block, tall windows, stone façade
> 3. Small locutorio in an Andalusian town, whitewashed wall, strong midday sun and hard shadows
> 4. Shopfront in a Valencian street with orange trees and a scooter parked outside
> 5. Locutorio between a hairdresser and a fruit shop in a Sevilla side street
> 6. Northern Spain, Bilbao or Santander, overcast grey sky, damp pavement
> 7. Wide shopfront in a modern suburban block, aluminium frame, plain sign
> 8. Locutorio in a pedestrian street with paving stones, no cars, people walking past from behind
> 9. Shopfront with the roller shutter half raised, early morning, empty street
> 10. Locutorio in a small Castilian town, low building, wide pavement, few passers-by

## Prompt 2 — Fachadas de noche y tarde

> A photograph of a *locutorio* shopfront in Spain at dusk or after dark. The
> interior lights spill onto the pavement. The sign is illuminated. The mood is
> quiet and ordinary, not dramatic.
>
> Generate 10 variations:
> 1. Rainy night, wet asphalt reflecting the shop's light, no people
> 2. Blue hour, sign just switched on, a person walking past seen from behind
> 3. Winter evening, breath visible, warm interior contrasting with cold street
> 4. Narrow old-town street at night, stone walls, single light source
> 5. Shopfront closed with the roller shutter down, street lamp overhead
> 6. Summer night, door open, warm light, chairs visible inside
> 7. Late evening in a busy commercial street, other shops lit in the background
> 8. Locutorio next to a bar terrace at night, empty chairs stacked
> 9. Rain seen through the window from inside, looking out at the street
> 10. Sign reflected in a puddle, low camera angle, no people

## Prompt 3 — Interiores en uso

> Interior of a modern Spanish *locutorio*. A service counter, a printer and
> scanner, a small shelf of mobile phone accessories and prepaid SIM cards, and a
> row of two or three computer workstations with current flat monitors. Clean,
> functional, modest. Fluorescent or LED ceiling lighting. Any people are seen
> from behind or cropped at the shoulders.
>
> Generate 10 variations:
> 1. Wide shot of the whole interior from the doorway, empty of customers
> 2. Counter area with a person seen from behind being attended, printer visible
> 3. Row of computer desks along a wall, modern monitors, empty chairs
> 4. Recently refurbished interior, wood and white, plants, minimal signage
> 5. Older but well-kept interior, tiled floor, painted walls, shelving
> 6. Narrow long shop, counter on the right, workstations on the left
> 7. Detail of the printing and photocopying corner, paper trays, guillotine
> 8. Small waiting area with two chairs and a leaflet stand
> 9. Interior seen from behind the counter looking towards the street door
> 10. Quiet moment, no customers, afternoon light coming through the window

## Prompt 4 — Detalles de mostrador y servicios

> Close-up photograph inside a Spanish *locutorio*, focused on one service. Shot
> at counter height, natural depth of field. Hands may appear but never faces.
> Any money visible is euro notes and coins.
>
> Generate 10 variations:
> 1. Hands filling in a money transfer form on the counter, pen and paper, card reader nearby
> 2. Card payment terminal on the counter with a receipt printing
> 3. Rack of prepaid SIM cards and top-up vouchers, generic packaging, no brand names
> 4. Multifunction printer mid-copy, sheet emerging from the tray
> 5. Shelf of phone cases, cables and chargers, neatly arranged
> 6. Small parcels and padded envelopes stacked ready for collection
> 7. Passport photo corner: white backdrop, stool, camera on a tripod
> 8. Counter from the customer's side: card reader, pen pot, hand sanitiser, price list
> 9. Euro notes and coins being counted on a counter mat, hands only
> 10. Laminating machine and stationery on a side table, documents in a tray

---

## Qué hacer con las que salgan

Genera las cuarenta y descarta sin piedad. En este tipo de material se cae la
mitad: por texto ilegible en los rótulos, por manos con seis dedos, o por
ambientación que no acaba de ser española. Con veinticinco buenas vas sobrado.

Cuando las tengas, pásalas por el script de conversión que ya está en el
proyecto y actualiza `POR_TIPO` en `src/components/Ilustracion.tsx` con los
nombres nuevos:

```bash
python3 pipeline/optimizar_imagenes.py /ruta/a/las/nuevas public/ilustraciones
```

Un apunte sobre el reparto: los grupos de `Ilustracion.tsx` asignan las imágenes
según el tipo de ficha. Las fachadas de día y de noche sirven para cualquiera;
los detalles de mostrador de envío deben ir solo a fichas de tipo `envio`, y los
puestos de internet solo a las de tipo `locutorio`. Repartir mal es lo único que
puede hacer que una imagen ilustrativa resulte contradictoria con el texto.
