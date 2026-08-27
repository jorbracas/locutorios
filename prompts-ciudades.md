# Prompts de redacción por localidad

123 localidades con 5 o más establecimientos, ordenadas de mayor a menor.

Pega cada bloque en el modelo, y guarda la respuesta en `data/textos-ciudad.json` con la clave que aparece en el título:

```json
{
  "madrid/getafe": "El texto devuelto…"
}
```

---

### Madrid (Madrid) — `madrid/madrid`

```
Escribe un texto de 180 a 240 palabras para la página de Madrid de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MADRID (no uses ningún otro):
- Total de establecimientos: 272
- Reparto: 178 locutorios, 57 especializados en envío de dinero, 37 comercios con servicios relacionados
- Códigos postales: 42
- Con teléfono publicado: 231
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 148 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 129 de 148
- Con caída de actividad al mediodía, sin afirmar cierre: 44 de 148
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 141 de 272
- Localidades cercanas con oferta: Parla (20 establecimientos, a 20.2 km), Alcorcón (18 establecimientos, a 13.6 km), Leganés (15 establecimientos, a 10.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Madrid".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Madrid.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Madrid encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Valencia (Valencia) — `valencia/valencia`

```
Escribe un texto de 180 a 240 palabras para la página de Valencia de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VALENCIA (no uses ningún otro):
- Total de establecimientos: 96
- Reparto: 46 locutorios, 27 especializados en envío de dinero, 23 comercios con servicios relacionados
- Códigos postales: 18
- Con teléfono publicado: 71
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 44 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 39 de 44
- Con caída de actividad al mediodía, sin afirmar cierre: 16 de 44
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 63 de 96
- Localidades cercanas con oferta: Mislata (6 establecimientos, a 3.6 km), Torrent (4 establecimientos, a 9.2 km), Burjassot (3 establecimientos, a 5.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Valencia".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Valencia.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Valencia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Zaragoza (Zaragoza) — `zaragoza/zaragoza`

```
Escribe un texto de 180 a 240 palabras para la página de Zaragoza de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ZARAGOZA (no uses ningún otro):
- Total de establecimientos: 87
- Reparto: 38 locutorios, 28 especializados en envío de dinero, 21 comercios con servicios relacionados
- Códigos postales: 14
- Con teléfono publicado: 69
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 38 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 35 de 38
- Con caída de actividad al mediodía, sin afirmar cierre: 9 de 38
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 29 de 87
- Localidades cercanas con oferta: Utebo (1 establecimientos, a 10.7 km), Zuera (1 establecimientos, a 25.8 km), Pedrola (1 establecimientos, a 31.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Zaragoza".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Zaragoza.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Zaragoza encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Barcelona (Barcelona) — `barcelona/barcelona`

```
Escribe un texto de 180 a 240 palabras para la página de Barcelona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BARCELONA (no uses ningún otro):
- Total de establecimientos: 83
- Reparto: 52 locutorios, 20 especializados en envío de dinero, 11 comercios con servicios relacionados
- Códigos postales: 24
- Con teléfono publicado: 70
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 35 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 32 de 35
- Con caída de actividad al mediodía, sin afirmar cierre: 18 de 35
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 25 de 83
- Localidades cercanas con oferta: L'Hospitalet de Llobregat (38 establecimientos, a 6.4 km), Santa Coloma de Gramenet (15 establecimientos, a 5.8 km), Badalona (12 establecimientos, a 6.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Barcelona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Barcelona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Barcelona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Sevilla (Sevilla) — `sevilla/sevilla`

```
Escribe un texto de 180 a 240 palabras para la página de Sevilla de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SEVILLA (no uses ningún otro):
- Total de establecimientos: 70
- Reparto: 28 locutorios, 24 especializados en envío de dinero, 18 comercios con servicios relacionados
- Códigos postales: 12
- Con teléfono publicado: 53
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 24 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 23 de 24
- Con caída de actividad al mediodía, sin afirmar cierre: 9 de 24
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 44 de 70
- Localidades cercanas con oferta: San Juan de Aznalfarache (5 establecimientos, a 6.4 km), Castilleja de la Cuesta (3 establecimientos, a 7.4 km), Camas (2 establecimientos, a 5.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Sevilla".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Sevilla.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Sevilla encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Bilbao (Bizkaia) — `bizkaia/bilbao`

```
Escribe un texto de 180 a 240 palabras para la página de Bilbao de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BILBAO (no uses ningún otro):
- Total de establecimientos: 67
- Reparto: 42 locutorios, 18 especializados en envío de dinero, 7 comercios con servicios relacionados
- Códigos postales: 13
- Con teléfono publicado: 57
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 30 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 28 de 30
- Con caída de actividad al mediodía, sin afirmar cierre: 18 de 30
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 20 de 67
- Localidades cercanas con oferta: San Vicente de Barakaldo (12 establecimientos, a 5.8 km), Algorta (5 establecimientos, a 11.9 km), Leioa (4 establecimientos, a 8.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Bilbao".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Bilbao.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Bilbao encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Palma (Illes Balears) — `illes-balears/palma`

```
Escribe un texto de 180 a 240 palabras para la página de Palma de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE PALMA (no uses ningún otro):
- Total de establecimientos: 57
- Reparto: 26 locutorios, 17 especializados en envío de dinero, 14 comercios con servicios relacionados
- Códigos postales: 12
- Con teléfono publicado: 44
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 37 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 36 de 37
- Con caída de actividad al mediodía, sin afirmar cierre: 17 de 37
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 15 de 57
- Localidades cercanas con oferta: Inca (5 establecimientos, a 27.1 km), Sóller (2 establecimientos, a 22.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Palma".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Palma.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Palma encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Granada (Granada) — `granada/granada`

```
Escribe un texto de 180 a 240 palabras para la página de Granada de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GRANADA (no uses ningún otro):
- Total de establecimientos: 40
- Reparto: 20 locutorios, 8 especializados en envío de dinero, 12 comercios con servicios relacionados
- Códigos postales: 14
- Con teléfono publicado: 23
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 12 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 8 de 12
- Con caída de actividad al mediodía, sin afirmar cierre: 10 de 12
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 12 de 40
- Localidades cercanas con oferta: Armilla (2 establecimientos, a 4.1 km), Maracena (1 establecimientos, a 4.1 km), Churriana de la Vega (1 establecimientos, a 5.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Granada".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Granada.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Granada encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alicante (Alicante) — `alicante/alicante`

```
Escribe un texto de 180 a 240 palabras para la página de Alicante de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALICANTE (no uses ningún otro):
- Total de establecimientos: 38
- Reparto: 18 locutorios, 11 especializados en envío de dinero, 9 comercios con servicios relacionados
- Códigos postales: 12
- Con teléfono publicado: 27
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 14 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 14
- Con caída de actividad al mediodía, sin afirmar cierre: 4 de 14
- Atributo publicable sin compararlo con una media: Visita rápida — 10 de 38
- Localidades cercanas con oferta: Elche (15 establecimientos, a 21.6 km), Villajoyosa (5 establecimientos, a 27.4 km), Elda (3 establecimientos, a 29.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alicante".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Alicante.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alicante encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### L'Hospitalet de Llobregat (Barcelona) — `barcelona/l-hospitalet-de-llobregat`

```
Escribe un texto de 180 a 240 palabras para la página de L'Hospitalet de Llobregat de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE L'HOSPITALET DE LLOBREGAT (no uses ningún otro):
- Total de establecimientos: 38
- Reparto: 24 locutorios, 7 especializados en envío de dinero, 7 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 30
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 17 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 16 de 17
- Con caída de actividad al mediodía, sin afirmar cierre: 9 de 17
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 11 de 38
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 6.4 km), Santa Coloma de Gramenet (15 establecimientos, a 12.2 km), Badalona (12 establecimientos, a 12.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en L'Hospitalet de Llobregat".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de L'Hospitalet de Llobregat.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En L'Hospitalet de Llobregat encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Vitoria-Gasteiz (Araba/Álava) — `araba-alava/vitoria-gasteiz`

```
Escribe un texto de 180 a 240 palabras para la página de Vitoria-Gasteiz de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VITORIA-GASTEIZ (no uses ningún otro):
- Total de establecimientos: 37
- Reparto: 22 locutorios, 8 especializados en envío de dinero, 7 comercios con servicios relacionados
- Códigos postales: 9
- Con teléfono publicado: 33
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 20 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 19 de 20
- Con caída de actividad al mediodía, sin afirmar cierre: 10 de 20
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 11 de 37
- Localidades cercanas con oferta: Miranda de Ebro (4 establecimientos, a 28.6 km), Arrasate / Mondragón (2 establecimientos, a 27.9 km), Haro (2 establecimientos, a 34.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vitoria-Gasteiz".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Vitoria-Gasteiz.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Vitoria-Gasteiz encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Murcia (Murcia) — `murcia/murcia`

```
Escribe un texto de 180 a 240 palabras para la página de Murcia de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MURCIA (no uses ningún otro):
- Total de establecimientos: 37
- Reparto: 14 locutorios, 13 especializados en envío de dinero, 10 comercios con servicios relacionados
- Códigos postales: 10
- Con teléfono publicado: 28
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 11 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 10 de 11
- Con caída de actividad al mediodía, sin afirmar cierre: 6 de 11
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 12 de 37
- Localidades cercanas con oferta: Molina de Segura (8 establecimientos, a 10.4 km), Archena (6 establecimientos, a 20.7 km), Orihuela (4 establecimientos, a 19.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Murcia".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Murcia.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Murcia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Pamplona (Navarra) — `navarra/pamplona`

```
Escribe un texto de 180 a 240 palabras para la página de Pamplona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE PAMPLONA (no uses ningún otro):
- Total de establecimientos: 33
- Reparto: 15 locutorios, 10 especializados en envío de dinero, 8 comercios con servicios relacionados
- Códigos postales: 10
- Con teléfono publicado: 27
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 13 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 13
- Con caída de actividad al mediodía, sin afirmar cierre: 9 de 13
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 10 de 33
- Localidades cercanas con oferta: Barañáin (8 establecimientos, a 2.9 km), Tafalla (3 establecimientos, a 32.2 km), Burlada (2 establecimientos, a 2.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Pamplona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Pamplona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Pamplona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Málaga (Malaga) — `malaga/malaga`

```
Escribe un texto de 180 a 240 palabras para la página de Málaga de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MÁLAGA (no uses ningún otro):
- Total de establecimientos: 30
- Reparto: 22 locutorios, 4 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales: 13
- Con teléfono publicado: 25
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 11 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 11
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 11
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 16 de 30
- Localidades cercanas con oferta: Fuengirola (6 establecimientos, a 25.4 km), Torremolinos (4 establecimientos, a 11.7 km), Las Lagunas de Mijas (3 establecimientos, a 26.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Málaga".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Málaga.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Málaga encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Lorca (Murcia) — `murcia/lorca`

```
Escribe un texto de 180 a 240 palabras para la página de Lorca de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LORCA (no uses ningún otro):
- Total de establecimientos: 26
- Reparto: 13 locutorios, 5 especializados en envío de dinero, 8 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 20
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 14 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 14 de 14
- Con caída de actividad al mediodía, sin afirmar cierre: 6 de 14
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 7 de 26
- Localidades cercanas con oferta: Totana (6 establecimientos, a 20.1 km), Águilas (5 establecimientos, a 31.3 km), Pulpí (3 establecimientos, a 29.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lorca".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Lorca.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Lorca encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Oviedo (Asturias) — `asturias/oviedo`

```
Escribe un texto de 180 a 240 palabras para la página de Oviedo de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE OVIEDO (no uses ningún otro):
- Total de establecimientos: 23
- Reparto: 12 locutorios, 6 especializados en envío de dinero, 5 comercios con servicios relacionados
- Códigos postales: 7
- Con teléfono publicado: 20
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 13 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 13
- Con caída de actividad al mediodía, sin afirmar cierre: 5 de 13
- Atributo publicable sin compararlo con una media: Visita rápida — 11 de 23
- Localidades cercanas con oferta: Gijón (20 establecimientos, a 23.1 km), Mieres (2 establecimientos, a 14.2 km), Langreo (2 establecimientos, a 15.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Oviedo".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Oviedo.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Oviedo encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Torrevieja (Alicante) — `alicante/torrevieja`

```
Escribe un texto de 180 a 240 palabras para la página de Torrevieja de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TORREVIEJA (no uses ningún otro):
- Total de establecimientos: 21
- Reparto: 12 locutorios, 8 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 19
- Franja de mayor afluencia: 10:00 a 13:00 (estimación sobre 8 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 6 de 8
- Con caída de actividad al mediodía, sin afirmar cierre: 6 de 8
- Atributo publicable sin compararlo con una media: Visita rápida — 6 de 21
- Localidades cercanas con oferta: Elche (15 establecimientos, a 32.3 km), Callosa de Segura (4 establecimientos, a 23.8 km), Orihuela (4 establecimientos, a 26.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrevieja".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Torrevieja.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Torrevieja encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Cartagena (Murcia) — `murcia/cartagena`

```
Escribe un texto de 180 a 240 palabras para la página de Cartagena de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CARTAGENA (no uses ningún otro):
- Total de establecimientos: 21
- Reparto: 4 locutorios, 12 especializados en envío de dinero, 5 comercios con servicios relacionados
- Códigos postales: 7
- Con teléfono publicado: 17
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 4
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 8 de 21
- Localidades cercanas con oferta: Los Alcázares (3 establecimientos, a 18.5 km), Fuente Alamo (3 establecimientos, a 20.1 km), Puerto de Mazarrón (3 establecimientos, a 24.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cartagena".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Cartagena.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Cartagena encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Gijón (Asturias) — `asturias/gijon`

```
Escribe un texto de 180 a 240 palabras para la página de Gijón de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GIJÓN (no uses ningún otro):
- Total de establecimientos: 20
- Reparto: 15 locutorios, 1 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales: 7
- Con teléfono publicado: 18
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 9 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 9
- Con caída de actividad al mediodía, sin afirmar cierre: 8 de 9
- Atributo publicable sin compararlo con una media: Visita rápida — 14 de 20
- Localidades cercanas con oferta: Oviedo (23 establecimientos, a 23.1 km), Avilés (2 establecimientos, a 20.3 km), Langreo (2 establecimientos, a 26.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Gijón".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Gijón.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Gijón encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Arrecife (Las Palmas) — `las-palmas/arrecife`

```
Escribe un texto de 180 a 240 palabras para la página de Arrecife de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ARRECIFE (no uses ningún otro):
- Total de establecimientos: 20
- Reparto: 11 locutorios, 2 especializados en envío de dinero, 7 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 16
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 15 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 13 de 15
- Con caída de actividad al mediodía, sin afirmar cierre: 10 de 15
- Atributo publicable sin compararlo con una media: Visita rápida — 11 de 20
- Localidades cercanas con oferta: Puerto del Carmen (1 establecimientos, a 10.9 km), Playa Blanca (1 establecimientos, a 29.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Arrecife".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Arrecife.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Arrecife encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Parla (Madrid) — `madrid/parla`

```
Escribe un texto de 180 a 240 palabras para la página de Parla de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE PARLA (no uses ningún otro):
- Total de establecimientos: 20
- Reparto: 9 locutorios, 5 especializados en envío de dinero, 6 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 15
- Franja de mayor afluencia: 11:00 a 14:00 (estimación sobre 10 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 10 de 10
- Con caída de actividad al mediodía, sin afirmar cierre: 5 de 10
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 6 de 20
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 20.2 km), Alcorcón (18 establecimientos, a 13.0 km), Getafe (15 establecimientos, a 8.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Parla".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Parla.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Parla encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Gandia (Valencia) — `valencia/gandia`

```
Escribe un texto de 180 a 240 palabras para la página de Gandia de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GANDIA (no uses ningún otro):
- Total de establecimientos: 20
- Reparto: 7 locutorios, 4 especializados en envío de dinero, 9 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 15
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 11 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 11
- Con caída de actividad al mediodía, sin afirmar cierre: 5 de 11
- Atributo publicable sin compararlo con una media: Visita rápida — 6 de 20
- Localidades cercanas con oferta: Alzira (5 establecimientos, a 29.4 km), Dénia (4 establecimientos, a 28.9 km), Xàtiva (4 establecimientos, a 29.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Gandia".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Gandia.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Gandia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Lleida (Lleida) — `lleida/lleida`

```
Escribe un texto de 180 a 240 palabras para la página de Lleida de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LLEIDA (no uses ningún otro):
- Total de establecimientos: 18
- Reparto: 12 locutorios, 5 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 8
- Con teléfono publicado: 12
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 5
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 12 de 18
- Localidades cercanas con oferta: Balaguer (4 establecimientos, a 24.3 km), Alcarràs (2 establecimientos, a 10.4 km), Mollerussa (2 establecimientos, a 22.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lleida".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Lleida.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Lleida encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alcorcón (Madrid) — `madrid/alcorcon`

```
Escribe un texto de 180 a 240 palabras para la página de Alcorcón de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALCORCÓN (no uses ningún otro):
- Total de establecimientos: 18
- Reparto: 11 locutorios, 5 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 14
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 7
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 5 de 18
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 13.6 km), Parla (20 establecimientos, a 13.0 km), Leganés (15 establecimientos, a 5.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcorcón".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Alcorcón.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alcorcón encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Santander (Cantabria) — `cantabria/santander`

```
Escribe un texto de 180 a 240 palabras para la página de Santander de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SANTANDER (no uses ningún otro):
- Total de establecimientos: 17
- Reparto: 13 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 7
- Con teléfono publicado: 17
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 6
- Atributo publicable sin compararlo con una media: Recogida en tienda — 8 de 17
- Localidades cercanas con oferta: Torrelavega (7 establecimientos, a 22.3 km), Maliaño (3 establecimientos, a 5.2 km), Santoña (2 establecimientos, a 29.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Santander".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Santander.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Santander encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Valladolid (Valladolid) — `valladolid/valladolid`

```
Escribe un texto de 180 a 240 palabras para la página de Valladolid de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VALLADOLID (no uses ningún otro):
- Total de establecimientos: 17
- Reparto: 10 locutorios, 2 especializados en envío de dinero, 5 comercios con servicios relacionados
- Códigos postales: 9
- Con teléfono publicado: 16
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 9 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 9
- Con caída de actividad al mediodía, sin afirmar cierre: 9 de 9
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 12 de 17
- Localidades cercanas con oferta: Cabezón de Pisuerga (1 establecimientos, a 12.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Valladolid".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Valladolid.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Valladolid encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Burgos (Burgos) — `burgos/burgos`

```
Escribe un texto de 180 a 240 palabras para la página de Burgos de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BURGOS (no uses ningún otro):
- Total de establecimientos: 16
- Reparto: 4 locutorios, 8 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 15
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 8 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 8 de 8
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 8
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 6 de 16

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Burgos".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Burgos.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Burgos encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Logroño (La Rioja) — `la-rioja/logrono`

```
Escribe un texto de 180 a 240 palabras para la página de Logroño de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LOGROÑO (no uses ningún otro):
- Total de establecimientos: 16
- Reparto: 7 locutorios, 3 especializados en envío de dinero, 6 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 12
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 9 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 9
- Con caída de actividad al mediodía, sin afirmar cierre: 5 de 9
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 9 de 16
- Localidades cercanas con oferta: Nájera (1 establecimientos, a 24.0 km), Lodosa (1 establecimientos, a 30.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Logroño".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Logroño.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Logroño encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Tarragona (Tarragona) — `tarragona/tarragona`

```
Escribe un texto de 180 a 240 palabras para la página de Tarragona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TARRAGONA (no uses ningún otro):
- Total de establecimientos: 16
- Reparto: 6 locutorios, 7 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 15
- Franja de mayor afluencia: 11:00 a 14:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 6
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 6 de 16
- Localidades cercanas con oferta: Reus (12 establecimientos, a 10.8 km), Salou (6 establecimientos, a 9.4 km), Cambrils (5 establecimientos, a 15.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Tarragona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Tarragona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Tarragona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Elche (Alicante) — `alicante/elche`

```
Escribe un texto de 180 a 240 palabras para la página de Elche de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ELCHE (no uses ningún otro):
- Total de establecimientos: 15
- Reparto: 11 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 11
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 7 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 7 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 5 de 7
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 8 de 15
- Localidades cercanas con oferta: Alicante (38 establecimientos, a 21.6 km), Torrevieja (21 establecimientos, a 32.3 km), Callosa de Segura (4 establecimientos, a 21.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Elche".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Elche.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Elche encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Santa Coloma de Gramenet (Barcelona) — `barcelona/santa-coloma-de-gramenet`

```
Escribe un texto de 180 a 240 palabras para la página de Santa Coloma de Gramenet de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SANTA COLOMA DE GRAMENET (no uses ningún otro):
- Total de establecimientos: 15
- Reparto: 3 locutorios, 10 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 11
- Franja de mayor afluencia: 16:00 a 19:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 6
- Atributo publicable sin compararlo con una media: Aparcamiento adaptado para sillas de ruedas — 6 de 15
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 5.8 km), L'Hospitalet de Llobregat (38 establecimientos, a 12.2 km), Badalona (12 establecimientos, a 1.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Santa Coloma de Gramenet".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Santa Coloma de Gramenet.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Santa Coloma de Gramenet encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Getafe (Madrid) — `madrid/getafe`

```
Escribe un texto de 180 a 240 palabras para la página de Getafe de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GETAFE (no uses ningún otro):
- Total de establecimientos: 15
- Reparto: 11 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 11
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 8 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 8
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 8
- Atributo publicable sin compararlo con una media: Visita rápida — 10 de 15
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 11.6 km), Parla (20 establecimientos, a 8.6 km), Alcorcón (18 establecimientos, a 9.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Getafe".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Getafe.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Getafe encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Leganés (Madrid) — `madrid/leganes`

```
Escribe un texto de 180 a 240 palabras para la página de Leganés de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LEGANÉS (no uses ningún otro):
- Total de establecimientos: 15
- Reparto: 8 locutorios, 4 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 10
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 4 de 15
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 10.9 km), Parla (20 establecimientos, a 10.1 km), Alcorcón (18 establecimientos, a 5.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Leganés".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Leganés.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Leganés encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Toledo (Toledo) — `toledo/toledo`

```
Escribe un texto de 180 a 240 palabras para la página de Toledo de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TOLEDO (no uses ningún otro):
- Total de establecimientos: 15
- Reparto: 9 locutorios, 4 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 12
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 4 de 7
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 4 de 15
- Localidades cercanas con oferta: Torrijos (6 establecimientos, a 25.4 km), Illescas (5 establecimientos, a 32.0 km), Fuensalida (2 establecimientos, a 25.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Toledo".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Toledo.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Toledo encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Albacete (Albacete) — `albacete/albacete`

```
Escribe un texto de 180 a 240 palabras para la página de Albacete de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALBACETE (no uses ningún otro):
- Total de establecimientos: 13
- Reparto: 7 locutorios, 2 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 11
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 7
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 9 de 13
- Localidades cercanas con oferta: Tarazona de la Mancha (1 establecimientos, a 30.2 km), La Roda (1 establecimientos, a 34.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Albacete".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Albacete.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Albacete encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Móstoles (Madrid) — `madrid/mostoles`

```
Escribe un texto de 180 a 240 palabras para la página de Móstoles de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MÓSTOLES (no uses ningún otro):
- Total de establecimientos: 13
- Reparto: 7 locutorios, 1 especializados en envío de dinero, 5 comercios con servicios relacionados
- Códigos postales: 7
- Con teléfono publicado: 9
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 13
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 17.7 km), Parla (20 establecimientos, a 12.4 km), Alcorcón (18 establecimientos, a 4.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Móstoles".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Móstoles.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Móstoles encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Badalona (Barcelona) — `barcelona/badalona`

```
Escribe un texto de 180 a 240 palabras para la página de Badalona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BADALONA (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 8 locutorios, 4 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 12
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 7
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 3 de 12
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 6.0 km), L'Hospitalet de Llobregat (38 establecimientos, a 12.4 km), Santa Coloma de Gramenet (15 establecimientos, a 1.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Badalona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Badalona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Badalona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Manresa (Barcelona) — `barcelona/manresa`

```
Escribe un texto de 180 a 240 palabras para la página de Manresa de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MANRESA (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 7 locutorios, 2 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 10
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 3 de 12
- Localidades cercanas con oferta: Terrassa (10 establecimientos, a 23.6 km), Sabadell (10 establecimientos, a 30.3 km), Rubí (5 establecimientos, a 31.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Manresa".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Manresa.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Manresa encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Vicente de Barakaldo (Bizkaia) — `bizkaia/san-vicente-de-barakaldo`

```
Escribe un texto de 180 a 240 palabras para la página de San Vicente de Barakaldo de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN VICENTE DE BARAKALDO (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 8 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 11
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 7 de 12
- Localidades cercanas con oferta: Bilbao (67 establecimientos, a 5.8 km), Algorta (5 establecimientos, a 6.6 km), Leioa (4 establecimientos, a 3.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Vicente de Barakaldo".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de San Vicente de Barakaldo.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En San Vicente de Barakaldo encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Córdoba (Cordoba) — `cordoba/cordoba`

```
Escribe un texto de 180 a 240 palabras para la página de Córdoba de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CÓRDOBA (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 10 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 11
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 9 de 12
- Localidades cercanas con oferta: La Carlota (1 establecimientos, a 27.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Córdoba".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Córdoba.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Córdoba encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Melilla (Melilla) — `melilla/melilla`

```
Escribe un texto de 180 a 240 palabras para la página de Melilla de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MELILLA (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 8 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 10
- Atributo publicable sin compararlo con una media: Visita rápida — 7 de 12

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Melilla".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Melilla.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Melilla encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Reus (Tarragona) — `tarragona/reus`

```
Escribe un texto de 180 a 240 palabras para la página de Reus de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE REUS (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 8 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 12
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 7 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 6 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 7
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 8 de 12
- Localidades cercanas con oferta: Tarragona (16 establecimientos, a 10.8 km), Salou (6 establecimientos, a 8.8 km), Cambrils (5 establecimientos, a 10.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Reus".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Reus.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Reus encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Talavera de la Reina (Toledo) — `toledo/talavera-de-la-reina`

```
Escribe un texto de 180 a 240 palabras para la página de Talavera de la Reina de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TALAVERA DE LA REINA (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 6 locutorios, 3 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 10
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 3 de 12
- Localidades cercanas con oferta: Castillo de Bayuela (1 establecimientos, a 19.6 km), Malpica de Tajo (1 establecimientos, a 25.1 km), El Casar de Escalona (1 establecimientos, a 27.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Talavera de la Reina".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Talavera de la Reina.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Talavera de la Reina encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Donostia / San Sebastián (Gipuzkoa) — `gipuzkoa/donostia-san-sebastian`

```
Escribe un texto de 180 a 240 palabras para la página de Donostia / San Sebastián de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE DONOSTIA / SAN SEBASTIÁN (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 6 comercios con servicios relacionados
- Códigos postales: 7
- Con teléfono publicado: 9
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 5
- Atributo publicable sin compararlo con una media: Visita rápida — 8 de 11
- Localidades cercanas con oferta: Errenteria (9 establecimientos, a 6.1 km), Irun (5 establecimientos, a 14.8 km), Lasarte (3 establecimientos, a 6.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Donostia / San Sebastián".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Donostia / San Sebastián.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Donostia / San Sebastián encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Figueres (Girona) — `girona/figueres`

```
Escribe un texto de 180 a 240 palabras para la página de Figueres de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE FIGUERES (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 4 locutorios, 7 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 10
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 7 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 7 de 7
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 7
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 3 de 11
- Localidades cercanas con oferta: Girona (9 establecimientos, a 34.4 km), Salt (8 establecimientos, a 34.9 km), Banyoles (3 establecimientos, a 23.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Figueres".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Figueres.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Figueres encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Salamanca (Salamanca) — `salamanca/salamanca`

```
Escribe un texto de 180 a 240 palabras para la página de Salamanca de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SALAMANCA (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 8 locutorios, 3 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 9
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 4 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 5
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 3 de 11

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Salamanca".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Salamanca.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Salamanca encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Ávila (Avila) — `avila/avila`

```
Escribe un texto de 180 a 240 palabras para la página de Ávila de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ÁVILA (no uses ningún otro):
- Total de establecimientos: 10
- Reparto: 6 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 8
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 4
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 6 de 10

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ávila".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Ávila.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Ávila encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Sabadell (Barcelona) — `barcelona/sabadell`

```
Escribe un texto de 180 a 240 palabras para la página de Sabadell de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SABADELL (no uses ningún otro):
- Total de establecimientos: 10
- Reparto: 2 locutorios, 6 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 3
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 16.4 km), L'Hospitalet de Llobregat (38 establecimientos, a 19.7 km), Santa Coloma de Gramenet (15 establecimientos, a 14.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Sabadell".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Sabadell.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Sabadell encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Terrassa (Barcelona) — `barcelona/terrassa`

```
Escribe un texto de 180 a 240 palabras para la página de Terrassa de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TERRASSA (no uses ningún otro):
- Total de establecimientos: 10
- Reparto: 5 locutorios, 4 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 6
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 4
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 4 de 10
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 21.8 km), L'Hospitalet de Llobregat (38 establecimientos, a 23.3 km), Santa Coloma de Gramenet (15 establecimientos, a 21.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Terrassa".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Terrassa.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Terrassa encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### León (Leon) — `leon/leon`

```
Escribe un texto de 180 a 240 palabras para la página de León de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LEÓN (no uses ningún otro):
- Total de establecimientos: 10
- Reparto: 6 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 8
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 6
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 6 de 10
- Localidades cercanas con oferta: Valencia de Don Juan (1 establecimientos, a 34.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en León".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de León.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En León encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alcalá de Henares (Madrid) — `madrid/alcala-de-henares`

```
Escribe un texto de 180 a 240 palabras para la página de Alcalá de Henares de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALCALÁ DE HENARES (no uses ningún otro):
- Total de establecimientos: 10
- Reparto: 7 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 9
- Franja de mayor afluencia: 16:00 a 19:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 7 de 10
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 28.2 km), Alcobendas (9 establecimientos, a 23.5 km), Torrejón de Ardoz (8 establecimientos, a 9.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcalá de Henares".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Alcalá de Henares.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alcalá de Henares encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Benidorm (Alicante) — `alicante/benidorm`

```
Escribe un texto de 180 a 240 palabras para la página de Benidorm de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BENIDORM (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 5 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 5
- Franja de mayor afluencia: 20:00 a 23:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 5 de 9
- Localidades cercanas con oferta: Villajoyosa (5 establecimientos, a 10.0 km), Calp (4 establecimientos, a 19.2 km), Altea (2 establecimientos, a 9.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Benidorm".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Benidorm.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Benidorm encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Cornellà de Llobregat (Barcelona) — `barcelona/cornella-de-llobregat`

```
Escribe un texto de 180 a 240 palabras para la página de Cornellà de Llobregat de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CORNELLÀ DE LLOBREGAT (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 2 locutorios, 5 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 5
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 9.2 km), L'Hospitalet de Llobregat (38 establecimientos, a 2.9 km), Santa Coloma de Gramenet (15 establecimientos, a 14.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cornellà de Llobregat".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Cornellà de Llobregat.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Cornellà de Llobregat encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Algeciras (Cadiz) — `cadiz/algeciras`

```
Escribe un texto de 180 a 240 palabras para la página de Algeciras de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALGECIRAS (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 5 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 8
- Franja de mayor afluencia: 14:00 a 17:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Localidades cercanas con oferta: San Luis de Sabinillas (4 establecimientos, a 33.1 km), Ceuta (3 establecimientos, a 29.2 km), La Línea de la Concepción (1 establecimientos, a 9.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Algeciras".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Algeciras.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Algeciras encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Castellón de la Plana (Castellon) — `castellon/castellon-de-la-plana`

```
Escribe un texto de 180 a 240 palabras para la página de Castellón de la Plana de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CASTELLÓN DE LA PLANA (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 1 locutorios, 7 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 8
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 6 de 9
- Localidades cercanas con oferta: Villarreal (4 establecimientos, a 7.3 km), Borriana (4 establecimientos, a 11.6 km), Almassora (2 establecimientos, a 4.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Castellón de la Plana".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Castellón de la Plana.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Castellón de la Plana encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Errenteria (Gipuzkoa) — `gipuzkoa/errenteria`

```
Escribe un texto de 180 a 240 palabras para la página de Errenteria de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ERRENTERIA (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 8 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 9
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 6 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 6
- Atributo publicable sin compararlo con una media: Visita rápida — 5 de 9
- Localidades cercanas con oferta: Donostia / San Sebastián (11 establecimientos, a 6.1 km), Irun (5 establecimientos, a 9.0 km), Lasarte (3 establecimientos, a 10.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Errenteria".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Errenteria.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Errenteria encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Girona (Girona) — `girona/girona`

```
Escribe un texto de 180 a 240 palabras para la página de Girona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GIRONA (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 5 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 8
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 3 de 9
- Localidades cercanas con oferta: Figueres (11 establecimientos, a 34.4 km), Salt (8 establecimientos, a 1.1 km), Lloret de Mar (6 establecimientos, a 30.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Girona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Girona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Girona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Ibiza (Illes Balears) — `illes-balears/ibiza`

```
Escribe un texto de 180 a 240 palabras para la página de Ibiza de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE IBIZA (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 6 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 6 de 9
- Localidades cercanas con oferta: Santa Eulària des Riu (3 establecimientos, a 12.5 km), Sant Antoni de Portmany (3 establecimientos, a 13.4 km), Playa d'en Bossa (1 establecimientos, a 2.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ibiza".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Ibiza.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Ibiza encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Lugo (Lugo) — `lugo/lugo`

```
Escribe un texto de 180 a 240 palabras para la página de Lugo de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LUGO (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 6 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 8
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 8 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 8 de 8
- Con caída de actividad al mediodía, sin afirmar cierre: 6 de 8
- Atributo publicable sin compararlo con una media: Visita rápida — 6 de 9
- Localidades cercanas con oferta: Sarria (1 establecimientos, a 28.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lugo".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Lugo.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Lugo encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alcobendas (Madrid) — `madrid/alcobendas`

```
Escribe un texto de 180 a 240 palabras para la página de Alcobendas de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALCOBENDAS (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 8 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 6 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 5 de 6
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 5 de 9
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 15.2 km), Alcorcón (18 establecimientos, a 26.8 km), Leganés (15 establecimientos, a 25.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcobendas".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Alcobendas.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alcobendas encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Almería (Almeria) — `almeria/almeria`

```
Escribe un texto de 180 a 240 palabras para la página de Almería de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALMERÍA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 4 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 6 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 6 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 6
- Atributo publicable sin compararlo con una media: Visita rápida — 2 de 8
- Localidades cercanas con oferta: El Ejido (8 establecimientos, a 30.0 km), Roquetas de Mar (6 establecimientos, a 17.0 km), El Parador de las Hortichuelas (3 establecimientos, a 13.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Almería".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Almería.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Almería encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### El Ejido (Almeria) — `almeria/el-ejido`

```
Escribe un texto de 180 a 240 palabras para la página de El Ejido de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE EL EJIDO (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 0 locutorios, 3 especializados en envío de dinero, 5 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 2
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 2 de 8
- Localidades cercanas con oferta: Almería (8 establecimientos, a 30.0 km), Roquetas de Mar (6 establecimientos, a 14.1 km), El Parador de las Hortichuelas (3 establecimientos, a 16.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en El Ejido".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de El Ejido.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En El Ejido encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Vic (Barcelona) — `barcelona/vic`

```
Escribe un texto de 180 a 240 palabras para la página de Vic de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VIC (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 5 locutorios, 3 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Franja de mayor afluencia: 13:00 a 16:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 8
- Localidades cercanas con oferta: Manlleu (3 establecimientos, a 8.9 km), Sant Celoni (2 establecimientos, a 32.9 km), Cardedeu (2 establecimientos, a 33.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vic".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Vic.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Vic encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Jerez de la Frontera (Cadiz) — `cadiz/jerez-de-la-frontera`

```
Escribe un texto de 180 a 240 palabras para la página de Jerez de la Frontera de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE JEREZ DE LA FRONTERA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 5 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Visita rápida — 6 de 8
- Localidades cercanas con oferta: El Puerto de Sta María (3 establecimientos, a 13.3 km), Chiclana de la Frontera (2 establecimientos, a 29.5 km), Puerto Real (1 establecimientos, a 18.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Jerez de la Frontera".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Jerez de la Frontera.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Jerez de la Frontera encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Salt (Girona) — `girona/salt`

```
Escribe un texto de 180 a 240 palabras para la página de Salt de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SALT (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 3 locutorios, 2 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 4 de 4
- Atributo publicable sin compararlo con una media: Visita rápida — 2 de 8
- Localidades cercanas con oferta: Figueres (11 establecimientos, a 35.0 km), Girona (9 establecimientos, a 1.1 km), Lloret de Mar (6 establecimientos, a 30.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Salt".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Salt.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Salt encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Lepe (Huelva) — `huelva/lepe`

```
Escribe un texto de 180 a 240 palabras para la página de Lepe de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LEPE (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Compra en tienda — 2 de 8
- Localidades cercanas con oferta: Cartaya (4 establecimientos, a 5.6 km), Huelva (4 establecimientos, a 22.9 km), Moguer (2 establecimientos, a 32.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lepe".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Lepe.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Lepe encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Las Palmas de Gran Canaria (Las Palmas) — `las-palmas/las-palmas-de-gran-canaria`

```
Escribe un texto de 180 a 240 palabras para la página de Las Palmas de Gran Canaria de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LAS PALMAS DE GRAN CANARIA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 5 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 6 de 8
- Localidades cercanas con oferta: Vecindario (2 establecimientos, a 30.7 km), Telde (1 establecimientos, a 15.0 km), Santa Lucía de Tirajana (1 establecimientos, a 30.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Las Palmas de Gran Canaria".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Las Palmas de Gran Canaria.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Las Palmas de Gran Canaria encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Fuenlabrada (Madrid) — `madrid/fuenlabrada`

```
Escribe un texto de 180 a 240 palabras para la página de Fuenlabrada de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE FUENLABRADA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 2 locutorios, 5 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 5
- Con teléfono publicado: 8
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 6
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 6
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 16.8 km), Parla (20 establecimientos, a 5.7 km), Alcorcón (18 establecimientos, a 7.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Fuenlabrada".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Fuenlabrada.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Fuenlabrada encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Torrejón de Ardoz (Madrid) — `madrid/torrejon-de-ardoz`

```
Escribe un texto de 180 a 240 palabras para la página de Torrejón de Ardoz de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TORREJÓN DE ARDOZ (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 4 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 4
- Atributo publicable sin compararlo con una media: Visita rápida — 2 de 8
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 18.6 km), Parla (20 establecimientos, a 34.4 km), Alcorcón (18 establecimientos, a 32.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrejón de Ardoz".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Torrejón de Ardoz.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Torrejón de Ardoz encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Molina de Segura (Murcia) — `murcia/molina-de-segura`

```
Escribe un texto de 180 a 240 palabras para la página de Molina de Segura de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MOLINA DE SEGURA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 7 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 5 de 8
- Localidades cercanas con oferta: Murcia (37 establecimientos, a 10.4 km), Archena (6 establecimientos, a 10.3 km), Orihuela (4 establecimientos, a 23.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Molina de Segura".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Molina de Segura.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Molina de Segura encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Barañáin (Navarra) — `navarra/baranain`

```
Escribe un texto de 180 a 240 palabras para la página de Barañáin de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BARAÑÁIN (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 5 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 5
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 6 de 8
- Localidades cercanas con oferta: Pamplona (33 establecimientos, a 2.9 km), Tafalla (3 establecimientos, a 30.5 km), Burlada (2 establecimientos, a 5.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Barañáin".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Barañáin.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Barañáin encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Tudela (Navarra) — `navarra/tudela`

```
Escribe un texto de 180 a 240 palabras para la página de Tudela de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TUDELA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 4 locutorios, 4 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 2 de 8
- Localidades cercanas con oferta: Alfaro (2 establecimientos, a 17.8 km), Villafranca (2 establecimientos, a 27.0 km), Caparroso (2 establecimientos, a 31.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Tudela".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Tudela.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Tudela encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Isidro (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/san-isidro`

```
Escribe un texto de 180 a 240 palabras para la página de San Isidro de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN ISIDRO (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 5 locutorios, 0 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 5
- Atributo publicable sin compararlo con una media: Visita rápida — 6 de 8
- Localidades cercanas con oferta: Arona (7 establecimientos, a 13.3 km), Adeje (2 establecimientos, a 17.1 km), Cabo Blanco (1 establecimientos, a 11.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Isidro".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de San Isidro.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En San Isidro encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### A Coruña (A Coruña) — `a-coruna/a-coruna`

```
Escribe un texto de 180 a 240 palabras para la página de A Coruña de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE A CORUÑA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 4 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 3
- Atributo publicable sin compararlo con una media: Aparcamiento adaptado para sillas de ruedas — 2 de 7
- Localidades cercanas con oferta: Culleredo (2 establecimientos, a 4.9 km), Arteixo (1 establecimientos, a 9.7 km), Betanzos (1 establecimientos, a 19.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en A Coruña".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de A Coruña.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En A Coruña encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Torrelavega (Cantabria) — `cantabria/torrelavega`

```
Escribe un texto de 180 a 240 palabras para la página de Torrelavega de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TORRELAVEGA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 1 locutorios, 2 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 2 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 3 de 3
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 7
- Localidades cercanas con oferta: Santander (17 establecimientos, a 22.3 km), Maliaño (3 establecimientos, a 18.1 km), Los Corrales de Buelna (2 establecimientos, a 10.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrelavega".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Torrelavega.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Torrelavega encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Ciudad Real (Ciudad Real) — `ciudad-real/ciudad-real`

```
Escribe un texto de 180 a 240 palabras para la página de Ciudad Real de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CIUDAD REAL (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 4 locutorios, 3 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 7
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 4 de 7
- Localidades cercanas con oferta: Bolaños de Calatrava (3 establecimientos, a 20.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ciudad Real".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Ciudad Real.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Ciudad Real encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Guadalajara (Guadalajara) — `guadalajara/guadalajara`

```
Escribe un texto de 180 a 240 palabras para la página de Guadalajara de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GUADALAJARA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 6
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 3
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 5 de 7
- Localidades cercanas con oferta: Alcalá de Henares (10 establecimientos, a 23.2 km), Torrejón de Ardoz (8 establecimientos, a 32.2 km), Azuqueca de Henares (6 establecimientos, a 10.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Guadalajara".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Guadalajara.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Guadalajara encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Huesca (Huesca) — `huesca/huesca`

```
Escribe un texto de 180 a 240 palabras para la página de Huesca de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE HUESCA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 3 locutorios, 0 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Visita rápida — 2 de 7

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Huesca".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Huesca.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Huesca encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Collado Villalba (Madrid) — `madrid/collado-villalba`

```
Escribe un texto de 180 a 240 palabras para la página de Collado Villalba de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE COLLADO VILLALBA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 7
- Localidades cercanas con oferta: Alcorcón (18 establecimientos, a 34.8 km), Alcobendas (9 establecimientos, a 32.5 km), Colmenar Viejo (7 establecimientos, a 20.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Collado Villalba".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Collado Villalba.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Collado Villalba encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Colmenar Viejo (Madrid) — `madrid/colmenar-viejo`

```
Escribe un texto de 180 a 240 palabras para la página de Colmenar Viejo de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE COLMENAR VIEJO (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 5 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 5 de 7
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 28.4 km), Alcorcón (18 establecimientos, a 35.0 km), Alcobendas (9 establecimientos, a 17.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Colmenar Viejo".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Colmenar Viejo.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Colmenar Viejo encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Marbella (Malaga) — `malaga/marbella`

```
Escribe un texto de 180 a 240 palabras para la página de Marbella de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MARBELLA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 3 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 5
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 4
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 2 de 7
- Localidades cercanas con oferta: Fuengirola (6 establecimientos, a 23.4 km), San Pedro Alcántara (5 establecimientos, a 9.9 km), Estepona (5 establecimientos, a 25.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Marbella".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Marbella.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Marbella encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Arona (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/arona`

```
Escribe un texto de 180 a 240 palabras para la página de Arona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ARONA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 6 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 5 de 7
- Localidades cercanas con oferta: San Isidro (8 establecimientos, a 13.3 km), Adeje (2 establecimientos, a 8.5 km), Las Galletas (1 establecimientos, a 4.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Arona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Arona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Arona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Roquetas de Mar (Almeria) — `almeria/roquetas-de-mar`

```
Escribe un texto de 180 a 240 palabras para la página de Roquetas de Mar de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ROQUETAS DE MAR (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 0 locutorios, 3 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 3
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 2 de 6
- Localidades cercanas con oferta: El Ejido (8 establecimientos, a 14.1 km), Almería (8 establecimientos, a 17.1 km), El Parador de las Hortichuelas (3 establecimientos, a 5.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Roquetas de Mar".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Roquetas de Mar.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Roquetas de Mar encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Mataró (Barcelona) — `barcelona/mataro`

```
Escribe un texto de 180 a 240 palabras para la página de Mataró de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MATARÓ (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 4 locutorios, 2 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 2 de 6
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 26.6 km), L'Hospitalet de Llobregat (38 establecimientos, a 33.0 km), Santa Coloma de Gramenet (15 establecimientos, a 21.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Mataró".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Mataró.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Mataró encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Vilanova i la Geltrú (Barcelona) — `barcelona/vilanova-i-la-geltru`

```
Escribe un texto de 180 a 240 palabras para la página de Vilanova i la Geltrú de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VILANOVA I LA GELTRÚ (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 3 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 3
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 6
- Localidades cercanas con oferta: Cornellà de Llobregat (9 establecimientos, a 33.4 km), Vilafranca del Penedès (5 establecimientos, a 13.9 km), Calafell (4 establecimientos, a 12.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vilanova i la Geltrú".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Vilanova i la Geltrú.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Vilanova i la Geltrú encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Lloret de Mar (Girona) — `girona/lloret-de-mar`

```
Escribe un texto de 180 a 240 palabras para la página de Lloret de Mar de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LLORET DE MAR (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 4 de 6
- Localidades cercanas con oferta: Girona (9 establecimientos, a 30.8 km), Salt (8 establecimientos, a 30.8 km), Pineda de Mar (4 establecimientos, a 15.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lloret de Mar".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Lloret de Mar.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Lloret de Mar encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Azuqueca de Henares (Guadalajara) — `guadalajara/azuqueca-de-henares`

```
Escribe un texto de 180 a 240 palabras para la página de Azuqueca de Henares de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE AZUQUECA DE HENARES (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 3 locales)
- Franja más tranquila: 17:00 a 19:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 3
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 6
- Localidades cercanas con oferta: Alcalá de Henares (10 establecimientos, a 12.7 km), Alcobendas (9 establecimientos, a 31.6 km), Torrejón de Ardoz (8 establecimientos, a 21.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Azuqueca de Henares".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Azuqueca de Henares.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Azuqueca de Henares encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Puerto del Rosario (Las Palmas) — `las-palmas/puerto-del-rosario`

```
Escribe un texto de 180 a 240 palabras para la página de Puerto del Rosario de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE PUERTO DEL ROSARIO (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 5 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 6
- Localidades cercanas con oferta: Corralejo (1 establecimientos, a 26.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Puerto del Rosario".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Puerto del Rosario.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Puerto del Rosario encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Sebastián de los Reyes (Madrid) — `madrid/san-sebastian-de-los-reyes`

```
Escribe un texto de 180 a 240 palabras para la página de San Sebastián de los Reyes de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN SEBASTIÁN DE LOS REYES (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 5 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Franja de mayor afluencia: 13:00 a 16:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 3
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 5 de 6
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 15.9 km), Alcorcón (18 establecimientos, a 27.8 km), Leganés (15 establecimientos, a 26.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Sebastián de los Reyes".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de San Sebastián de los Reyes.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En San Sebastián de los Reyes encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Fuengirola (Malaga) — `malaga/fuengirola`

```
Escribe un texto de 180 a 240 palabras para la página de Fuengirola de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE FUENGIROLA (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — los 6
- Localidades cercanas con oferta: Málaga (30 establecimientos, a 25.5 km), Marbella (7 establecimientos, a 23.4 km), San Pedro Alcántara (5 establecimientos, a 33.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Fuengirola".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Fuengirola.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Fuengirola encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Archena (Murcia) — `murcia/archena`

```
Escribe un texto de 180 a 240 palabras para la página de Archena de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ARCHENA (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 2 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 2 de 6
- Localidades cercanas con oferta: Murcia (37 establecimientos, a 20.7 km), Molina de Segura (8 establecimientos, a 10.3 km), Orihuela (4 establecimientos, a 31.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Archena".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Archena.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Archena encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Totana (Murcia) — `murcia/totana`

```
Escribe un texto de 180 a 240 palabras para la página de Totana de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TOTANA (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 3 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 5
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 5
- Atributo publicable sin compararlo con una media: Visita rápida — 5 de 6
- Localidades cercanas con oferta: Lorca (26 establecimientos, a 20.1 km), Mazarrón (3 establecimientos, a 25.0 km), Fuente Alamo (3 establecimientos, a 29.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Totana".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Totana.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Totana encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### La Laguna (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/la-laguna`

```
Escribe un texto de 180 a 240 palabras para la página de La Laguna de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LA LAGUNA (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 5 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 3
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 3
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 6
- Localidades cercanas con oferta: Santa Cruz de Tenerife (6 establecimientos, a 4.2 km), Candelaria (1 establecimientos, a 13.5 km), Arafo (1 establecimientos, a 17.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en La Laguna".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de La Laguna.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En La Laguna encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Santa Cruz de Tenerife (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/santa-cruz-de-tenerife`

```
Escribe un texto de 180 a 240 palabras para la página de Santa Cruz de Tenerife de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SANTA CRUZ DE TENERIFE (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 5 de 6
- Localidades cercanas con oferta: La Laguna (6 establecimientos, a 4.2 km), Candelaria (1 establecimientos, a 16.0 km), Arafo (1 establecimientos, a 20.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Santa Cruz de Tenerife".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Santa Cruz de Tenerife.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Santa Cruz de Tenerife encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Segovia (Segovia) — `segovia/segovia`

```
Escribe un texto de 180 a 240 palabras para la página de Segovia de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SEGOVIA (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 4
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Recogida en tienda — 3 de 6
- Localidades cercanas con oferta: Moralzarzal (1 establecimientos, a 31.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Segovia".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Segovia.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Segovia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Salou (Tarragona) — `tarragona/salou`

```
Escribe un texto de 180 a 240 palabras para la página de Salou de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SALOU (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 5 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 6
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 5 de 6
- Localidades cercanas con oferta: Tarragona (16 establecimientos, a 9.4 km), Reus (12 establecimientos, a 8.8 km), Cambrils (5 establecimientos, a 7.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Salou".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Salou.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Salou encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Torrijos (Toledo) — `toledo/torrijos`

```
Escribe un texto de 180 a 240 palabras para la página de Torrijos de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TORRIJOS (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 1 locutorios, 3 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Localidades cercanas con oferta: Toledo (15 establecimientos, a 25.4 km), Fuensalida (2 establecimientos, a 9.8 km), Santa Olalla (1 establecimientos, a 13.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrijos".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Torrijos.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Torrijos encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Mislata (Valencia) — `valencia/mislata`

```
Escribe un texto de 180 a 240 palabras para la página de Mislata de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MISLATA (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 3 locutorios, 3 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 2 de 6
- Localidades cercanas con oferta: Valencia (96 establecimientos, a 3.6 km), Torrent (4 establecimientos, a 6.4 km), Paterna (3 establecimientos, a 3.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Mislata".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Mislata.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Mislata encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Villajoyosa (Alicante) — `alicante/villajoyosa`

```
Escribe un texto de 180 a 240 palabras para la página de Villajoyosa de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VILLAJOYOSA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 3 locutorios, 0 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 3
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 2 de 5
- Localidades cercanas con oferta: Alicante (38 establecimientos, a 27.4 km), Benidorm (9 establecimientos, a 10.0 km), Calp (4 establecimientos, a 29.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Villajoyosa".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Villajoyosa.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Villajoyosa encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Barberà del Vallès (Barcelona) — `barcelona/barbera-del-valles`

```
Escribe un texto de 180 a 240 palabras para la página de Barberà del Vallès de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BARBERÀ DEL VALLÈS (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 0 locutorios, 5 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 2 de 5
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 12.9 km), L'Hospitalet de Llobregat (38 establecimientos, a 16.5 km), Santa Coloma de Gramenet (15 establecimientos, a 10.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Barberà del Vallès".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Barberà del Vallès.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Barberà del Vallès encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Ripollet (Barcelona) — `barcelona/ripollet`

```
Escribe un texto de 180 a 240 palabras para la página de Ripollet de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE RIPOLLET (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 2 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 3
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 2 de 5
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 9.8 km), L'Hospitalet de Llobregat (38 establecimientos, a 14.6 km), Santa Coloma de Gramenet (15 establecimientos, a 6.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ripollet".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Ripollet.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Ripollet encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Rubí (Barcelona) — `barcelona/rubi`

```
Escribe un texto de 180 a 240 palabras para la página de Rubí de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE RUBÍ (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 3 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 3
- Atributo publicable sin compararlo con una media: Recogida en tienda — 2 de 5
- Localidades cercanas con oferta: Barcelona (83 establecimientos, a 14.4 km), L'Hospitalet de Llobregat (38 establecimientos, a 14.6 km), Santa Coloma de Gramenet (15 establecimientos, a 15.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Rubí".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Rubí.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Rubí encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Vilafranca del Penedès (Barcelona) — `barcelona/vilafranca-del-penedes`

```
Escribe un texto de 180 a 240 palabras para la página de Vilafranca del Penedès de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VILAFRANCA DEL PENEDÈS (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 1 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 2 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 3
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 4 de 5
- Localidades cercanas con oferta: L'Hospitalet de Llobregat (38 establecimientos, a 34.4 km), Cornellà de Llobregat (9 establecimientos, a 31.7 km), Vilanova i la Geltrú (6 establecimientos, a 13.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vilafranca del Penedès".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Vilafranca del Penedès.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Vilafranca del Penedès encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Algorta (Bizkaia) — `bizkaia/algorta`

```
Escribe un texto de 180 a 240 palabras para la página de Algorta de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALGORTA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 3
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 3 de 5
- Localidades cercanas con oferta: Bilbao (67 establecimientos, a 11.9 km), San Vicente de Barakaldo (12 establecimientos, a 6.6 km), Leioa (4 establecimientos, a 3.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Algorta".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Algorta.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Algorta encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Cáceres (Caceres) — `caceres/caceres`

```
Escribe un texto de 180 a 240 palabras para la página de Cáceres de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CÁCERES (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 3 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 3 de 5

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cáceres".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Cáceres.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Cáceres encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Cuenca (Cuenca) — `cuenca/cuenca`

```
Escribe un texto de 180 a 240 palabras para la página de Cuenca de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CUENCA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 3 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 3
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 3 de 5

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cuenca".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Cuenca.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Cuenca encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Irun (Gipuzkoa) — `gipuzkoa/irun`

```
Escribe un texto de 180 a 240 palabras para la página de Irun de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE IRUN (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 5
- Localidades cercanas con oferta: Donostia / San Sebastián (11 establecimientos, a 14.8 km), Errenteria (9 establecimientos, a 9.0 km), Lasarte (3 establecimientos, a 19.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Irun".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Irun.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Irun encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Inca (Illes Balears) — `illes-balears/inca`

```
Escribe un texto de 180 a 240 palabras para la página de Inca de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE INCA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 2 de 5
- Localidades cercanas con oferta: Palma (57 establecimientos, a 27.0 km), Manacor (4 establecimientos, a 30.7 km), Sóller (2 establecimientos, a 18.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Inca".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Inca.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Inca encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Arganda del Rey (Madrid) — `madrid/arganda-del-rey`

```
Escribe un texto de 180 a 240 palabras para la página de Arganda del Rey de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ARGANDA DEL REY (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 1 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 2
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 2 de 5
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 23.8 km), Parla (20 establecimientos, a 28.1 km), Alcorcón (18 establecimientos, a 32.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Arganda del Rey".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Arganda del Rey.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Arganda del Rey encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Majadahonda (Madrid) — `madrid/majadahonda`

```
Escribe un texto de 180 a 240 palabras para la página de Majadahonda de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MAJADAHONDA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 15:00 a 18:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Visita rápida — 3 de 5
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 13.7 km), Parla (20 establecimientos, a 25.3 km), Alcorcón (18 establecimientos, a 12.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Majadahonda".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Majadahonda.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Majadahonda encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Fernando de Henares (Madrid) — `madrid/san-fernando-de-henares`

```
Escribe un texto de 180 a 240 palabras para la página de San Fernando de Henares de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN FERNANDO DE HENARES (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 5
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 13.2 km), Parla (20 establecimientos, a 28.7 km), Alcorcón (18 establecimientos, a 26.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Fernando de Henares".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de San Fernando de Henares.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En San Fernando de Henares encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Estepona (Malaga) — `malaga/estepona`

```
Escribe un texto de 180 a 240 palabras para la página de Estepona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ESTEPONA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 3 locutorios, 2 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 3
- Atributo publicable sin compararlo con una media: Visita rápida — 3 de 5
- Localidades cercanas con oferta: Marbella (7 establecimientos, a 25.5 km), San Pedro Alcántara (5 establecimientos, a 15.7 km), San Luis de Sabinillas (4 establecimientos, a 9.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Estepona".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Estepona.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Estepona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Pedro Alcántara (Malaga) — `malaga/san-pedro-alcantara`

```
Escribe un texto de 180 a 240 palabras para la página de San Pedro Alcántara de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN PEDRO ALCÁNTARA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 4 de 4
- Con caída de actividad al mediodía, sin afirmar cierre: 1 de 4
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 5
- Localidades cercanas con oferta: Marbella (7 establecimientos, a 9.9 km), Fuengirola (6 establecimientos, a 33.2 km), Estepona (5 establecimientos, a 15.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Pedro Alcántara".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de San Pedro Alcántara.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En San Pedro Alcántara encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Águilas (Murcia) — `murcia/aguilas`

```
Escribe un texto de 180 a 240 palabras para la página de Águilas de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ÁGUILAS (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 2 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 3
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 3
- Con caída de actividad al mediodía, sin afirmar cierre: 2 de 3
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 3 de 5
- Localidades cercanas con oferta: Lorca (26 establecimientos, a 31.3 km), Pulpí (3 establecimientos, a 14.3 km), Vera (3 establecimientos, a 30.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Águilas".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Águilas.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Águilas encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Palencia (Palencia) — `palencia/palencia`

```
Escribe un texto de 180 a 240 palabras para la página de Palencia de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE PALENCIA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 3 locutorios, 0 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Tarjetas de débito — 3 de 5
- Localidades cercanas con oferta: Paredes de Nava (1 establecimientos, a 20.9 km), Cabezón de Pisuerga (1 establecimientos, a 30.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Palencia".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Palencia.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Palencia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Juan de Aznalfarache (Sevilla) — `sevilla/san-juan-de-aznalfarache`

```
Escribe un texto de 180 a 240 palabras para la página de San Juan de Aznalfarache de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN JUAN DE AZNALFARACHE (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Pagos con móvil vía NFC — 4 de 5
- Localidades cercanas con oferta: Sevilla (70 establecimientos, a 6.4 km), Castilleja de la Cuesta (3 establecimientos, a 3.4 km), Camas (2 establecimientos, a 4.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Juan de Aznalfarache".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de San Juan de Aznalfarache.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En San Juan de Aznalfarache encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Soria (Soria) — `soria/soria`

```
Escribe un texto de 180 a 240 palabras para la página de Soria de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SORIA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 2
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 5
- Localidades cercanas con oferta: Almazán (1 establecimientos, a 31.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Soria".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Soria.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Soria encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Amposta (Tarragona) — `tarragona/amposta`

```
Escribe un texto de 180 a 240 palabras para la página de Amposta de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE AMPOSTA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Visita rápida — 4 de 5
- Localidades cercanas con oferta: Tortosa (5 establecimientos, a 12.6 km), Benicarló (4 establecimientos, a 34.7 km), L'Ametlla de Mar (2 establecimientos, a 27.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Amposta".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Amposta.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Amposta encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Cambrils (Tarragona) — `tarragona/cambrils`

```
Escribe un texto de 180 a 240 palabras para la página de Cambrils de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CAMBRILS (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 4 de 5
- Localidades cercanas con oferta: Tarragona (16 establecimientos, a 16.0 km), Reus (12 establecimientos, a 10.1 km), Salou (6 establecimientos, a 7.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cambrils".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Cambrils.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Cambrils encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Tortosa (Tarragona) — `tarragona/tortosa`

```
Escribe un texto de 180 a 240 palabras para la página de Tortosa de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TORTOSA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 1 locutorios, 4 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Atributo publicable sin compararlo con una media: Acceso para sillas de ruedas — 2 de 5
- Localidades cercanas con oferta: Amposta (5 establecimientos, a 12.6 km), Móra d'Ebre (3 establecimientos, a 32.4 km), L'Ametlla de Mar (2 establecimientos, a 25.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Tortosa".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Tortosa.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Tortosa encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alcañiz (Teruel) — `teruel/alcaniz`

```
Escribe un texto de 180 a 240 palabras para la página de Alcañiz de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALCAÑIZ (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 0 locutorios, 4 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 5
- Localidades cercanas con oferta: Caspe (1 establecimientos, a 22.0 km), Alcorisa (1 establecimientos, a 27.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcañiz".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Alcañiz.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alcañiz encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Illescas (Toledo) — `toledo/illescas`

```
Escribe un texto de 180 a 240 palabras para la página de Illescas de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ILLESCAS (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 3
- Atributo publicable sin compararlo con una media: Tarjetas de crédito — 2 de 5
- Localidades cercanas con oferta: Madrid (272 establecimientos, a 34.7 km), Parla (20 establecimientos, a 14.6 km), Alcorcón (18 establecimientos, a 25.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Illescas".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Illescas.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Illescas encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alzira (Valencia) — `valencia/alzira`

```
Escribe un texto de 180 a 240 palabras para la página de Alzira de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALZIRA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 1 locutorios, 2 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales: 1
- Con teléfono publicado: 4
- Localidades cercanas con oferta: Gandia (20 establecimientos, a 29.4 km), Xàtiva (4 establecimientos, a 19.6 km), Torrent (4 establecimientos, a 31.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alzira".
- Integra el total, el reparto por tipo y el teléfono publicado.
- Si hay datos de afluencia, dedica el segundo párrafo a la muestra, la franja
  punta, la tranquila, el domingo y la posible pausa de mediodía. Di
  expresamente que son observaciones de afluencia, no horarios oficiales.
- Un encabezado "## " a mitad del texto, con un título específico de Alzira.
- Explica que el término locutorio ya no se limita a cabinas de llamadas, pero
  no atribuyas recargas de móvil, papelería ni ningún servicio a todos los
  establecimientos: deben confirmarse uno a uno.

PROHIBIDO
- Inventar horarios, comisiones, precios, servicios u operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Convertir actividad en domingo en "abre los domingos", o una caída al
  mediodía en "cierra": la afluencia no demuestra apertura ni cierre.
- Añadir barrios, zonas, medios de transporte, perfiles de clientela o causas
  que no estén entre los datos suministrados.
- Comparar con otras ciudades o con una media no incluida en el bloque.
- Redondear cifras o distancias.
- Usar las palabras reseñas, opiniones, comentarios, ficha, scraping o Google,
  ni explicar el origen interno de los datos.
- Añadir notas, rutas de archivos, comentarios editoriales o texto fuera del
  artículo.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alzira encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```
