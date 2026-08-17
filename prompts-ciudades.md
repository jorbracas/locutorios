# Prompts de redacción por localidad

121 localidades con 5 o más establecimientos, ordenadas de mayor a menor.

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
- Total de establecimientos: 271
- Reparto: 177 locutorios, 57 especializados en envío de dinero, 37 comercios con servicios relacionados
- Códigos postales cubiertos: 28001, 28002, 28003, 28004, 28005, 28006, 28007, 28008, 28009, 28010, 28011, 28012, 28013, 28014, 28015, 28017, 28018, 28019, 28020, 28021, 28022, 28024, 28025, 28026, 28027, 28028, 28029, 28030, 28031, 28032, 28033, 28034, 28037, 28038, 28039, 28041, 28042, 28043, 28044, 28045, 28047, 28053
- Con teléfono publicado: 230
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 147 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 128 de 147
- Con jornada partida (cierre al mediodía): 44 de 147
- Tarjetas de crédito: 140 de 271
- Tarjetas de débito: 140 de 271
- Pagos con móvil vía NFC: 115 de 271
- Visita rápida: 105 de 271
- Localidades cercanas con oferta: Parla (20 establecimientos, a 20.2 km), Alcorcón (18 establecimientos, a 13.6 km), Leganés (15 establecimientos, a 10.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Madrid".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Madrid.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Total de establecimientos: 99
- Reparto: 48 locutorios, 28 especializados en envío de dinero, 23 comercios con servicios relacionados
- Códigos postales cubiertos: 46004, 46005, 46006, 46007, 46008, 46009, 46011, 46014, 46015, 46018, 46019, 46020, 46021, 46022, 46023, 46024, 46025, 46035, 46139, 46920
- Con teléfono publicado: 73
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 46 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 41 de 46
- Con jornada partida (cierre al mediodía): 17 de 46
- Acceso para sillas de ruedas: 63 de 99
- Tarjetas de crédito: 46 de 99
- Tarjetas de débito: 39 de 99
- Pagos con móvil vía NFC: 36 de 99
- Visita rápida: 32 de 99
- Localidades cercanas con oferta: Mislata (4 establecimientos, a 3.6 km), Torrent (4 establecimientos, a 9.3 km), Burjassot (3 establecimientos, a 5.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Valencia".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Valencia.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50010, 50011, 50013, 50014, 50015, 50017, 50620
- Con teléfono publicado: 69
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 38 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 35 de 38
- Con jornada partida (cierre al mediodía): 9 de 38
- Aparcamiento adaptado para sillas de ruedas: 38 de 87
- Tarjetas de débito: 30 de 87
- Tarjetas de crédito: 29 de 87
- Pagos con móvil vía NFC: 28 de 87
- Localidades cercanas con oferta: Utebo (1 establecimientos, a 10.7 km), Zuera (1 establecimientos, a 25.8 km), Pedrola (1 establecimientos, a 31.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Zaragoza".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Zaragoza.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Total de establecimientos: 84
- Reparto: 53 locutorios, 20 especializados en envío de dinero, 11 comercios con servicios relacionados
- Códigos postales cubiertos: 08001, 08003, 08004, 08005, 08013, 08014, 08015, 08016, 08019, 08020, 08023, 08025, 08026, 08027, 08028, 08029, 08030, 08031, 08032, 08033, 08037, 08038, 08041, 08042, 08170
- Con teléfono publicado: 70
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 36 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 33 de 36
- Con jornada partida (cierre al mediodía): 18 de 36
- Tarjetas de crédito: 42 de 84
- Tarjetas de débito: 37 de 84
- Pagos con móvil vía NFC: 34 de 84
- Aparcamiento adaptado para sillas de ruedas: 28 de 84
- Acceso para sillas de ruedas: 25 de 84
- Localidades cercanas con oferta: L'Hospitalet de Llobregat (36 establecimientos, a 6.6 km), Santa Coloma de Gramenet (16 establecimientos, a 5.5 km), Badalona (11 establecimientos, a 5.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Barcelona".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Barcelona.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 41001, 41004, 41005, 41006, 41007, 41008, 41009, 41010, 41011, 41013, 41014, 41016
- Con teléfono publicado: 53
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 24 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 23 de 24
- Con jornada partida (cierre al mediodía): 9 de 24
- Acceso para sillas de ruedas: 44 de 70
- Visita rápida: 26 de 70
- Tarjetas de crédito: 25 de 70
- Tarjetas de débito: 24 de 70
- Pagos con móvil vía NFC: 23 de 70
- Localidades cercanas con oferta: San Juan de Aznalfarache (5 establecimientos, a 6.4 km), Castilleja de la Cuesta (3 establecimientos, a 7.4 km), Camas (2 establecimientos, a 5.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Sevilla".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Sevilla.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Total de establecimientos: 66
- Reparto: 42 locutorios, 17 especializados en envío de dinero, 7 comercios con servicios relacionados
- Códigos postales cubiertos: 48001, 48002, 48003, 48004, 48005, 48006, 48007, 48008, 48010, 48012, 48013, 48014, 48015
- Con teléfono publicado: 56
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 29 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 27 de 29
- Con jornada partida (cierre al mediodía): 17 de 29
- Tarjetas de crédito: 29 de 66
- Tarjetas de débito: 29 de 66
- Pagos con móvil vía NFC: 26 de 66
- Visita rápida: 23 de 66
- Acceso para sillas de ruedas: 20 de 66
- Localidades cercanas con oferta: San Vicente de Barakaldo (12 establecimientos, a 5.8 km), Algorta (5 establecimientos, a 11.9 km), Durango (4 establecimientos, a 26.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Bilbao".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Bilbao.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 07001, 07002, 07003, 07004, 07005, 07006, 07007, 07008, 07010, 07011, 07013, 07015
- Con teléfono publicado: 44
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 37 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 36 de 37
- Con jornada partida (cierre al mediodía): 17 de 37
- Tarjetas de crédito: 27 de 57
- Tarjetas de débito: 26 de 57
- Pagos con móvil vía NFC: 23 de 57
- Visita rápida: 18 de 57
- Acceso para sillas de ruedas: 15 de 57
- Localidades cercanas con oferta: Inca (5 establecimientos, a 27.1 km), Sóller (2 establecimientos, a 22.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Palma".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Palma.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Total de establecimientos: 39
- Reparto: 19 locutorios, 8 especializados en envío de dinero, 12 comercios con servicios relacionados
- Códigos postales cubiertos: 18001, 18002, 18003, 18004, 18005, 18006, 18007, 18009, 18010, 18011, 18012, 18013, 18014, 18015
- Con teléfono publicado: 22
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 11 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 8 de 11
- Con jornada partida (cierre al mediodía): 9 de 11
- Tarjetas de crédito: 15 de 39
- Acceso para sillas de ruedas: 15 de 39
- Pagos con móvil vía NFC: 12 de 39
- Tarjetas de débito: 12 de 39
- Visita rápida: 10 de 39
- Localidades cercanas con oferta: Armilla (2 establecimientos, a 4.1 km), Urb. los Vergeles (1 establecimientos, a 1.7 km), Maracena (1 establecimientos, a 4.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Granada".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Granada.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Granada encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Murcia (Murcia) — `murcia/murcia`

```
Escribe un texto de 180 a 240 palabras para la página de Murcia de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MURCIA (no uses ningún otro):
- Total de establecimientos: 39
- Reparto: 15 locutorios, 13 especializados en envío de dinero, 11 comercios con servicios relacionados
- Códigos postales cubiertos: 30002, 30003, 30004, 30005, 30006, 30007, 30009, 30010, 30011, 30012, 30100, 30570
- Con teléfono publicado: 28
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 11 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 10 de 11
- Con jornada partida (cierre al mediodía): 6 de 11
- Acceso para sillas de ruedas: 19 de 39
- Pagos con móvil vía NFC: 13 de 39
- Tarjetas de débito: 13 de 39
- Tarjetas de crédito: 12 de 39
- Visita rápida: 10 de 39
- Localidades cercanas con oferta: Molina de Segura (8 establecimientos, a 10.5 km), Archena (6 establecimientos, a 20.8 km), Orihuela (4 establecimientos, a 19.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Murcia".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Murcia.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Murcia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Alicante (Alicante) — `alicante/alicante`

```
Escribe un texto de 180 a 240 palabras para la página de Alicante de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ALICANTE (no uses ningún otro):
- Total de establecimientos: 38
- Reparto: 18 locutorios, 11 especializados en envío de dinero, 9 comercios con servicios relacionados
- Códigos postales cubiertos: 03001, 03004, 03005, 03007, 03009, 03010, 03011, 03012, 03013, 03014, 03015, 03540
- Con teléfono publicado: 27
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 14 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 14
- Con jornada partida (cierre al mediodía): 4 de 14
- Acceso para sillas de ruedas: 17 de 38
- Tarjetas de crédito: 16 de 38
- Tarjetas de débito: 13 de 38
- Pagos con móvil vía NFC: 12 de 38
- Visita rápida: 10 de 38
- Localidades cercanas con oferta: Elche (15 establecimientos, a 21.6 km), Villajoyosa (5 establecimientos, a 27.4 km), Elda (3 establecimientos, a 29.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alicante".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Alicante.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alicante encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Vitoria-Gasteiz (Araba/Álava) — `araba-alava/vitoria-gasteiz`

```
Escribe un texto de 180 a 240 palabras para la página de Vitoria-Gasteiz de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VITORIA-GASTEIZ (no uses ningún otro):
- Total de establecimientos: 36
- Reparto: 23 locutorios, 7 especializados en envío de dinero, 6 comercios con servicios relacionados
- Códigos postales cubiertos: 01001, 01002, 01003, 01006, 01007, 01010, 01012, 01013, 01015, 01400
- Con teléfono publicado: 32
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 18 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 17 de 18
- Con jornada partida (cierre al mediodía): 9 de 18
- Tarjetas de crédito: 21 de 36
- Tarjetas de débito: 18 de 36
- Visita rápida: 16 de 36
- Pagos con móvil vía NFC: 16 de 36
- Acceso para sillas de ruedas: 10 de 36
- Localidades cercanas con oferta: Durango (4 establecimientos, a 34.7 km), Miranda de Ebro (3 establecimientos, a 28.8 km), Arrasate / Mondragón (2 establecimientos, a 27.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vitoria-Gasteiz".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Vitoria-Gasteiz.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Vitoria-Gasteiz encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### L'Hospitalet de Llobregat (Barcelona) — `barcelona/l-hospitalet-de-llobregat`

```
Escribe un texto de 180 a 240 palabras para la página de L'Hospitalet de Llobregat de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE L'HOSPITALET DE LLOBREGAT (no uses ningún otro):
- Total de establecimientos: 36
- Reparto: 22 locutorios, 7 especializados en envío de dinero, 7 comercios con servicios relacionados
- Códigos postales cubiertos: 08901, 08902, 08903, 08904, 08905, 08906
- Con teléfono publicado: 28
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 15 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 14 de 15
- Con jornada partida (cierre al mediodía): 8 de 15
- Tarjetas de crédito: 12 de 36
- Pagos con móvil vía NFC: 10 de 36
- Tarjetas de débito: 10 de 36
- Aparcamiento adaptado para sillas de ruedas: 9 de 36
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 6.6 km), Santa Coloma de Gramenet (16 establecimientos, a 12.2 km), Badalona (11 establecimientos, a 12.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en L'Hospitalet de Llobregat".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de L'Hospitalet de Llobregat.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En L'Hospitalet de Llobregat encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Pamplona (Navarra) — `navarra/pamplona`

```
Escribe un texto de 180 a 240 palabras para la página de Pamplona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE PAMPLONA (no uses ningún otro):
- Total de establecimientos: 33
- Reparto: 15 locutorios, 10 especializados en envío de dinero, 8 comercios con servicios relacionados
- Códigos postales cubiertos: 31001, 31002, 31003, 31004, 31005, 31008, 31011, 31012, 31014, 31015
- Con teléfono publicado: 27
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 13 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 13
- Con jornada partida (cierre al mediodía): 9 de 13
- Tarjetas de crédito: 17 de 33
- Pagos con móvil vía NFC: 16 de 33
- Tarjetas de débito: 16 de 33
- Visita rápida: 14 de 33
- Acceso para sillas de ruedas: 10 de 33
- Localidades cercanas con oferta: Barañáin (8 establecimientos, a 2.9 km), Tafalla (3 establecimientos, a 32.2 km), Burlada (2 establecimientos, a 2.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Pamplona".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Pamplona.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 29001, 29002, 29003, 29004, 29006, 29007, 29009, 29010, 29011, 29012, 29014, 29018, 29909
- Con teléfono publicado: 25
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 11 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 11
- Con jornada partida (cierre al mediodía): 2 de 11
- Acceso para sillas de ruedas: 16 de 30
- Tarjetas de crédito: 15 de 30
- Tarjetas de débito: 13 de 30
- Visita rápida: 12 de 30
- Pagos con móvil vía NFC: 11 de 30
- Localidades cercanas con oferta: Fuengirola (6 establecimientos, a 25.4 km), Torremolinos (4 establecimientos, a 11.7 km), Las Lagunas de Mijas (3 establecimientos, a 26.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Málaga".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Málaga.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 30800
- Con teléfono publicado: 20
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 14 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 14 de 14
- Con jornada partida (cierre al mediodía): 6 de 14
- Tarjetas de débito: 9 de 26
- Tarjetas de crédito: 9 de 26
- Pagos con móvil vía NFC: 7 de 26
- Acceso para sillas de ruedas: 7 de 26
- Localidades cercanas con oferta: Totana (6 establecimientos, a 20.1 km), Águilas (5 establecimientos, a 31.3 km), Pulpí (3 establecimientos, a 29.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lorca".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Lorca.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 33001, 33006, 33007, 33010, 33011, 33012, 33013
- Con teléfono publicado: 20
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 13 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 13
- Con jornada partida (cierre al mediodía): 5 de 13
- Visita rápida: 11 de 23
- Tarjetas de débito: 11 de 23
- Tarjetas de crédito: 11 de 23
- Pagos con móvil vía NFC: 10 de 23
- Aparcamiento adaptado para sillas de ruedas: 9 de 23
- Localidades cercanas con oferta: Gijón (20 establecimientos, a 23.1 km), Mieres (2 establecimientos, a 14.2 km), Langreo (2 establecimientos, a 15.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Oviedo".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Oviedo.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 03181, 03182, 03183, 03185
- Con teléfono publicado: 19
- Franja de mayor afluencia: 10:00 a 13:00 (estimación sobre 8 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 6 de 8
- Con jornada partida (cierre al mediodía): 6 de 8
- Tarjetas de crédito: 8 de 21
- Tarjetas de débito: 8 de 21
- Pagos con móvil vía NFC: 7 de 21
- Visita rápida: 6 de 21
- Localidades cercanas con oferta: Elche (15 establecimientos, a 32.3 km), Callosa de Segura (4 establecimientos, a 23.8 km), Orihuela (4 establecimientos, a 26.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrevieja".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Torrevieja.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 30201, 30202, 30203, 30204, 30205, 30300, 30310
- Con teléfono publicado: 17
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 3 de 4
- Acceso para sillas de ruedas: 8 de 21
- Localidades cercanas con oferta: Los Alcázares (3 establecimientos, a 18.5 km), Fuente Alamo (3 establecimientos, a 20.1 km), Puerto de Mazarrón (3 establecimientos, a 24.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cartagena".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Cartagena.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 33205, 33208, 33209, 33210, 33212, 33213, 33350
- Con teléfono publicado: 18
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 9 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 9
- Con jornada partida (cierre al mediodía): 8 de 9
- Visita rápida: 14 de 20
- Tarjetas de crédito: 12 de 20
- Tarjetas de débito: 10 de 20
- Aparcamiento adaptado para sillas de ruedas: 9 de 20
- Recogida en tienda: 9 de 20
- Localidades cercanas con oferta: Oviedo (23 establecimientos, a 23.1 km), Avilés (2 establecimientos, a 20.3 km), Langreo (2 establecimientos, a 26.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Gijón".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Gijón.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 35500
- Con teléfono publicado: 16
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 15 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 13 de 15
- Con jornada partida (cierre al mediodía): 10 de 15
- Tarjetas de crédito: 12 de 20
- Visita rápida: 11 de 20
- Tarjetas de débito: 11 de 20
- Pagos con móvil vía NFC: 10 de 20
- Buenos productos: 5 de 20
- Localidades cercanas con oferta: Puerto del Carmen (1 establecimientos, a 10.9 km), Playa Blanca (1 establecimientos, a 29.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Arrecife".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Arrecife.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28981, 28982, 28983
- Con teléfono publicado: 15
- Franja de mayor afluencia: 11:00 a 14:00 (estimación sobre 10 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 10 de 10
- Con jornada partida (cierre al mediodía): 5 de 10
- Tarjetas de crédito: 8 de 20
- Tarjetas de débito: 7 de 20
- Pagos con móvil vía NFC: 6 de 20
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 20.2 km), Alcorcón (18 establecimientos, a 13.0 km), Getafe (15 establecimientos, a 8.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Parla".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Parla.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 46701, 46702
- Con teléfono publicado: 15
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 11 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 11 de 11
- Con jornada partida (cierre al mediodía): 5 de 11
- Pagos con móvil vía NFC: 8 de 20
- Tarjetas de crédito: 8 de 20
- Tarjetas de débito: 8 de 20
- Acceso para sillas de ruedas: 8 de 20
- Visita rápida: 6 de 20
- Localidades cercanas con oferta: Alzira (5 establecimientos, a 29.4 km), Dénia (4 establecimientos, a 28.9 km), Xàtiva (4 establecimientos, a 29.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Gandia".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Gandia.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008
- Con teléfono publicado: 12
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 5
- Con jornada partida (cierre al mediodía): 3 de 5
- Tarjetas de crédito: 12 de 18
- Tarjetas de débito: 10 de 18
- Pagos con móvil vía NFC: 7 de 18
- Acceso para sillas de ruedas: 5 de 18
- Localidades cercanas con oferta: Balaguer (4 establecimientos, a 24.3 km), Alcarràs (2 establecimientos, a 10.4 km), Mollerussa (2 establecimientos, a 22.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lleida".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Lleida.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28921, 28922, 28923, 28925
- Con teléfono publicado: 14
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con jornada partida (cierre al mediodía): 3 de 7
- Tarjetas de crédito: 6 de 18
- Tarjetas de débito: 5 de 18
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 13.6 km), Parla (20 establecimientos, a 13.0 km), Leganés (15 establecimientos, a 5.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcorcón".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Alcorcón.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 39001, 39002, 39006, 39007, 39008, 39009, 39010
- Con teléfono publicado: 17
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 6
- Con jornada partida (cierre al mediodía): 1 de 6
- Tarjetas de crédito: 10 de 17
- Pagos con móvil vía NFC: 9 de 17
- Recogida en tienda: 8 de 17
- Visita rápida: 8 de 17
- Tarjetas de débito: 8 de 17
- Localidades cercanas con oferta: Torrelavega (7 establecimientos, a 22.3 km), Maliaño (3 establecimientos, a 5.2 km), Santoña (2 establecimientos, a 29.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Santander".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Santander.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 47002, 47004, 47005, 47007, 47009, 47010, 47011, 47012, 47013
- Con teléfono publicado: 16
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 9 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 9
- Con jornada partida (cierre al mediodía): 9 de 9
- Pagos con móvil vía NFC: 12 de 17
- Tarjetas de crédito: 12 de 17
- Tarjetas de débito: 12 de 17
- Visita rápida: 11 de 17
- Compra en tienda: 6 de 17
- Localidades cercanas con oferta: Cabezón de Pisuerga (1 establecimientos, a 12.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Valladolid".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Valladolid.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Valladolid encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Santa Coloma de Gramenet (Barcelona) — `barcelona/santa-coloma-de-gramenet`

```
Escribe un texto de 180 a 240 palabras para la página de Santa Coloma de Gramenet de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SANTA COLOMA DE GRAMENET (no uses ningún otro):
- Total de establecimientos: 16
- Reparto: 4 locutorios, 10 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales cubiertos: 08914, 08918, 08922, 08923
- Con teléfono publicado: 12
- Franja de mayor afluencia: 16:00 a 19:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 6
- Con jornada partida (cierre al mediodía): 3 de 6
- Aparcamiento adaptado para sillas de ruedas: 7 de 16
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 5.5 km), L'Hospitalet de Llobregat (36 establecimientos, a 12.2 km), Badalona (11 establecimientos, a 1.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Santa Coloma de Gramenet".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Santa Coloma de Gramenet.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Santa Coloma de Gramenet encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Burgos (Burgos) — `burgos/burgos`

```
Escribe un texto de 180 a 240 palabras para la página de Burgos de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BURGOS (no uses ningún otro):
- Total de establecimientos: 16
- Reparto: 4 locutorios, 8 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales cubiertos: 09001, 09002, 09003, 09005, 09007
- Con teléfono publicado: 15
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 8 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 8 de 8
- Con jornada partida (cierre al mediodía): 3 de 8
- Tarjetas de débito: 7 de 16
- Acceso para sillas de ruedas: 6 de 16
- Tarjetas de crédito: 6 de 16
- Visita rápida: 5 de 16
- Pagos con móvil vía NFC: 5 de 16

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Burgos".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Burgos.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 26002, 26003, 26004, 26005
- Con teléfono publicado: 12
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 9 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 9 de 9
- Con jornada partida (cierre al mediodía): 5 de 9
- Pagos con móvil vía NFC: 9 de 16
- Tarjetas de crédito: 9 de 16
- Tarjetas de débito: 9 de 16
- Acceso para sillas de ruedas: 8 de 16
- Visita rápida: 8 de 16
- Localidades cercanas con oferta: Nájera (1 establecimientos, a 24.0 km), Lodosa (1 establecimientos, a 30.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Logroño".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Logroño.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 43001, 43002, 43006, 43007, 43100, 43130
- Con teléfono publicado: 15
- Franja de mayor afluencia: 11:00 a 14:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 6
- Con jornada partida (cierre al mediodía): 3 de 6
- Tarjetas de crédito: 6 de 16
- Localidades cercanas con oferta: Reus (12 establecimientos, a 10.8 km), Salou (6 establecimientos, a 9.4 km), Cambrils (5 establecimientos, a 15.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Tarragona".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Tarragona.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 03201, 03202, 03204, 03205, 03206
- Con teléfono publicado: 11
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 7 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 7 de 7
- Con jornada partida (cierre al mediodía): 5 de 7
- Acceso para sillas de ruedas: 8 de 15
- Tarjetas de débito: 8 de 15
- Tarjetas de crédito: 7 de 15
- Pagos con móvil vía NFC: 6 de 15
- Recogida en tienda: 4 de 15
- Localidades cercanas con oferta: Alicante (38 establecimientos, a 21.6 km), Torrevieja (21 establecimientos, a 32.3 km), Callosa de Segura (4 establecimientos, a 21.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Elche".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Elche.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Elche encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Getafe (Madrid) — `madrid/getafe`

```
Escribe un texto de 180 a 240 palabras para la página de Getafe de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GETAFE (no uses ningún otro):
- Total de establecimientos: 15
- Reparto: 11 locutorios, 3 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 28901, 28902, 28903, 28904, 28907
- Con teléfono publicado: 11
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 8 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 8
- Con jornada partida (cierre al mediodía): 3 de 8
- Visita rápida: 10 de 15
- Tarjetas de crédito: 10 de 15
- Tarjetas de débito: 9 de 15
- Pagos con móvil vía NFC: 8 de 15
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 11.6 km), Parla (20 establecimientos, a 8.6 km), Alcorcón (18 establecimientos, a 9.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Getafe".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Getafe.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28911, 28912, 28913, 28914, 28915, 28919
- Con teléfono publicado: 10
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Tarjetas de crédito: 8 de 15
- Tarjetas de débito: 8 de 15
- Visita rápida: 7 de 15
- Pagos con móvil vía NFC: 7 de 15
- A domicilio: 5 de 15
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 10.9 km), Parla (20 establecimientos, a 10.1 km), Alcorcón (18 establecimientos, a 5.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Leganés".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Leganés.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 45001, 45003, 45004, 45005, 45006, 45007
- Con teléfono publicado: 12
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con jornada partida (cierre al mediodía): 4 de 7
- Tarjetas de crédito: 6 de 15
- Tarjetas de débito: 6 de 15
- Acceso para sillas de ruedas: 4 de 15
- Aparcamiento adaptado para sillas de ruedas: 4 de 15
- Visita rápida: 4 de 15
- Localidades cercanas con oferta: Torrijos (6 establecimientos, a 25.4 km), Illescas (5 establecimientos, a 32.0 km), Fuensalida (2 establecimientos, a 25.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Toledo".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Toledo.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 02002, 02004, 02005
- Con teléfono publicado: 11
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con jornada partida (cierre al mediodía): 3 de 7
- Acceso para sillas de ruedas: 9 de 13
- Pagos con móvil vía NFC: 9 de 13
- Tarjetas de crédito: 9 de 13
- Tarjetas de débito: 9 de 13
- Visita rápida: 8 de 13
- Localidades cercanas con oferta: Tarazona de la Mancha (1 establecimientos, a 30.2 km), La Roda (1 establecimientos, a 34.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Albacete".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Albacete.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28931, 28932, 28933, 28934, 28935, 28936, 28937
- Con teléfono publicado: 9
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 4
- Con jornada partida (cierre al mediodía): 3 de 4
- Tarjetas de débito: 6 de 13
- Visita rápida: 5 de 13
- Tarjetas de crédito: 5 de 13
- Pagos con móvil vía NFC: 4 de 13
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 17.7 km), Parla (20 establecimientos, a 12.4 km), Alcorcón (18 establecimientos, a 4.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Móstoles".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Móstoles.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Móstoles encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Manresa (Barcelona) — `barcelona/manresa`

```
Escribe un texto de 180 a 240 palabras para la página de Manresa de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE MANRESA (no uses ningún otro):
- Total de establecimientos: 12
- Reparto: 7 locutorios, 2 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales cubiertos: 08241, 08242
- Con teléfono publicado: 10
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 3 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Tarjetas de crédito: 5 de 12
- Tarjetas de débito: 4 de 12
- Visita rápida: 3 de 12
- Pagos con móvil vía NFC: 3 de 12
- Compra en tienda: 3 de 12
- Localidades cercanas con oferta: Terrassa (10 establecimientos, a 23.6 km), Sabadell (10 establecimientos, a 30.3 km), Rubí (5 establecimientos, a 31.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Manresa".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Manresa.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 48901, 48903
- Con teléfono publicado: 11
- Tarjetas de crédito: 7 de 12
- Tarjetas de débito: 7 de 12
- Pagos con móvil vía NFC: 6 de 12
- Visita rápida: 5 de 12
- Recogida en tienda: 3 de 12
- Localidades cercanas con oferta: Bilbao (66 establecimientos, a 5.8 km), Algorta (5 establecimientos, a 6.6 km), Durango (4 establecimientos, a 31.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Vicente de Barakaldo".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de San Vicente de Barakaldo.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 14001, 14004, 14005, 14006, 14008, 14010
- Con teléfono publicado: 11
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Tarjetas de crédito: 9 de 12
- Acceso para sillas de ruedas: 8 de 12
- Tarjetas de débito: 8 de 12
- Pagos con móvil vía NFC: 7 de 12
- Visita rápida: 6 de 12
- Localidades cercanas con oferta: La Carlota (1 establecimientos, a 27.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Córdoba".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Córdoba.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 52002, 52003, 52004, 52005, 52006
- Con teléfono publicado: 10
- Visita rápida: 7 de 12
- Tarjetas de crédito: 6 de 12
- Pagos con móvil vía NFC: 5 de 12
- Tarjetas de débito: 5 de 12

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Melilla".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Melilla.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 43201, 43202, 43204, 43205
- Con teléfono publicado: 12
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 7 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 6 de 7
- Con jornada partida (cierre al mediodía): 3 de 7
- Tarjetas de crédito: 8 de 12
- Pagos con móvil vía NFC: 5 de 12
- Tarjetas de débito: 5 de 12
- Visita rápida: 4 de 12
- Recogida en tienda: 3 de 12
- Localidades cercanas con oferta: Tarragona (16 establecimientos, a 10.8 km), Salou (6 establecimientos, a 8.8 km), Cambrils (5 establecimientos, a 10.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Reus".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Reus.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 45600
- Con teléfono publicado: 10
- Visita rápida: 5 de 12
- Tarjetas de crédito: 5 de 12
- Tarjetas de débito: 5 de 12
- Pagos con móvil vía NFC: 3 de 12
- Amigable con la comunidad LGTBI+: 3 de 12
- Localidades cercanas con oferta: Castillo de Bayuela (1 establecimientos, a 19.6 km), Malpica de Tajo (1 establecimientos, a 25.1 km), El Casar de Escalona (1 establecimientos, a 27.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Talavera de la Reina".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Talavera de la Reina.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Talavera de la Reina encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Badalona (Barcelona) — `barcelona/badalona`

```
Escribe un texto de 180 a 240 palabras para la página de Badalona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE BADALONA (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 7 locutorios, 4 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales cubiertos: 08912, 08913, 08914, 08915, 08917, 08918
- Con teléfono publicado: 11
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 7 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 7 de 7
- Con jornada partida (cierre al mediodía): 3 de 7
- Aparcamiento adaptado para sillas de ruedas: 5 de 11
- Pagos con móvil vía NFC: 3 de 11
- Tarjetas de débito: 3 de 11
- Tarjetas de crédito: 3 de 11
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 5.9 km), L'Hospitalet de Llobregat (36 establecimientos, a 12.5 km), Santa Coloma de Gramenet (16 establecimientos, a 1.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Badalona".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Badalona.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Badalona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Donostia / San Sebastián (Gipuzkoa) — `gipuzkoa/donostia-san-sebastian`

```
Escribe un texto de 180 a 240 palabras para la página de Donostia / San Sebastián de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE DONOSTIA / SAN SEBASTIÁN (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 6 comercios con servicios relacionados
- Códigos postales cubiertos: 20002, 20003, 20006, 20007, 20011, 20012, 20015
- Con teléfono publicado: 9
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 5
- Con jornada partida (cierre al mediodía): 1 de 5
- Visita rápida: 8 de 11
- Pagos con móvil vía NFC: 8 de 11
- Tarjetas de crédito: 8 de 11
- Tarjetas de débito: 8 de 11
- Recogida en tienda: 3 de 11
- Localidades cercanas con oferta: Errenteria (9 establecimientos, a 6.1 km), Irun (5 establecimientos, a 14.8 km), Lasarte (3 establecimientos, a 6.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Donostia / San Sebastián".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Donostia / San Sebastián.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 17600
- Con teléfono publicado: 10
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 7 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 7 de 7
- Con jornada partida (cierre al mediodía): 3 de 7
- Tarjetas de crédito: 3 de 11
- Localidades cercanas con oferta: Girona (11 establecimientos, a 34.4 km), Salt (6 establecimientos, a 35.0 km), Banyoles (3 establecimientos, a 23.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Figueres".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Figueres.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Figueres encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Girona (Girona) — `girona/girona`

```
Escribe un texto de 180 a 240 palabras para la página de Girona de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE GIRONA (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 6 locutorios, 4 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 17002, 17005, 17006, 17190
- Con teléfono publicado: 10
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 1 de 3
- Con jornada partida (cierre al mediodía): 3 de 3
- Tarjetas de crédito: 5 de 11
- Tarjetas de débito: 4 de 11
- Visita rápida: 3 de 11
- Pagos con móvil vía NFC: 3 de 11
- Localidades cercanas con oferta: Figueres (11 establecimientos, a 34.4 km), Salt (6 establecimientos, a 1.1 km), Lloret de Mar (6 establecimientos, a 30.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Girona".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Girona.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Girona encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Salamanca (Salamanca) — `salamanca/salamanca`

```
Escribe un texto de 180 a 240 palabras para la página de Salamanca de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SALAMANCA (no uses ningún otro):
- Total de establecimientos: 11
- Reparto: 8 locutorios, 3 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales cubiertos: 37004, 37005, 37006, 37007, 37500
- Con teléfono publicado: 9
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 4 de 5
- Con jornada partida (cierre al mediodía): 3 de 5
- Pagos con móvil vía NFC: 4 de 11
- Tarjetas de crédito: 4 de 11
- Tarjetas de débito: 4 de 11
- Acceso para sillas de ruedas: 3 de 11
- Aseo adaptado para sillas de ruedas: 3 de 11

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Salamanca".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Salamanca.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 05001, 05003, 05005
- Con teléfono publicado: 8
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 4
- Con jornada partida (cierre al mediodía): 3 de 4
- Tarjetas de crédito: 6 de 10
- Tarjetas de débito: 6 de 10
- Visita rápida: 4 de 10
- Pagos con móvil vía NFC: 4 de 10

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ávila".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Ávila.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08200, 08202, 08203, 08204, 08206, 08207
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 3
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 16.3 km), L'Hospitalet de Llobregat (36 establecimientos, a 19.7 km), Santa Coloma de Gramenet (16 establecimientos, a 14.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Sabadell".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Sabadell.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08221, 08222, 08223, 08224, 08225, 08226
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 4
- Con jornada partida (cierre al mediodía): 2 de 4
- Tarjetas de crédito: 4 de 10
- Recogida en tienda: 3 de 10
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 21.7 km), L'Hospitalet de Llobregat (36 establecimientos, a 23.3 km), Santa Coloma de Gramenet (16 establecimientos, a 21.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Terrassa".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Terrassa.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 24002, 24004, 24006, 24008, 24009
- Con teléfono publicado: 8
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 6
- Con jornada partida (cierre al mediodía): 2 de 6
- Tarjetas de crédito: 6 de 10
- Visita rápida: 5 de 10
- Pagos con móvil vía NFC: 5 de 10
- Tarjetas de débito: 5 de 10
- A domicilio: 3 de 10
- Localidades cercanas con oferta: Valencia de Don Juan (1 establecimientos, a 34.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en León".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de León.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28802, 28803, 28804, 28806, 28807
- Con teléfono publicado: 9
- Franja de mayor afluencia: 16:00 a 19:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Tarjetas de crédito: 7 de 10
- Tarjetas de débito: 7 de 10
- Pagos con móvil vía NFC: 5 de 10
- Visita rápida: 4 de 10
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 28.2 km), Alcobendas (9 establecimientos, a 23.5 km), Torrejón de Ardoz (8 establecimientos, a 9.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcalá de Henares".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Alcalá de Henares.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 03501, 03502, 03503
- Con teléfono publicado: 5
- Franja de mayor afluencia: 20:00 a 23:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 4
- Con jornada partida (cierre al mediodía): 2 de 4
- Acceso para sillas de ruedas: 5 de 9
- Pagos con móvil vía NFC: 5 de 9
- Tarjetas de crédito: 5 de 9
- Tarjetas de débito: 5 de 9
- Localidades cercanas con oferta: Villajoyosa (5 establecimientos, a 10.0 km), Calp (4 establecimientos, a 19.2 km), Altea (2 establecimientos, a 9.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Benidorm".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Benidorm.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08940
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 5
- Con jornada partida (cierre al mediodía): 3 de 5
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 9.4 km), L'Hospitalet de Llobregat (36 establecimientos, a 2.9 km), Santa Coloma de Gramenet (16 establecimientos, a 14.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cornellà de Llobregat".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Cornellà de Llobregat.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 11201, 11203, 11204, 11207
- Con teléfono publicado: 8
- Franja de mayor afluencia: 14:00 a 17:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Localidades cercanas con oferta: San Luis de Sabinillas (4 establecimientos, a 33.1 km), Ceuta (3 establecimientos, a 29.2 km), La Línea de la Concepción (1 establecimientos, a 9.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Algeciras".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Algeciras.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Algeciras encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Errenteria (Gipuzkoa) — `gipuzkoa/errenteria`

```
Escribe un texto de 180 a 240 palabras para la página de Errenteria de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ERRENTERIA (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 8 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 20100
- Con teléfono publicado: 9
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 6 de 6
- Con jornada partida (cierre al mediodía): 3 de 6
- Visita rápida: 5 de 9
- Pagos con móvil vía NFC: 4 de 9
- Tarjetas de crédito: 4 de 9
- Tarjetas de débito: 4 de 9
- Localidades cercanas con oferta: Donostia / San Sebastián (11 establecimientos, a 6.1 km), Irun (5 establecimientos, a 9.0 km), Lasarte (3 establecimientos, a 10.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Errenteria".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Errenteria.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Errenteria encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Ibiza (Illes Balears) — `illes-balears/ibiza`

```
Escribe un texto de 180 a 240 palabras para la página de Ibiza de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE IBIZA (no uses ningún otro):
- Total de establecimientos: 9
- Reparto: 6 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 07800
- Con teléfono publicado: 7
- Tarjetas de crédito: 6 de 9
- A domicilio: 4 de 9
- Tarjetas de débito: 4 de 9
- Pagos con móvil vía NFC: 3 de 9
- Localidades cercanas con oferta: Sant Antoni de Portmany (3 establecimientos, a 13.4 km), Santa Eulària des Riu (2 establecimientos, a 12.4 km), Playa d'en Bossa (1 establecimientos, a 2.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ibiza".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Ibiza.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 27001, 27002, 27003, 27004, 27297
- Con teléfono publicado: 8
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 8 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 8 de 8
- Con jornada partida (cierre al mediodía): 6 de 8
- Visita rápida: 6 de 9
- Tarjetas de crédito: 6 de 9
- Pagos con móvil vía NFC: 5 de 9
- Tarjetas de débito: 5 de 9
- Recogida en tienda: 3 de 9
- Localidades cercanas con oferta: Sarria (1 establecimientos, a 28.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lugo".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Lugo.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28100
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 6 de 6
- Con jornada partida (cierre al mediodía): 5 de 6
- Pagos con móvil vía NFC: 5 de 9
- Tarjetas de crédito: 5 de 9
- Tarjetas de débito: 5 de 9
- Visita rápida: 3 de 9
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 15.2 km), Alcorcón (18 establecimientos, a 26.8 km), Leganés (15 establecimientos, a 25.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcobendas".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Alcobendas.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 04002, 04004, 04005, 04008, 04009
- Con teléfono publicado: 7
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 6 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 6 de 6
- Con jornada partida (cierre al mediodía): 2 de 6
- Acceso para sillas de ruedas: 4 de 8
- Pagos con móvil vía NFC: 4 de 8
- Tarjetas de débito: 4 de 8
- Tarjetas de crédito: 4 de 8
- Compra en tienda: 2 de 8
- Localidades cercanas con oferta: El Ejido (8 establecimientos, a 30.0 km), Roquetas de Mar (6 establecimientos, a 17.0 km), El Parador de las Hortichuelas (3 establecimientos, a 13.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Almería".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Almería.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 04700, 04716, 04717
- Con teléfono publicado: 2
- Acceso para sillas de ruedas: 2 de 8
- Localidades cercanas con oferta: Almería (8 establecimientos, a 30.0 km), Roquetas de Mar (6 establecimientos, a 14.1 km), El Parador de las Hortichuelas (3 establecimientos, a 16.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en El Ejido".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de El Ejido.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08500
- Con teléfono publicado: 7
- Franja de mayor afluencia: 13:00 a 16:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Pagos con móvil vía NFC: 4 de 8
- Tarjetas de crédito: 4 de 8
- Tarjetas de débito: 4 de 8
- Localidades cercanas con oferta: Manlleu (3 establecimientos, a 8.9 km), Sant Celoni (2 establecimientos, a 32.9 km), Cardedeu (2 establecimientos, a 33.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vic".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Vic.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 11401, 11402, 11403, 11404, 11407
- Con teléfono publicado: 6
- Visita rápida: 6 de 8
- Tarjetas de crédito: 5 de 8
- Pagos con móvil vía NFC: 4 de 8
- Tarjetas de débito: 4 de 8
- Acceso para sillas de ruedas: 4 de 8
- Localidades cercanas con oferta: El Puerto de Sta María (2 establecimientos, a 13.2 km), Chiclana de la Frontera (2 establecimientos, a 29.5 km), El (1 establecimientos, a 13.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Jerez de la Frontera".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Jerez de la Frontera.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Jerez de la Frontera encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Castellón de la Plana (Castellon) — `castellon/castellon-de-la-plana`

```
Escribe un texto de 180 a 240 palabras para la página de Castellón de la Plana de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE CASTELLÓN DE LA PLANA (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 1 locutorios, 6 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 12001, 12002, 12004, 12006
- Con teléfono publicado: 7
- Acceso para sillas de ruedas: 5 de 8
- Localidades cercanas con oferta: Villarreal (4 establecimientos, a 7.4 km), Borriana (4 establecimientos, a 11.7 km), Almassora (2 establecimientos, a 4.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Castellón de la Plana".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Castellón de la Plana.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Castellón de la Plana encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Lepe (Huelva) — `huelva/lepe`

```
Escribe un texto de 180 a 240 palabras para la página de Lepe de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LEPE (no uses ningún otro):
- Total de establecimientos: 8
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales cubiertos: 21440
- Con teléfono publicado: 6
- Recogida en tienda: 2 de 8
- Compra en tienda: 2 de 8
- Localidades cercanas con oferta: Cartaya (4 establecimientos, a 5.6 km), Huelva (4 establecimientos, a 22.9 km), Moguer (2 establecimientos, a 32.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lepe".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Lepe.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 35007, 35008, 35011, 35012
- Con teléfono publicado: 6
- Tarjetas de crédito: 6 de 8
- Tarjetas de débito: 6 de 8
- Visita rápida: 5 de 8
- Pagos con móvil vía NFC: 5 de 8
- Amigable con la comunidad LGTBI+: 3 de 8
- Localidades cercanas con oferta: Vecindario (2 establecimientos, a 30.7 km), Telde (1 establecimientos, a 15.0 km), Santa Lucía de Tirajana (1 establecimientos, a 30.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Las Palmas de Gran Canaria".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Las Palmas de Gran Canaria.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28941, 28942, 28943, 28944, 28945
- Con teléfono publicado: 8
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 6 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 5 de 6
- Con jornada partida (cierre al mediodía): 3 de 6
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 16.8 km), Parla (20 establecimientos, a 5.7 km), Alcorcón (18 establecimientos, a 7.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Fuenlabrada".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Fuenlabrada.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28850
- Con teléfono publicado: 5
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 4
- Con jornada partida (cierre al mediodía): 2 de 4
- Tarjetas de crédito: 4 de 8
- Tarjetas de débito: 4 de 8
- Compra en tienda: 3 de 8
- Pagos con móvil vía NFC: 3 de 8
- Visita rápida: 2 de 8
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 18.6 km), Parla (20 establecimientos, a 34.4 km), Alcorcón (18 establecimientos, a 32.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrejón de Ardoz".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Torrejón de Ardoz.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 30500
- Con teléfono publicado: 7
- Pagos con móvil vía NFC: 5 de 8
- Tarjetas de débito: 4 de 8
- Tarjetas de crédito: 4 de 8
- Recogida en tienda: 3 de 8
- Compra en tienda: 3 de 8
- Localidades cercanas con oferta: Murcia (39 establecimientos, a 10.5 km), Archena (6 establecimientos, a 10.3 km), Orihuela (4 establecimientos, a 23.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Molina de Segura".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Molina de Segura.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 31010
- Con teléfono publicado: 5
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 5
- Con jornada partida (cierre al mediodía): 2 de 5
- Tarjetas de crédito: 6 de 8
- Pagos con móvil vía NFC: 5 de 8
- Tarjetas de débito: 5 de 8
- Visita rápida: 4 de 8
- Localidades cercanas con oferta: Pamplona (33 establecimientos, a 2.9 km), Tafalla (3 establecimientos, a 30.5 km), Burlada (2 establecimientos, a 5.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Barañáin".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Barañáin.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 31500
- Con teléfono publicado: 6
- Visita rápida: 3 de 8
- Pagos con móvil vía NFC: 2 de 8
- Tarjetas de débito: 2 de 8
- Tarjetas de crédito: 2 de 8
- Localidades cercanas con oferta: Alfaro (2 establecimientos, a 17.8 km), Villafranca (2 establecimientos, a 27.0 km), Caparroso (2 establecimientos, a 31.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Tudela".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Tudela.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Tudela encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Torrelavega (Cantabria) — `cantabria/torrelavega`

```
Escribe un texto de 180 a 240 palabras para la página de Torrelavega de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE TORRELAVEGA (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 1 locutorios, 2 especializados en envío de dinero, 4 comercios con servicios relacionados
- Códigos postales cubiertos: 39300
- Con teléfono publicado: 7
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 2 de 3
- Con jornada partida (cierre al mediodía): 3 de 3
- Visita rápida: 4 de 7
- Tarjetas de crédito: 4 de 7
- Tarjetas de débito: 4 de 7
- Pagos con móvil vía NFC: 3 de 7
- Aseo adaptado para sillas de ruedas: 2 de 7
- Localidades cercanas con oferta: Santander (17 establecimientos, a 22.3 km), Maliaño (3 establecimientos, a 18.1 km), Los Corrales de Buelna (2 establecimientos, a 10.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrelavega".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Torrelavega.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 13001, 13002, 13003, 13004
- Con teléfono publicado: 7
- Acceso para sillas de ruedas: 4 de 7
- Aseo adaptado para sillas de ruedas: 3 de 7
- Asientos adaptados sillas de ruedas: 3 de 7
- Visita rápida: 3 de 7
- Pagos con móvil vía NFC: 3 de 7
- Localidades cercanas con oferta: Bolaños de Calatrava (3 establecimientos, a 20.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ciudad Real".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Ciudad Real.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 19002, 19003, 19004
- Con teléfono publicado: 6
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 2 de 3
- Tarjetas de crédito: 5 de 7
- Pagos con móvil vía NFC: 4 de 7
- Tarjetas de débito: 4 de 7
- Visita rápida: 4 de 7
- Acceso para sillas de ruedas: 2 de 7
- Localidades cercanas con oferta: Alcalá de Henares (10 establecimientos, a 23.2 km), Torrejón de Ardoz (8 establecimientos, a 32.2 km), Azuqueca de Henares (6 establecimientos, a 10.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Guadalajara".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Guadalajara.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 22001
- Con teléfono publicado: 5
- Tarjetas de crédito: 4 de 7
- Tarjetas de débito: 3 de 7
- Visita rápida: 2 de 7

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Huesca".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Huesca.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28400
- Con teléfono publicado: 6
- Pagos con móvil vía NFC: 4 de 7
- Tarjetas de crédito: 4 de 7
- Tarjetas de débito: 4 de 7
- A domicilio: 3 de 7
- Visita rápida: 2 de 7
- Localidades cercanas con oferta: Alcorcón (18 establecimientos, a 34.8 km), Alcobendas (9 establecimientos, a 32.5 km), Colmenar Viejo (7 establecimientos, a 20.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Collado Villalba".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Collado Villalba.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28770
- Con teléfono publicado: 6
- Pagos con móvil vía NFC: 5 de 7
- Tarjetas de crédito: 5 de 7
- Tarjetas de débito: 5 de 7
- Visita rápida: 4 de 7
- Recogida en tienda: 2 de 7
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 28.4 km), Alcorcón (18 establecimientos, a 35.0 km), Alcobendas (9 establecimientos, a 17.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Colmenar Viejo".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Colmenar Viejo.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 29601, 29602, 29603
- Con teléfono publicado: 5
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 4 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 2 de 4
- Tarjetas de crédito: 3 de 7
- Tarjetas de débito: 2 de 7
- Visita rápida: 2 de 7
- Localidades cercanas con oferta: Fuengirola (6 establecimientos, a 23.4 km), San Pedro Alcántara (5 establecimientos, a 9.9 km), Estepona (5 establecimientos, a 25.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Marbella".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Marbella.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Marbella encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Isidro (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/san-isidro`

```
Escribe un texto de 180 a 240 palabras para la página de San Isidro de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN ISIDRO (no uses ningún otro):
- Total de establecimientos: 7
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales cubiertos: 38611
- Con teléfono publicado: 6
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Visita rápida: 5 de 7
- Pagos con móvil vía NFC: 5 de 7
- Tarjetas de crédito: 5 de 7
- Tarjetas de débito: 5 de 7
- Recogida en tienda: 3 de 7
- Localidades cercanas con oferta: Arona (3 establecimientos, a 13.6 km), Adeje (2 establecimientos, a 17.2 km), San Isidro de Abona (1 establecimientos, a 0.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Isidro".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de San Isidro.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Total de establecimientos: 6
- Reparto: 3 locutorios, 2 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 15003, 15006, 15010
- Con teléfono publicado: 6
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 3
- Con jornada partida (cierre al mediodía): 1 de 3
- Acceso para sillas de ruedas: 3 de 6
- Visita rápida: 3 de 6
- Pagos con móvil vía NFC: 3 de 6
- Tarjetas de crédito: 3 de 6
- Tarjetas de débito: 3 de 6
- Localidades cercanas con oferta: Culleredo (2 establecimientos, a 4.8 km), Coruña ( A ) (1 establecimientos, a 0.7 km), Arteixo (1 establecimientos, a 9.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en A Coruña".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de A Coruña.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En A Coruña encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Roquetas de Mar (Almeria) — `almeria/roquetas-de-mar`

```
Escribe un texto de 180 a 240 palabras para la página de Roquetas de Mar de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE ROQUETAS DE MAR (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 0 locutorios, 3 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales cubiertos: 04740
- Con teléfono publicado: 3
- Acceso para sillas de ruedas: 2 de 6
- Localidades cercanas con oferta: El Ejido (8 establecimientos, a 14.1 km), Almería (8 establecimientos, a 17.1 km), El Parador de las Hortichuelas (3 establecimientos, a 5.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Roquetas de Mar".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Roquetas de Mar.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08302, 08303, 08304
- Con teléfono publicado: 5
- Tarjetas de crédito: 3 de 6
- Tarjetas de débito: 3 de 6
- Pagos con móvil vía NFC: 2 de 6
- Visita rápida: 2 de 6
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 26.4 km), L'Hospitalet de Llobregat (36 establecimientos, a 33.0 km), Santa Coloma de Gramenet (16 establecimientos, a 21.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Mataró".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Mataró.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08800
- Con teléfono publicado: 6
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 2 de 3
- Con jornada partida (cierre al mediodía): 1 de 3
- Pagos con móvil vía NFC: 4 de 6
- Tarjetas de crédito: 4 de 6
- Tarjetas de débito: 4 de 6
- Acceso para sillas de ruedas: 3 de 6
- Visita rápida: 3 de 6
- Localidades cercanas con oferta: Cornellà de Llobregat (9 establecimientos, a 33.4 km), Vilafranca del Penedès (5 establecimientos, a 13.9 km), Viladecans (4 establecimientos, a 26.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vilanova i la Geltrú".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Vilanova i la Geltrú.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 17310
- Con teléfono publicado: 4
- Tarjetas de crédito: 4 de 6
- Acceso para sillas de ruedas: 2 de 6
- Visita rápida: 2 de 6
- Tarjetas de débito: 2 de 6
- Localidades cercanas con oferta: Girona (11 establecimientos, a 30.8 km), Salt (6 establecimientos, a 30.8 km), Pineda de Mar (4 establecimientos, a 15.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Lloret de Mar".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Lloret de Mar.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Lloret de Mar encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Salt (Girona) — `girona/salt`

```
Escribe un texto de 180 a 240 palabras para la página de Salt de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SALT (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales cubiertos: 17190
- Con teléfono publicado: 5
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 3 de 3
- Pagos con móvil vía NFC: 3 de 6
- Tarjetas de crédito: 3 de 6
- Tarjetas de débito: 3 de 6
- Localidades cercanas con oferta: Girona (11 establecimientos, a 1.1 km), Figueres (11 establecimientos, a 35.0 km), Lloret de Mar (6 establecimientos, a 30.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Salt".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Salt.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Salt encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Azuqueca de Henares (Guadalajara) — `guadalajara/azuqueca-de-henares`

```
Escribe un texto de 180 a 240 palabras para la página de Azuqueca de Henares de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE AZUQUECA DE HENARES (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 2 locutorios, 1 especializados en envío de dinero, 3 comercios con servicios relacionados
- Códigos postales cubiertos: 19200
- Con teléfono publicado: 5
- Franja de mayor afluencia: 12:00 a 15:00 (estimación sobre 3 locales)
- Franja más tranquila: 17:00 a 19:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 2 de 3
- Pagos con móvil vía NFC: 4 de 6
- Tarjetas de crédito: 4 de 6
- Tarjetas de débito: 4 de 6
- Visita rápida: 3 de 6
- Acceso para sillas de ruedas: 2 de 6
- Localidades cercanas con oferta: Alcalá de Henares (10 establecimientos, a 12.7 km), Alcobendas (9 establecimientos, a 31.6 km), Torrejón de Ardoz (8 establecimientos, a 21.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Azuqueca de Henares".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Azuqueca de Henares.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 35600
- Con teléfono publicado: 4
- Visita rápida: 4 de 6
- Pagos con móvil vía NFC: 4 de 6
- Tarjetas de crédito: 4 de 6
- Tarjetas de débito: 4 de 6
- Buenos productos: 2 de 6
- Localidades cercanas con oferta: Corralejo (1 establecimientos, a 26.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Puerto del Rosario".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Puerto del Rosario.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28701
- Con teléfono publicado: 6
- Franja de mayor afluencia: 13:00 a 16:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 1 de 3
- Pagos con móvil vía NFC: 5 de 6
- Tarjetas de crédito: 5 de 6
- Tarjetas de débito: 5 de 6
- Visita rápida: 2 de 6
- Recogida en tienda: 2 de 6
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 15.9 km), Alcorcón (18 establecimientos, a 27.8 km), Leganés (15 establecimientos, a 26.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Sebastián de los Reyes".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de San Sebastián de los Reyes.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 29640, 29651
- Con teléfono publicado: 4
- Pagos con móvil vía NFC: los 6
- Tarjetas de crédito: los 6
- Tarjetas de débito: los 6
- Visita rápida: 3 de 6
- Acceso para sillas de ruedas: 2 de 6
- Localidades cercanas con oferta: Málaga (30 establecimientos, a 25.5 km), Marbella (7 establecimientos, a 23.4 km), San Pedro Alcántara (5 establecimientos, a 33.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Fuengirola".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Fuengirola.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 30600
- Con teléfono publicado: 4
- Visita rápida: 2 de 6
- Acceso para sillas de ruedas: 2 de 6
- Localidades cercanas con oferta: Murcia (39 establecimientos, a 20.8 km), Molina de Segura (8 establecimientos, a 10.3 km), Orihuela (4 establecimientos, a 31.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Archena".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Archena.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 30850
- Con teléfono publicado: 5
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 5 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 5
- Con jornada partida (cierre al mediodía): 2 de 5
- Visita rápida: 5 de 6
- Tarjetas de crédito: 4 de 6
- Tarjetas de débito: 4 de 6
- Pagos con móvil vía NFC: 3 de 6
- Acceso para sillas de ruedas: 2 de 6
- Localidades cercanas con oferta: Lorca (26 establecimientos, a 20.1 km), Mazarrón (3 establecimientos, a 25.0 km), Fuente Alamo (3 establecimientos, a 29.1 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Totana".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Totana.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Totana encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Santa Cruz de Tenerife (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/santa-cruz-de-tenerife`

```
Escribe un texto de 180 a 240 palabras para la página de Santa Cruz de Tenerife de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SANTA CRUZ DE TENERIFE (no uses ningún otro):
- Total de establecimientos: 6
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 38003, 38005, 38006, 38007
- Con teléfono publicado: 6
- Tarjetas de crédito: 5 de 6
- Tarjetas de débito: 5 de 6
- Pagos con móvil vía NFC: 4 de 6
- Aparcamiento adaptado para sillas de ruedas: 3 de 6
- Visita rápida: 3 de 6
- Localidades cercanas con oferta: La Laguna (5 establecimientos, a 4.4 km), Taco (1 establecimientos, a 4.0 km), Candelaria (1 establecimientos, a 16.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Santa Cruz de Tenerife".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Santa Cruz de Tenerife.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 40001, 40002, 40005, 40006
- Con teléfono publicado: 5
- Recogida en tienda: 3 de 6
- Compra en tienda: 3 de 6
- Visita rápida: 3 de 6
- Pagos con móvil vía NFC: 3 de 6
- Tarjetas de crédito: 3 de 6
- Localidades cercanas con oferta: Moralzarzal (1 establecimientos, a 31.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Segovia".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Segovia.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 43840
- Con teléfono publicado: 6
- Tarjetas de crédito: 5 de 6
- Acceso para sillas de ruedas: 4 de 6
- Visita rápida: 3 de 6
- Tarjetas de débito: 3 de 6
- A domicilio: 2 de 6
- Localidades cercanas con oferta: Tarragona (16 establecimientos, a 9.4 km), Reus (12 establecimientos, a 8.8 km), Cambrils (5 establecimientos, a 7.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Salou".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Salou.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 45500
- Con teléfono publicado: 5
- Localidades cercanas con oferta: Toledo (15 establecimientos, a 25.4 km), Fuensalida (2 establecimientos, a 9.8 km), Santa Olalla (1 establecimientos, a 13.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Torrijos".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Torrijos.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Torrijos encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### Villajoyosa (Alicante) — `alicante/villajoyosa`

```
Escribe un texto de 180 a 240 palabras para la página de Villajoyosa de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE VILLAJOYOSA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 3 locutorios, 0 especializados en envío de dinero, 2 comercios con servicios relacionados
- Códigos postales cubiertos: 03570
- Con teléfono publicado: 3
- Recogida en tienda: 2 de 5
- Pagos con móvil vía NFC: 2 de 5
- Tarjetas de crédito: 2 de 5
- Tarjetas de débito: 2 de 5
- Localidades cercanas con oferta: Alicante (38 establecimientos, a 27.4 km), Benidorm (9 establecimientos, a 10.0 km), Calp (4 establecimientos, a 29.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Villajoyosa".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Villajoyosa.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08210
- Con teléfono publicado: 5
- Acceso para sillas de ruedas: 2 de 5
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 12.7 km), L'Hospitalet de Llobregat (36 establecimientos, a 16.5 km), Santa Coloma de Gramenet (16 establecimientos, a 10.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Barberà del Vallès".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Barberà del Vallès.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08291
- Con teléfono publicado: 3
- Aparcamiento adaptado para sillas de ruedas: 2 de 5
- Recogida en tienda: 2 de 5
- Servicios de reparación: 2 de 5
- Visita rápida: 2 de 5
- Aparatos electrónicos: 2 de 5
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 9.6 km), L'Hospitalet de Llobregat (36 establecimientos, a 14.6 km), Santa Coloma de Gramenet (16 establecimientos, a 7.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Ripollet".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Ripollet.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08191
- Con teléfono publicado: 4
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 3 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 2 de 3
- Recogida en tienda: 2 de 5
- Compra en tienda: 2 de 5
- Pagos con móvil vía NFC: 2 de 5
- Tarjetas de débito: 2 de 5
- Aparcamiento adaptado para sillas de ruedas: 2 de 5
- Localidades cercanas con oferta: Barcelona (84 establecimientos, a 14.4 km), L'Hospitalet de Llobregat (36 establecimientos, a 14.6 km), Santa Coloma de Gramenet (16 establecimientos, a 15.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Rubí".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Rubí.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 08720
- Con teléfono publicado: 4
- Franja de mayor afluencia: 17:00 a 20:00 (estimación sobre 3 locales)
- Franja más tranquila: 14:00 a 16:00
- Con actividad registrada en domingo: 2 de 3
- Con jornada partida (cierre al mediodía): 2 de 3
- Acceso para sillas de ruedas: 4 de 5
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de crédito: 3 de 5
- Tarjetas de débito: 3 de 5
- Recogida en tienda: 2 de 5
- Localidades cercanas con oferta: L'Hospitalet de Llobregat (36 establecimientos, a 34.4 km), Cornellà de Llobregat (9 establecimientos, a 31.7 km), Vilanova i la Geltrú (6 establecimientos, a 13.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Vilafranca del Penedès".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Vilafranca del Penedès.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 48991
- Con teléfono publicado: 5
- Franja de mayor afluencia: 19:00 a 22:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 2 de 3
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de débito: 3 de 5
- Tarjetas de crédito: 3 de 5
- Visita rápida: 2 de 5
- Localidades cercanas con oferta: Bilbao (66 establecimientos, a 11.9 km), San Vicente de Barakaldo (12 establecimientos, a 6.6 km), Santurtzi (3 establecimientos, a 3.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Algorta".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Algorta.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 10001, 10002
- Con teléfono publicado: 5
- Tarjetas de crédito: 3 de 5
- Visita rápida: 2 de 5
- Pagos con móvil vía NFC: 2 de 5
- Tarjetas de débito: 2 de 5

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cáceres".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Cáceres.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 16001, 16003, 16004
- Con teléfono publicado: 4
- Tarjetas de crédito: 3 de 5
- Tarjetas de débito: 3 de 5
- Visita rápida: 2 de 5
- Pagos con móvil vía NFC: 2 de 5

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cuenca".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Cuenca.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 20301, 20302
- Con teléfono publicado: 5
- Visita rápida: 4 de 5
- Tarjetas de crédito: 4 de 5
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de débito: 3 de 5
- Compra en tienda: 2 de 5
- Localidades cercanas con oferta: Donostia / San Sebastián (11 establecimientos, a 14.8 km), Errenteria (9 establecimientos, a 9.0 km), Lasarte (3 establecimientos, a 19.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Irun".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Irun.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 07300
- Con teléfono publicado: 5
- Tarjetas de crédito: 2 de 5
- Tarjetas de débito: 2 de 5
- Localidades cercanas con oferta: Palma (57 establecimientos, a 27.0 km), Manacor (4 establecimientos, a 30.7 km), Sóller (2 establecimientos, a 18.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Inca".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Inca.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28500
- Con teléfono publicado: 2
- Tarjetas de crédito: 2 de 5
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 23.8 km), Parla (20 establecimientos, a 28.1 km), Alcorcón (18 establecimientos, a 32.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Arganda del Rey".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Arganda del Rey.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28220
- Con teléfono publicado: 5
- Franja de mayor afluencia: 15:00 a 18:00 (estimación sobre 4 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Visita rápida: 3 de 5
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de crédito: 3 de 5
- Tarjetas de débito: 3 de 5
- Compra en tienda: 2 de 5
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 13.7 km), Parla (20 establecimientos, a 25.3 km), Alcorcón (18 establecimientos, a 12.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Majadahonda".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Majadahonda.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 28830
- Con teléfono publicado: 4
- Pagos con móvil vía NFC: 4 de 5
- Tarjetas de crédito: 4 de 5
- Tarjetas de débito: 4 de 5
- Compra en tienda: 3 de 5
- Visita rápida: 3 de 5
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 13.2 km), Parla (20 establecimientos, a 28.7 km), Alcorcón (18 establecimientos, a 26.3 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Fernando de Henares".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de San Fernando de Henares.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 29680
- Con teléfono publicado: 5
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 9:00 a 11:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 1 de 3
- Visita rápida: 3 de 5
- Tarjetas de crédito: 3 de 5
- Recogida en tienda: 2 de 5
- Acceso para sillas de ruedas: 2 de 5
- Pagos con móvil vía NFC: 2 de 5
- Localidades cercanas con oferta: Marbella (7 establecimientos, a 25.5 km), San Pedro Alcántara (5 establecimientos, a 15.7 km), San Luis de Sabinillas (4 establecimientos, a 9.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Estepona".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Estepona.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 29670
- Con teléfono publicado: 4
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 4 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 4 de 4
- Con jornada partida (cierre al mediodía): 1 de 4
- Visita rápida: 4 de 5
- Tarjetas de crédito: 4 de 5
- Tarjetas de débito: 4 de 5
- Acceso para sillas de ruedas: 2 de 5
- Pagos con móvil vía NFC: 2 de 5
- Localidades cercanas con oferta: Marbella (7 establecimientos, a 9.9 km), Fuengirola (6 establecimientos, a 33.2 km), Estepona (5 establecimientos, a 15.6 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Pedro Alcántara".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de San Pedro Alcántara.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 30880
- Con teléfono publicado: 3
- Franja de mayor afluencia: 18:00 a 21:00 (estimación sobre 3 locales)
- Franja más tranquila: 15:00 a 17:00
- Con actividad registrada en domingo: 3 de 3
- Con jornada partida (cierre al mediodía): 2 de 3
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de crédito: 3 de 5
- Tarjetas de débito: 3 de 5
- Visita rápida: 2 de 5
- Localidades cercanas con oferta: Lorca (26 establecimientos, a 31.3 km), Pulpí (3 establecimientos, a 14.3 km), Vera (3 establecimientos, a 30.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Águilas".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Águilas.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 34002, 34005
- Con teléfono publicado: 5
- Tarjetas de crédito: 3 de 5
- Tarjetas de débito: 3 de 5
- Pagos con móvil vía NFC: 2 de 5
- Localidades cercanas con oferta: Paredes de Nava (1 establecimientos, a 20.9 km), Cabezón de Pisuerga (1 establecimientos, a 30.9 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Palencia".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Palencia.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Palencia encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### La Laguna (Santa Cruz de Tenerife) — `santa-cruz-de-tenerife/la-laguna`

```
Escribe un texto de 180 a 240 palabras para la página de La Laguna de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE LA LAGUNA (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 0 especializados en envío de dinero, 1 comercios con servicios relacionados
- Códigos postales cubiertos: 38108, 38204, 38320
- Con teléfono publicado: 3
- Tarjetas de crédito: 4 de 5
- Aparcamiento adaptado para sillas de ruedas: 3 de 5
- Visita rápida: 3 de 5
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de débito: 3 de 5
- Localidades cercanas con oferta: Santa Cruz de Tenerife (6 establecimientos, a 4.4 km), Taco (1 establecimientos, a 2.2 km), Candelaria (1 establecimientos, a 13.8 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en La Laguna".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de La Laguna.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En La Laguna encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```

### San Juan de Aznalfarache (Sevilla) — `sevilla/san-juan-de-aznalfarache`

```
Escribe un texto de 180 a 240 palabras para la página de San Juan de Aznalfarache de un
directorio español de locutorios y puntos de envío de dinero.

DATOS REALES DE SAN JUAN DE AZNALFARACHE (no uses ningún otro):
- Total de establecimientos: 5
- Reparto: 4 locutorios, 1 especializados en envío de dinero, 0 comercios con servicios relacionados
- Códigos postales cubiertos: 41920
- Con teléfono publicado: 4
- Pagos con móvil vía NFC: 4 de 5
- Tarjetas de crédito: 4 de 5
- Tarjetas de débito: 4 de 5
- Visita rápida: 3 de 5
- Acceso para sillas de ruedas: 2 de 5
- Localidades cercanas con oferta: Sevilla (70 establecimientos, a 6.4 km), Castilleja de la Cuesta (3 establecimientos, a 3.4 km), Camas (2 establecimientos, a 4.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en San Juan de Aznalfarache".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de San Juan de Aznalfarache.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 42001, 42004
- Con teléfono publicado: 5
- Visita rápida: 4 de 5
- Pagos con móvil vía NFC: 4 de 5
- Tarjetas de crédito: 4 de 5
- Tarjetas de débito: 4 de 5
- Acceso para sillas de ruedas: 2 de 5
- Localidades cercanas con oferta: Almazán (1 establecimientos, a 31.7 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Soria".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Soria.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 43870
- Con teléfono publicado: 5
- Visita rápida: 4 de 5
- Tarjetas de crédito: 4 de 5
- Pagos con móvil vía NFC: 3 de 5
- Tarjetas de débito: 3 de 5
- Recogida en tienda: 2 de 5
- Localidades cercanas con oferta: Tortosa (5 establecimientos, a 12.6 km), Benicarló (4 establecimientos, a 34.7 km), L'Ametlla de Mar (2 establecimientos, a 27.2 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Amposta".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Amposta.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 43850
- Con teléfono publicado: 4
- Tarjetas de crédito: 4 de 5
- Tarjetas de débito: 3 de 5
- Acceso para sillas de ruedas: 2 de 5
- Visita rápida: 2 de 5
- Pagos con móvil vía NFC: 2 de 5
- Localidades cercanas con oferta: Tarragona (16 establecimientos, a 16.0 km), Reus (12 establecimientos, a 10.1 km), Salou (6 establecimientos, a 7.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Cambrils".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Cambrils.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 43500
- Con teléfono publicado: 5
- Acceso para sillas de ruedas: 2 de 5
- Localidades cercanas con oferta: Amposta (5 establecimientos, a 12.6 km), Móra d'Ebre (3 establecimientos, a 32.4 km), L'Ametlla de Mar (2 establecimientos, a 25.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Tortosa".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Tortosa.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 44600
- Con teléfono publicado: 5
- Localidades cercanas con oferta: Caspe (1 establecimientos, a 22.0 km), Alcorisa (1 establecimientos, a 27.4 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alcañiz".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Alcañiz.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 45200
- Con teléfono publicado: 3
- Visita rápida: 2 de 5
- Tarjetas de crédito: 2 de 5
- Localidades cercanas con oferta: Madrid (271 establecimientos, a 34.7 km), Parla (20 establecimientos, a 14.6 km), Alcorcón (18 establecimientos, a 25.0 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Illescas".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Illescas.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
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
- Códigos postales cubiertos: 46600
- Con teléfono publicado: 4
- Localidades cercanas con oferta: Gandia (20 establecimientos, a 29.4 km), Xàtiva (4 establecimientos, a 19.6 km), Torrent (4 establecimientos, a 31.5 km)

REQUISITOS
- Español de España, tono informativo y sobrio. Nada de marketing.
- Empieza por lo que le sirve a alguien que busca "locutorios en Alzira".
- Usa al menos tres de los datos de arriba de forma natural, integrados en la
  frase, no como una lista.
- Un encabezado "## " a mitad del texto, con un título específico de Alzira.
- Menciona que los locutorios hoy funcionan sobre todo como puntos de envío de
  dinero, recargas de móvil y papelería, no como cabinas de llamadas.

PROHIBIDO
- Inventar horarios, comisiones, precios o nombres de operadores de remesas.
- Nombrar establecimientos concretos.
- Afirmar nada sobre la calidad del trato o del servicio.
- Frases de relleno tipo "en el corazón de la ciudad" o "una amplia variedad de
  servicios para satisfacer todas tus necesidades".
- Empezar con "Si estás buscando" o "En Alzira encontrarás".

Devuelve solo el texto en markdown, sin comentarios ni comillas.
```
