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

## Saneamiento de datos y textos

Dos scripts, **en este orden**, cada vez que se regeneren los datos desde el CSV:

```bash
python3 pipeline/build_data.py /ruta/al/locutorios.csv ./data
python3 pipeline/sanear_geografia.py ./data     # 1. geografía
python3 pipeline/depurar_textos.py ./data       # 2. textos
python3 pipeline/agregar_ciudades.py ./data     # 3. agregados
python3 pipeline/escribir_textos_ciudad.py ./data
```

Ambos aceptan `--simular` para ver el efecto sin escribir.

### 1. Geografía

El origen trae fichas mal ubicadas, y eso genera páginas de localidad enteras en
sitios equivocados. En España los dos primeros dígitos del código postal fijan la
provincia sin ambigüedad, así que sirven de verificación objetiva.

Corrige 1 provincia errónea (un MoneyGram de Vitoria catalogado en Bizkaia, cuando
Vitoria es Álava) y funde 16 localidades fantasma. La más llamativa: un locutorio
con CP 28018 y dirección en Puente de Vallecas estaba catalogado en Fuengirola,
porque la dirección de Google ya venía corrupta («28018 Fuengirola, Madrid»).
Creaba una página `/madrid/fuengirola` inexistente, además de la Fuengirola real
de Málaga.

También unifica los slugs con artículo pospuesto (`hospitalet-de-llobregat-l` →
`l-hospitalet-de-llobregat`), que de otro modo publican dos páginas compitiendo.

La fusión automática solo se aplica cuando la localidad de origen es residual (2
fichas o menos) y la de destino la triplica. No toda discrepancia es un error:
Lejona y Leioa son la misma localidad en dos idiomas, Puente Tocinos es una
pedanía de Murcia y Vecindario pertenece a Santa Lucía de Tirajana. Esos 26 casos
quedan anotados en `data/informe-geografia.json` para revisión manual, sin tocar.

### 2. Textos

Cuatro niveles, **todos por eliminación de frase completa**. Ninguno reescribe:
un intento anterior con sustituciones producía castellano roto y destrozaba usos
neutros.

- **Acusaciones graves** (99 frases): robo, acoso, racismo, amenazas, plagas,
  móviles robados, retención de fondos. Un directorio no tiene por qué arbitrar
  una acusación penal porque alguien la escribiera en una reseña, y las
  coletillas de «no verificado» o «de ser cierto» no protegen: la imputación ya
  está publicada y el negocio sigue siendo identificable.
- **Juicios duros sobre personas identificables**: art. 7.7 de la LO 1/1982.
- **Especulación** (4.818 frases + 883 secciones enteras): «es probable que
  cuente con fax», «es común que dispongan de cabinas». Si no sabemos que tiene
  fax, hablar del fax no aporta; añadir después que no está confirmado no arregla
  nada, porque el lector ya lo ha leído. Se eliminan también los encabezados
  especulativos («¿Qué servicios podría ofrecer un locutorio como este?») junto
  con la sección que introducen.
- **Relleno de entorno** (1.299 frases): «de fácil acceso», «tráfico moderado»,
  «a pocos minutos del centro». No procede de ningún dato calculado.

Resultado: 2.737 fichas tocadas, media de 106 palabras eliminadas. La media del
corpus baja de 745 a 707 palabras y el mínimo queda en 205. Quince fichas bajan
de 300 palabras, y son precisamente las que apenas tenían otra cosa que
especulación.

#### Falsos positivos que hubo que acotar

El vocabulario se solapa con usos inocentes, y todos estos aparecieron de verdad
en el corpus:

- «el servicio más **demandado**» no es una demanda judicial.
- «prevenir el **fraude**», «normativa de **blanqueo**» es lenguaje regulatorio.
- «las fricciones son **menores**» es un adjetivo, no un menor de edad.
- «**estafeta**» es una oficina de correos.
- «citas para extranjería, **policía**, DNI» es un servicio del propio local.

Por eso el detector lleva una lista de contextos neutros que desactivan la
coincidencia. Conviene mantenerla si se amplían los patrones.

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

## Saneamiento de geografía

`pipeline/sanear_geografia.py` corrige errores de ubicación del origen, que no
son cosméticos: generan páginas de localidad enteras en sitios equivocados.

En España los dos primeros dígitos del código postal determinan la provincia sin
ambigüedad, y eso da una verificación objetiva. Para la ciudad se usa una
heurística: si un CP concentra sus fichas en una localidad y aparece una suelta
en otra, la suelta casi siempre está mal.

Corrigió un error de provincia (un MoneyGram de Vitoria-Gasteiz catalogado en
Bizkaia, siendo Álava) y fusionó 17 localidades fantasma. Entre ellas, un
`madrid/fuengirola` creado por una ficha con CP 28018 y dirección en Puente de
Vallecas: la dirección que venía de Google ya estaba corrupta. El total pasa de
803 localidades a 787.

No fusiona a ciegas: `lejona` y `leioa` son la misma localidad en castellano y
euskera, Puente Tocinos es una pedanía de Murcia y Vecindario pertenece a Santa
Lucía de Tirajana. La fusión automática solo actúa cuando la localidad de origen
es residual y la de destino la triplica; las 26 restantes quedan anotadas en
`data/informe-geografia.json` para revisión manual.

### El código postal no siempre es de fiar

`sanear_geografia.py` valida la provincia con el CP, que en España la determina
sin ambigüedad. Pero da por bueno el propio CP, y ahí tiene un punto ciego.

Lo destapó India Post: figuraba en La Adrada con CP 05430, que es efectivamente
de La Adrada, así que la validación no protestó. Sus coordenadas, en cambio,
caen a 0,5 km del casco de Sotillo de la Adrada y a 3,6 km del de La Adrada, y
la calle Carmen Rodríguez está en el callejero de Sotillo, cuyo CP es 05420. El
dato erróneo era el código postal.

De ahí `corregir_localidades.py`, que hace dos cosas: aplica correcciones
verificadas una a una, y audita todas las fichas comparando su posición con el
centroide de su localidad. Cuando el CP y las coordenadas discrepan, mandan las
coordenadas: un CP se teclea mal, una latitud viene del propio mapa.

Corrigió cuatro casos (India Post, un Money Exchange asignado a Vitoria estando
en Laudio/Llodio, un Locutorio de Montornès puesto en Barcelona y un locutorio
de La Pobla de Farnals puesto en València) y dejó 28 discrepancias en
`data/informe-localidades.json` para revisión manual. Varias de esas 28 no son
errores: Casetas es un barrio de Zaragoza y Beniaján una pedanía de Murcia, así
que no se tocan sin comprobarlas.

**Orden obligatorio** al regenerar desde el CSV:

```bash
python3 pipeline/build_data.py /ruta/al.csv ./data
python3 pipeline/sanear_geografia.py ./data
python3 pipeline/corregir_localidades.py ./data
python3 pipeline/depurar_textos.py ./data
python3 pipeline/corregir_fichas.py ./data
python3 pipeline/ampliar_fichas.py ./data
python3 pipeline/correccion_final.py ./data
python3 pipeline/agregar_ciudades.py ./data
python3 pipeline/escribir_textos_ciudad.py ./data
```

## Pasada final de control (verificación contra disco, no contra informes)

Esta pasada partió de una regla estricta: verificar el contenido *final* en
disco, no confiar en los recuentos de informes anteriores. Encontró y corrigió
problemas reales que las pasadas previas habían dejado sin resolver:

- **8 acusaciones graves adicionales** no cubiertas antes: "gesto machista" y
  "destratada" en Akash (una anécdota completa que había pasado inadvertida),
  "trato machista" en Locutorio Oliva, "sensación/sentimiento/intento de
  engaño" en tres fichas más, y un párrafo huérfano en Locutorio DG donde la
  respuesta del propietario a una crítica ya eliminada había quedado sin
  sentido.
- **129 casos de concordancia rota** (`información divididas`, `información
  encontradas`, `la información son mixtas`) — un fallo sistémico del dataset
  original, no introducido por ninguna pasada de este proyecto. Se resolvió
  sustituyendo "información" por "opiniones", que además de corregir la
  concordancia es la expresión idiomática natural para lo que la frase
  pretendía decir.
- **56 + 43 fragmentos de texto realmente mutilado**, causados por un fallo en
  mi propia función `limpiar_meta` de una pasada anterior: una expresión
  regular sin límite de palabra que convertía "20 años **de** experiencia" en
  "20 años **d.**", y una segunda variante que dejaba "Conoce su oferta**.de**
  quienes lo han utilizado." Reparado con precisión matemática: solo se toca
  un campo cuando el texto actual coincide *exactamente* con lo que el fallo
  habría producido sobre el original, nunca por sustitución a ciegas.
- **13 encabezados y 4 metas** con "advertencias/carencias/contradicciones",
  que el filtro de la pasada anterior no cubría (solo buscaba
  "controversia/sospecha/punto débil").

### Verificación programática final (tras el build, releída de disco)

```json
{
  "acusaciones_problematicas_restantes": 0,
  "criticas_operativas_conservadas": 2332,
  "errores_gramaticales_restantes": 0,
  "texto_mutilado_restante": 0,
  "nombres_de_reviews_restantes": 0,
  "headings_problematicos_restantes": 0,
  "metas_problematicas_restantes": 0,
  "urls_duplicadas": 0,
  "atributos_duplicados": 0,
  "encabezados_vacios": 0,
  "unknown_indexable": false,
  "unknown_en_sitemap": false
}
```

El fichero completo, con las 817 fichas modificadas y los dos casos que
quedan para revisión manual (26 discrepancias geográficas que podrían ser
barrios/pedanías legítimos, y las 413 fichas cortas por falta de datos), está
en `data/CONTROL-FINAL.json`.

## Revisión final: geografía, redirects y sitemap

Pasada quirúrgica sobre el estado actual (no una reescritura). Verificó cada
caso contra los propios datos antes de mover nada, distinguiendo error real
de falso positivo por proximidad de centroide.

**15 fichas movidas**, cada una con justificación verificable: 9 por código
postal que no coincidía con la localidad asignada (confirmados dos con fuente
externa: CP 17190 = Salt, CP 12006 = Castellón de la Plana), y 6 por
normalización de denominación (Lejona/Leioa, Santa Eulalia del Río/Santa
Eulària des Riu, dos duplicados de "Castellón" y "Alcossebre").

**10 casos quedaron explícitamente sin tocar** por ser falsos positivos del
detector de proximidad — incluido uno nuevo encontrado en esta pasada:
"Locutorio Internacional Barajas" seguía en Madrid pese a que el detector
proponía Paracuellos de Jarama por cercanía de centroide; el propio nombre
comercial confirma que el distrito de Barajas es Madrid capital.

**24 casos van a revisión manual**, sin cambios: 2 canarios (Click
World/ELEWUACUBA, donde Maspalomas/Vecindario dependen del nivel
administrativo usado) y 22 discrepancias nuevas detectadas al regenerar el
informe geográfico desde cero, la mayoría distritos del área metropolitana de
Barcelona cuya posición cae cerca de un municipio vecino sin que eso implique
error — exactamente el patrón de falso positivo que advertía el encargo.

### Redirects

`next.config.mjs` incorpora 21 redirects permanentes (308), verificados sin
cadenas (A→B→C siempre resuelve en un salto) y contrastados contra
`.next/routes-manifest.json` tras el build. Cubren tanto las fichas movidas
como las 6 páginas de ciudad que se quedaron sin fichas.

### Sitemap

`sitemap.ts` ya no usa `new Date()` como `lastModified`: el dataset no tiene
fecha real de modificación por ficha, así que el campo se omite en vez de
inventarse. Generar el sitio no significa que las 3.050 fichas hayan
cambiado ese día.

### Metadatos duplicados

7 pares de `metaTitulo` idénticos y 1 par de `metaDescripcion` idéntica,
diferenciados por calle o número sin inventar servicios. Verificado en 0
tras el build.

### Datos derivados

`geo.json`, `agregados-ciudad.json` y los dos textos editoriales que citaban
cifras ahora desactualizadas (Murcia: 39→37 establecimientos; Valencia:
99→96) se regeneraron para reflejar la geografía movida. El resto de las
localidades quedó intacto.

**Informe completo**: `data/INFORME-REVISION-GEO-SEO.json`.

## Dominio de producción: www

Vercel tiene configurado `www.locutorioscercademi.com` como dominio de
producción, con el apex (`locutorioscercademi.com`) haciendo un redirect 308
permanente hacia él. `SITIO.dominio` en `src/lib/seo.ts` es la única fuente
de verdad para esto — de ahí salen `metadataBase`, el `canonical` de cada
página, las 3.836 URLs del sitemap, el `Host` de `robots.txt` y el `url` del
JSON-LD. Si el dominio de producción cambia otra vez, ese es el único sitio
que hay que tocar.

Antes de este ajuste, todo apuntaba al apex sin `www`, lo que habría obligado
a un salto de redirección extra en cada URL del sitemap al rastrear, y
generado una inconsistencia entre la URL declarada canónica y la que
realmente sirve el contenido sin redirigir.

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
