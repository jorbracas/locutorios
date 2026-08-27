# Revisión y reconstrucción de textos de ciudad

## Situación recibida

La actualización contenía 30 textos para una selección prevista de 123
localidades. Faltaban 93. No era seguro incorporar los 30 existentes:

- Valencia y Murcia incluían notas internas y rutas de archivos dentro del
  texto público.
- Barcelona seguía usando cifras anteriores: 85 establecimientos en lugar de
  83, 25 códigos postales en lugar de 24, una muestra de 37 en lugar de 35 y
  otros recuentos desactualizados.
- Varios textos añadían barrios, medios de transporte, perfiles de clientela y
  explicaciones causales que no aparecían en los datos suministrados.
- La actividad de `popular_times` se convertía en apertura dominical, cierre al
  mediodía u horario continuo. Una curva de afluencia no permite afirmar eso.
- El ejemplo incluido en todos los prompts ya contenía geografía urbana no
  suministrada; el modelo imitaba ese patrón pese a la prohibición de inventar.
- `escribir_textos_ciudad.py` solo conocía 20 textos. Una regeneración posterior
  habría eliminado los diez nuevos.
- `package-lock.json` no estaba sincronizado con los overrides de
  `package.json`, por lo que `npm ci` fallaba antes de compilar.

## Cambios aplicados

1. `pipeline/escribir_textos_ciudad.py` genera de forma reproducible los 123
   textos desde `agregados-ciudad.json`. No llama a una API y no usa conocimiento
   externo.
2. Cada texto queda entre 180 y 240 palabras, contiene un H2 con el nombre de la
   localidad y utiliza únicamente recuentos, afluencia, atributos y localidades
   cercanas permitidos.
3. `pipeline/validar_textos_ciudad.py` comprueba cobertura, longitud, cifras,
   conceptos obligatorios, residuos internos, lenguaje de scrapeo, geografía no
   suministrada y duplicados exactos.
4. `pipeline/generar_prompts_ciudad.py` conserva una vía opcional para
   reescritura editorial, pero sin el ejemplo contaminante y con prohibiciones
   explícitas contra apertura/cierre inferidos, barrios, causas y servicios no
   confirmados.
5. La interfaz ya no muestra “abren en domingo” ni “cierran al mediodía”. Ahora
   habla de actividad observada y caída de afluencia. Las preguntas sobre pago,
   accesibilidad y envío tampoco interpretan la ausencia de un atributo como una
   negativa.
6. Se actualizó el lockfile para que la instalación limpia sea reproducible.

## Resultado verificado

- 123 de 123 localidades incluidas.
- 2.011 de 3.050 establecimientos cubiertos por texto de ciudad.
- Longitud entre 180 y 222 palabras; media de 202,9.
- 0 cifras no autorizadas.
- 0 notas o rutas internas filtradas.
- 0 duplicados exactos y 0 estructuras completas idénticas tras normalización.
- Validador de ciudades: `PASS`.
- TypeScript: `PASS`.
- Build de producción: `PASS`, 3.897 páginas estáticas.
- Auditoría de dependencias: 0 vulnerabilidades.

## Uso

```bash
npm ci
npm run cities
npm run validate:cities
npm run typecheck
npm run build
```

## Límite real del resultado

Estos 123 textos son redacción controlada y basada en datos, no 123 artículos
investigados y escritos de forma independiente. Eliminan el riesgo de publicar
hechos inventados y se actualizan cuando cambian los agregados, pero no crean por
sí solos autoridad, enlaces ni información local exclusiva. Si se busca una
diferenciación editorial mayor, conviene reescribir manualmente las localidades
con demanda real y pasar después el mismo validador; producir más prosa automática
sin nuevas fuentes no soluciona un problema de indexación.
