# locutorioscercademi.com

Directorio de locutorios y puntos de envío de dinero en España. Next.js 15 (App
Router), TypeScript, Tailwind v4. Todo el sitio se genera en compilación: no hay
base de datos ni llamadas en tiempo de ejecución.

**3.050 fichas · 803 localidades · 52 provincias · 3.915 páginas estáticas.**

---

## Puesta en marcha

```bash
npm install
npm run dev          # http://localhost:3000
npm run build        # genera las 3.915 páginas
npm run typecheck
```

El build tarda unos minutos por el volumen de páginas. Es normal.

## Estructura

```
data/
  geo.json                   índice de provincias y localidades
  listings/<provincia>.json  fichas completas, un fichero por provincia
pipeline/
  build_data.py              CSV maestro -> JSON
src/
  app/
    page.tsx                            portada
    provincias/page.tsx                 índice de provincias
    [provincia]/page.tsx                provincia
    [provincia]/[ciudad]/page.tsx       localidad
    [provincia]/[ciudad]/[negocio]/     ficha
    sitemap.ts  robots.ts  not-found.tsx
  components/
    Chapa.tsx      rótulo SVG generado por negocio
    Buscador.tsx   búsqueda de localidades en cliente
    Mapa.tsx       mapa bajo demanda
    Ui.tsx         migas, tarjetas, distintivos, JSON-LD
  lib/
    data.ts        acceso a datos con caché
    seo.ts         metadatos y JSON-LD
    markdown.ts    renderizador del texto editorial
```

## Regenerar los datos

El CSV maestro pesa unos 170 MB. **No se versiona**: GitHub rechaza ficheros de
más de 100 MB y `.gitignore` ya excluye `*.csv`. Guárdalo fuera del repositorio
y regenera cuando haya datos nuevos:

```bash
python3 pipeline/build_data.py /ruta/al/locutorios.csv ./data
```

Lo que hace el pipeline, además de convertir el formato:

- Recupera Ceuta y Melilla, que llegaban sin provincia por ser ciudades autónomas.
- Descarta 6 filas sin ciudad, sin provincia reconocible o sin slug.
- Garantiza que `provincia/ciudad/negocio` sea único, añadiendo sufijo si hace falta.
- Construye títulos que quepan en 60 caracteres y desambigua los repetidos
  añadiendo la calle (las cadenas de remesas repiten nombre en la misma ciudad).
- Extrae los atributos del JSON `about` de Google a una estructura plana.
- Descarta webs que apuntan a Google, que no aportan nada al usuario.

## Despliegue

1. `git init && git add . && git commit -m "Versión inicial"`
2. Subir a GitHub.
3. Importar el repositorio en Vercel.
4. Añadir `locutorioscercademi.com` en **Settings → Domains** y apuntar los DNS.
5. Antes de que entre tráfico: dar de alta el dominio en Google Search Console y
   enviar `https://locutorioscercademi.com/sitemap.xml`.

### El framework tiene que ser Next.js

`vercel.json` fija `"framework": "nextjs"` a propósito, y no conviene quitarlo.

Si el proyecto de Vercel queda con el preset en «Other», ocurre algo que despista
mucho: el build **termina correctamente**, genera las 3.915 páginas y el log no
muestra ni un error, pero después Vercel sirve solo la carpeta `public/` e ignora
la salida de `next build`. El resultado es que las imágenes de
`/ilustraciones/` responden 200 mientras que la portada, las fichas y hasta
`/robots.txt` devuelven 404.

Fijarlo en `vercel.json` evita depender de la detección automática y deja la
configuración en el repositorio. Si aun así siguiera fallando, comprobar en
**Settings → Build and Deployment** que *Output Directory* esté sin sobrescribir:
un valor manual en ese campo tiene prioridad sobre el preset.

---

## Decisiones de SEO

**Arquitectura de URLs.** `/{provincia}/{ciudad}/{negocio}`, sin prefijos ni barra
final. El slug de negocio se repite 624 veces a nivel nacional, así que los tres
niveles son necesarios para que las rutas sean únicas.

**Provincias en `noindex, follow`.** Son nodos de navegación: su contenido es una
lista de enlaces que competiría con las páginas de localidad, que sí responden a
una intención de búsqueda real. El `follow` es imprescindible; sin él se cortaría
el rastreo hacia las 803 localidades y las 3.050 fichas.

**`/provincias` sí se indexa.** Con las provincias en `noindex`, este índice es el
camino corto entre la portada y el resto del sitio. Sin él, el rastreo dependería
solo del sitemap.

**Sin `aggregateRating` ni `review` en el marcado.** Las valoraciones del CSV son
de Google y no las hemos recogido nosotros. Marcarlas como propias incumple la
política de datos estructurados y expone el dominio a una acción manual. El
`LocalBusiness` se limita a hechos verificables: nombre, dirección, coordenadas,
teléfono. Las valoraciones sí se usan internamente para ordenar los listados,
donde no son visibles ni marcables.

**Sin fotos de Google.** Las 3.034 imágenes disponibles eran de Street View y de
`lh3.googleusercontent.com`. Enlazarlas incumple sus términos, las URLs caducan
sin aviso y penalizan el LCP. En su lugar, cada negocio tiene una *chapa*: un SVG
generado a partir de un hash de su identificador, siempre igual para el mismo
negocio, sin peticiones de red y sin desplazamiento de layout.

**Mapa bajo demanda.** El iframe de OpenStreetMap solo se inserta al pulsar. De
otro modo, cada una de las 3.050 fichas cargaría un tercero bloqueante justo en
el elemento que compite por el LCP.

**Sitemap sin las provincias.** Declarar en el sitemap una URL que pides no
indexar es una señal contradictoria que Search Console marca como error.

---

## Actividad observada, no horarios

`hours` viene vacío en las 3.050 fichas, pero 1.238 (41 %) traen `popular_times`:
la afluencia por hora que Google calcula a partir de señales de ubicación. El
pipeline la convierte en franjas contiguas de actividad.

No es lo mismo que un horario y la web nunca lo llama así. Aun así deduce mucho:
592 fichas muestran el corte del mediodía de la jornada partida y 154 revelan el
día de cierre semanal. El bloque se titula «Cuándo suele haber movimiento» y
lleva al pie el aviso de que es un dato estimado, no facilitado por el
establecimiento.

## Ilustraciones

40 imágenes generadas para este proyecto en `public/ilustraciones/`, en WebP a
720 y 1400 px de ancho (6,7 MB en total). Sustituyen a la primera tanda de 20:
esta corrige la ambientación latinoamericana, el equipamiento anticuado y evita
cualquier marca real reconocible. No son fotos de los establecimientos, así que
se usan con dos reglas fijas:

- **Nunca en la cabecera de la ficha.** Ahí manda la chapa, que sí es única de
  cada negocio. Las ilustraciones van dentro del contenido, acompañando al texto.
- **Siempre con pie de foto** que aclara que la imagen no corresponde a ese
  establecimiento. Alguien que llega buscando un local concreto y ve la foto de
  otro se lleva una impresión falsa.

El reparto es determinista por `place_id` y respeta el tipo, definido en
`POR_TIPO` dentro de `src/components/Ilustracion.tsx`:

- Fachadas de día y de noche (20): neutras, sirven para cualquier tipo de ficha.
- Interiores y detalles de locutorio (12): puestos de ordenador, impresión,
  fotos de carné — solo en fichas `locutorio`.
- Interiores y detalles de envío de dinero (6): mostrador, formulario, euros —
  solo en fichas `envio`.
- Detalles de accesorios y SIM (2): para fichas `otros`.

### Añadir una nueva tanda

```bash
python3 pipeline/optimizar_imagenes.py /ruta/a/las/nuevas public/ilustraciones
```

Después hay que dar de alta cada nombre nuevo en `FACHADAS` o `POR_TIPO`, y su
descripción en `DESCRIPCION`, dentro de `src/components/Ilustracion.tsx`. El
script solo convierte; el reparto por tipo se mantiene manual a propósito, para
no colar por error una imagen de envío de dinero en una ficha que no ofrece
ese servicio.

## Saneamiento de riesgo reputacional

`pipeline/despersonalizar.py` ya se ha aplicado sobre `data/`. Vuelve a pasarlo
cada vez que regeneres los datos desde el CSV:

```bash
python3 pipeline/build_data.py /ruta/al/locutorios.csv ./data
python3 pipeline/despersonalizar.py ./data          # obligatorio despues
python3 pipeline/despersonalizar.py ./data --simular  # ver sin aplicar
```

Sobre 3.050 fichas afectó a 494 (16 %): 369 frases eliminadas y 262 citas
integradas. La media perdida son 18 palabras y ninguna ficha baja de 460, así
que el impacto en contenido es despreciable.

Qué elimina y por qué:

- **Imputaciones de delito** («estafa», «timo», «fraudulentas») y de infracción
  sanitaria («productos caducados»). Afirmarlas sin sentencia puede ser calumnia
  (art. 205 CP) y, en el caso sanitario, provocarle una inspección al negocio.
- **Juicios duros sobre personas identificables.** En un local con una sola
  persona tras el mostrador, «la dependienta es antipática» identifica a alguien
  concreto aunque no se dé el nombre: art. 7.7 de la LO 1/1982.
- **Reseñas entrecomilladas.** Las comillas delatan que el texto se copió de
  algún sitio. Las citas cortas pierden solo las comillas y las palabras se
  integran en la frase; las de más de 60 caracteres se eliminan con su frase.

Lo que **no** hace, deliberadamente: reescribir. Un primer intento sustituía
términos con expresiones regulares y producía castellano roto («resulta un trato
poco cordial, seca y con un trato distante») además de destrozar usos neutros
(«prevenir el fraude» → «prevenir el discrepancias sobre el servicio prestado»).
Eliminar una frase de un texto de 745 palabras siempre da resultado gramatical;
reescribirla automáticamente, casi nunca.

Tampoco antepone «según opiniones de clientes» de forma automática: la detección
capturaba «bebidas frías», «frutos secos» y «la ausencia de quejas».

El informe de cambios queda en `data/informe-riesgo.json`, con la URL de cada
ficha tocada por si quieres revisarlas a mano.

## Páginas de localidad

Las 803 páginas de localidad son el punto débil estructural del directorio: un
párrafo de plantilla con el nombre intercambiado es el patrón que mejor detectan
los sistemas de contenido útil de Google. Aquí no hay reseñas de las que sacar
variación natural, como sí ocurre en las fichas.

La distribución obliga a segmentar: **el 55 % de las localidades tiene un único
establecimiento** y solo el 4 % tiene 15 o más. Un mismo tratamiento para las 803
no funciona.

### Qué diferencia cada página

`pipeline/agregar_ciudades.py` calcula, por localidad, datos que ninguna otra
reproduce igual: reparto por tipo, franja de mayor y menor afluencia, cuántos
abren domingo, cuántos tienen jornada partida, atributos de pago y accesibilidad
por encima del 25 % de cobertura, códigos postales y localidades vecinas con más
oferta en 35 km.

De ahí salen tres bloques, todos con datos reales y ninguno redactado:

- **Ficha resumen** (`ResumenCiudad.tsx`): las cifras de cabecera.
- **Preguntas frecuentes** (`PreguntasCiudad.tsx`): hasta 8 preguntas construidas
  desde los recuentos, con marcado `FAQPage`. Es lo que ataca el long-tail donde
  el pack de Maps no compite: «locutorio abierto domingo en X», «que acepte
  tarjeta en X», «a qué hora hay menos cola».
- **Enlazado a localidades vecinas**: reparte autoridad en horizontal, sin pasar
  por la provincia, que va con `noindex`.

### Texto redactado, solo donde compensa

```bash
python3 pipeline/agregar_ciudades.py ./data
python3 pipeline/generar_prompts_ciudad.py ./data --minimo 5
```

Genera un prompt por localidad con **5 o más establecimientos**: 121 localidades
que cubren el 65 % de las fichas del directorio. Cada prompt lleva incrustados los
datos reales de esa localidad y prohíbe explícitamente inventar horarios,
comisiones u operadores.

Las respuestas se guardan en `data/textos-ciudad.json`:

```json
{ "madrid/getafe": "El texto devuelto en markdown…" }
```

El fichero es opcional y la página funciona sin él. Las localidades sin texto se
sostienen con los datos agregados y las preguntas, que ya las diferencian.

**Ya hay 20 textos escritos**, los de las localidades más grandes, que cubren
1.116 de las 3.050 fichas (37 % del directorio). Están en
`pipeline/escribir_textos_ciudad.py` y se vuelcan con:

```bash
python3 pipeline/escribir_textos_ciudad.py ./data
```

El script conserva lo que ya hubiera en `textos-ciudad.json`, así que se puede
ejecutar tantas veces como haga falta sin perder textos añadidos a mano.

Cada uno parte del rasgo que distingue a esa localidad en los datos, y por eso
no se parecen entre sí: Granada es la única capital cuyo hueco de actividad cae
de 15:00 a 17:00 y no por la mañana; Murcia tiene el pico más tardío del país
(19:00 a 22:00); Torrevieja es la única con punta de mañana; en Cartagena los
puntos de envío triplican a los locutorios, al revés que en el resto; en Lorca
los 14 establecimientos con datos abren en domingo, sin excepción; y Gijón tiene
la jornada partida casi generalizada, 8 de 9.

Todas las cifras citadas en los textos se han contrastado una a una contra
`agregados-ciudad.json`. Si regeneras los datos y cambian los recuentos, hay que
revisarlos: un texto que contradiga a la tabla que tiene al lado hace más daño
que no tener texto.

### Sobre las keywords

«Locutorios cerca de mí» es prácticamente inalcanzable en orgánico: la resuelve
el pack de Maps y el orgánico apenas recibe clic. La consulta ganable es
«locutorios en [ciudad]» y, sobre todo, el long-tail al que responden las
preguntas frecuentes.

## Seguridad de dependencias

El proyecto va en **Next.js 15.5.21**, la versión de mantenimiento LTS de la
línea 15.5, con **React 19.2.3**. No usar una versión anterior: toda la rama 15.x
por debajo de 15.5.7 arrastra CVE-2025-66478, un RCE con CVSS 10.0 en el
protocolo de React Server Components que afecta al App Router. Las versiones
posteriores corrigen además CVE-2025-55183 y CVE-2025-55184.

`package.json` incluye dos `overrides`:

```json
"overrides": { "sharp": "^0.35.0", "postcss": "^8.5.23" }
```

Ninguno de los dos afecta al funcionamiento del sitio. `sharp` entra como
dependencia opcional de la optimización de imágenes de Next, que aquí no se usa
(las ilustraciones van con `<img>` plano). `postcss` solo interviene en
compilación y sus fallos requieren CSS controlado por un atacante, cosa
imposible cuando todo el CSS es propio. Se fijan igualmente para que
`npm audit` quede en cero y no haya ruido que enmascare un aviso real.

Next.js publica ahora **parches de seguridad mensuales**. Conviene revisar
`nextjs.org/blog` de vez en cuando y subir dentro de la línea 15.5, que no trae
cambios incompatibles. Saltar a la 16.x sí es un cambio mayor y no urge.

## Pendiente

- **Aviso legal y privacidad.** Los textos están redactados pero tienen campos
  entre corchetes: identificación del titular, NIF y domicilio. La LSSI lo exige
  antes de publicar.
- **Fuentes.** Se cargan por `<link>` a Google Fonts porque el entorno donde se
  generó el proyecto no tenía salida a `fonts.googleapis.com`. En Vercel sí la
  hay: migrar a `next/font/google` las autoaloja y elimina el FOUT y una
  conexión externa. Es la mejora de rendimiento más barata que queda.
- **Analítica.** No hay ninguna. Al añadirla habrá que revisar
  `/privacidad` y valorar un banner de consentimiento.
