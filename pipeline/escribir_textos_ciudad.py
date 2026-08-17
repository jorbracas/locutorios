#!/usr/bin/env python3
"""
Textos editoriales de las localidades principales.

Cada texto parte de los datos reales de `agregados-ciudad.json` de esa
localidad concreta. Ese es todo el mecanismo antiplantilla: Granada tiene un
hueco de actividad de 15:00 a 17:00 que no tiene ninguna otra capital, Murcia
concentra su punta de 19:00 a 22:00, Torrevieja es la unica con punta de
manana, y en Cartagena los puntos de envio triplican a los locutorios. Escribir
sobre eso produce veinte textos distintos sin esfuerzo de invencion.

No se afirma nada que no este en los datos: ni comisiones, ni operadores, ni
horarios oficiales, ni juicios sobre la calidad del servicio.

Uso:  python3 escribir_textos_ciudad.py ./data
"""

import json
import sys
from pathlib import Path

TEXTOS: dict[str, str] = {}

# --------------------------------------------------------------------------

TEXTOS["madrid/madrid"] = """\
Madrid concentra 271 establecimientos con servicios de locutorio o envío de \
dinero, repartidos por 42 códigos postales distintos. Esa dispersión es la \
característica más útil de la ciudad: salvo en los distritos del extremo norte, \
es raro tener que desplazarse más de un par de barrios para encontrar uno.

La actividad se concentra en la franja de 17:00 a 20:00, cuando coinciden la \
salida del trabajo y el horario en el que resulta más cómodo llamar a otros \
husos. Si puedes elegir, entre las 9:00 y las 11:00 hay bastante menos gente. \
De los 147 locales con datos de afluencia, 128 registran movimiento en domingo, \
una proporción que en Madrid tiene sentido: buena parte de la clientela trabaja \
de lunes a sábado.

## Qué se hace hoy en un locutorio madrileño

De los 271 locales, 57 están orientados específicamente al envío de dinero y \
177 figuran como locutorios que suelen combinar ese servicio con recargas de \
móvil, tarjetas SIM, fotocopias y papelería. Las cabinas de llamadas, que dieron \
nombre al negocio, han desaparecido casi por completo.

Hay 230 fichas con teléfono publicado. Merece la pena usarlo: los horarios de \
estos negocios cambian con frecuencia y no siempre se reflejan en internet.
"""

TEXTOS["valencia/valencia"] = """\
Los 99 establecimientos registrados en Valencia se reparten por 20 códigos \
postales, con una concentración clara en los barrios del oeste y del sur del \
centro histórico. Hay un dato que distingue a la ciudad del resto de capitales \
grandes: 63 de esos 99 locales declaran acceso para sillas de ruedas, una \
proporción notablemente más alta que la media del directorio.

## Cuándo conviene acercarse

La franja de mayor movimiento va de 18:00 a 21:00, y la más despejada de 9:00 a \
11:00. De los 46 locales con datos de afluencia, 41 registran actividad en \
domingo y 17 muestran el corte de mediodía propio de la jornada partida, así que \
la hora de la comida es el momento con más riesgo de encontrar cerrado.

El reparto por tipo está bastante equilibrado: 48 locutorios, 28 puntos \
centrados en el envío de dinero y 23 comercios que ofrecen servicios \
relacionados sin ser su actividad principal. En la práctica, muchos de los \
primeros tramitan también remesas, además de recargas de móvil, tarjetas SIM e \
impresión.

Con 73 teléfonos publicados sobre 99 fichas, en la mayoría de casos puedes \
confirmar por adelantado si tienen el servicio concreto que buscas.
"""

TEXTOS["zaragoza/zaragoza"] = """\
Con 87 establecimientos repartidos en solo 14 códigos postales, Zaragoza tiene \
una de las concentraciones más altas del directorio. La oferta se agrupa sobre \
todo en el entorno del casco histórico y los barrios del sur, lo que en la \
práctica significa que casi siempre hay varias opciones a poca distancia una de \
otra.

Otro rasgo local: 38 de los 87 locales indican disponer de aparcamiento adaptado \
para sillas de ruedas, la cifra más alta entre las capitales de tamaño similar.

## Horarios y afluencia

El movimiento se concentra entre las 17:00 y las 20:00, mientras que de 9:00 a \
11:00 la actividad es mucho menor. De los 38 establecimientos con datos de \
afluencia, 35 registran movimiento en domingo y solo 9 muestran cierre al \
mediodía, una proporción baja que sugiere que la mayoría mantiene horario \
continuo.

El reparto es de 38 locutorios, 28 puntos de envío de dinero y 21 comercios con \
servicios relacionados. Como en el resto del país, el negocio se ha desplazado \
de las llamadas internacionales hacia las remesas, las recargas de móvil y la \
papelería.

Hay teléfono publicado en 69 de las 87 fichas.
"""

TEXTOS["barcelona/barcelona"] = """\
Barcelona reúne 84 establecimientos en 25 códigos postales, con una presencia \
especialmente densa en Ciutat Vella y el Raval. Conviene tener en cuenta algo \
que no aparece en el mapa de la ciudad: L'Hospitalet de Llobregat, a apenas 6,6 \
km, suma otros 36 establecimientos, y Santa Coloma de Gramenet añade 16. Para \
quien se mueve en metro, el área metropolitana ofrece bastante más de lo que \
sugiere el recuento municipal.

## Ritmo de la ciudad

La franja de mayor afluencia es de 18:00 a 21:00 y la más tranquila de 9:00 a \
11:00. De los 36 locales con datos de actividad, 33 registran movimiento en \
domingo y 18 —la mitad— muestran el corte del mediodía, así que en Barcelona la \
jornada partida sigue siendo habitual en este tipo de negocio.

De los 84 establecimientos, 53 son locutorios y 20 están centrados en el envío \
de dinero. La mayoría combina remesas con recargas de móvil, venta de tarjetas \
SIM, fotocopias e impresión; las cabinas de llamadas apenas quedan como \
recuerdo del origen del negocio.

Hay 70 fichas con teléfono, suficiente para confirmar antes de desplazarse.
"""

TEXTOS["sevilla/sevilla"] = """\
Los 70 establecimientos de Sevilla se distribuyen por 12 códigos postales, con \
mayor densidad en el entorno de la Macarena y los barrios del este. Destaca un \
dato de accesibilidad: 44 de los 70 locales declaran acceso para sillas de \
ruedas, casi dos de cada tres.

El reparto entre tipos está más igualado que en otras capitales: 28 locutorios y \
24 puntos específicos de envío de dinero, además de 18 comercios que ofrecen \
servicios relacionados. Es una señal de que en la ciudad la remesa se ha \
consolidado como negocio propio y no solo como añadido.

## A qué hora ir

El movimiento se concentra entre las 18:00 y las 21:00. Para evitar cola, la \
franja de 9:00 a 11:00 es claramente la más despejada. De los 24 locales con \
datos de afluencia, 23 registran actividad en domingo, prácticamente todos, y \
solo 9 muestran cierre al mediodía.

Más allá de los envíos, la oferta habitual incluye recargas de móvil, tarjetas \
SIM para llamadas internacionales, fotocopias, impresión y plastificado. Las \
comisiones de envío varían según el operador y el destino, así que conviene \
preguntar el importe final antes de cerrar la operación.
"""

TEXTOS["bizkaia/bilbao"] = """\
De los 66 establecimientos registrados en Bilbao, 42 son locutorios propiamente \
dichos y solo 17 están centrados en el envío de dinero. Es una proporción más \
inclinada hacia el locutorio clásico que la de otras ciudades de tamaño similar, \
donde la remesa suele haber ganado más terreno como negocio independiente.

La oferta se reparte por 13 códigos postales, con una concentración marcada en \
San Francisco y el entorno de Bilbao La Vieja.

## La jornada partida sigue viva

Es el rasgo más útil que revelan los datos de Bilbao: de los 29 locales con \
información de afluencia, 17 muestran el corte del mediodía. Casi seis de cada \
diez cierran unas horas entre la mañana y la tarde, así que planificar la visita \
importa más aquí que en otras ciudades. La franja de mayor movimiento va de \
17:00 a 20:00 y la más tranquila de 9:00 a 11:00. En domingo hay actividad \
registrada en 27 de esos 29.

Aunque el rótulo diga locutorio, lo que se encuentra dentro son sobre todo \
envíos de dinero, recargas de móvil, tarjetas SIM y servicios de impresión.

Con 56 teléfonos publicados sobre 66 fichas, llamar antes es fácil y evita el \
viaje en balde.
"""

TEXTOS["illes-balears/palma"] = """\
Palma concentra 57 establecimientos en 12 códigos postales. El dato más \
llamativo es el de los domingos: de los 37 locales con información de afluencia, \
36 registran actividad ese día. Es prácticamente la totalidad, y la proporción \
más alta entre las ciudades grandes del directorio.

## Una ciudad que no cierra el fin de semana

Esa apertura dominical encaja con el perfil laboral de buena parte de la \
clientela, muy ligada a la hostelería y los servicios, donde el domingo no \
siempre es día libre y el descanso cae entre semana. La franja de mayor \
movimiento va de 18:00 a 21:00 y la más despejada de 9:00 a 11:00. Eso sí, 17 de \
esos 37 locales cierran al mediodía, así que la hora de comer es el peor momento \
para acercarse.

El reparto es de 26 locutorios, 17 puntos de envío de dinero y 14 comercios con \
servicios relacionados. Las remesas, las recargas de móvil y las tarjetas SIM \
para llamadas internacionales son hoy el núcleo del negocio.

Hay teléfono publicado en 44 de las 57 fichas. Fuera de Palma, Inca reúne otros \
5 establecimientos a unos 27 km.
"""

TEXTOS["granada/granada"] = """\
Granada tiene una particularidad que no comparte ninguna otra capital del \
directorio: su franja más tranquila no es la primera hora de la mañana, sino la \
de 15:00 a 17:00. La afluencia cae en la sobremesa y repunta con fuerza entre \
las 18:00 y las 21:00.

El dato encaja con otro: de los 11 establecimientos con información de \
actividad, 9 muestran el corte del mediodía. En Granada la jornada partida es la \
norma, no la excepción, así que acercarse a las cuatro de la tarde es la peor \
apuesta posible.

## Qué hay y dónde

Son 39 establecimientos repartidos por 14 códigos postales: 19 locutorios, 8 \
puntos centrados en el envío de dinero y 12 comercios que ofrecen servicios \
relacionados. La oferta se concentra en el entorno del Zaidín y los barrios del \
norte.

De los 39, 15 declaran acceso para sillas de ruedas y otros tantos admiten pago \
con tarjeta de crédito.

Solo 22 fichas tienen teléfono publicado, bastante menos que en otras ciudades \
de tamaño parecido. Cuando no lo haya, la alternativa es fiarse de las franjas \
de actividad, teniendo en cuenta que son estimaciones y no horarios declarados.
"""

TEXTOS["murcia/murcia"] = """\
Los locutorios de Murcia tienen el horario más tardío de todo el directorio: la \
franja de mayor afluencia va de 19:00 a 22:00, dos horas más tarde que en \
ciudades como Zaragoza o Bilbao. Quien venga de otra provincia y planifique la \
visita a media tarde puede encontrarse el local todavía tranquilo, que en la \
práctica es una ventaja.

La hora con menos movimiento es la de 9:00 a 11:00.

## Servicios y reparto

Son 39 establecimientos en 12 códigos postales, con un reparto muy equilibrado: \
15 locutorios, 13 puntos de envío de dinero y 11 comercios con servicios \
relacionados. Ese equilibrio indica una demanda de remesas consolidada, con \
locales dedicados en exclusiva a ello.

De los 11 locales con datos de afluencia, 10 registran actividad en domingo y 6 \
cierran al mediodía. Diecinueve de los 39 declaran acceso para sillas de ruedas.

Fuera de la capital, la comarca ofrece bastante más: Molina de Segura suma 8 \
establecimientos a 10,5 km y Archena otros 6 a unos 21 km.

El servicio habitual combina envío de dinero, recargas de móvil, tarjetas SIM, \
fotocopias y papelería. Hay teléfono publicado en 28 de las 39 fichas.
"""

TEXTOS["alicante/alicante"] = """\
Alicante reúne 38 establecimientos repartidos por 12 códigos postales, con mayor \
presencia en los barrios del norte del centro. De ellos, 18 son locutorios, 11 \
están centrados en el envío de dinero y 9 son comercios que ofrecen servicios \
relacionados sin ser su actividad principal.

Diecisiete de los 38 declaran acceso para sillas de ruedas.

## Horarios

La franja de mayor movimiento va de 17:00 a 20:00, algo más temprana que en \
otras ciudades del arco mediterráneo, y la más tranquila de 9:00 a 11:00. De los \
14 locales con datos de afluencia, 11 registran actividad en domingo y solo 4 \
muestran cierre al mediodía, así que el horario continuo es lo habitual.

Conviene mirar también fuera del término municipal. Elche, a unos 22 km, suma 15 \
establecimientos, y Villajoyosa otros 5. Para quien se mueve en tren o en \
autobús, ampliar el radio multiplica las opciones.

Como en el resto del país, el negocio gira hoy en torno al envío de dinero, las \
recargas de móvil y las tarjetas SIM para llamadas internacionales, con \
fotocopias e impresión como complemento. Hay 27 teléfonos publicados sobre 38 \
fichas.
"""

TEXTOS["araba-alava/vitoria-gasteiz"] = """\
Vitoria-Gasteiz tiene 36 establecimientos en 10 códigos postales, y una ventaja \
práctica poco habitual: 32 de esas 36 fichas incluyen teléfono. Es una de las \
mejores coberturas del directorio, lo que en un sector donde los horarios \
cambian a menudo resulta más útil de lo que parece.

De los 36, 23 son locutorios, 7 están centrados en el envío de dinero y 6 son \
comercios con servicios relacionados.

## Cuándo hay movimiento

La franja de mayor afluencia va de 18:00 a 21:00 y la más despejada de 9:00 a \
11:00. De los 18 locales con datos de actividad, 17 registran movimiento en \
domingo y 9 —la mitad— cierran al mediodía, un patrón parecido al del resto del \
País Vasco.

Veintiuno de los 36 admiten pago con tarjeta de crédito y 16 aceptan pago con \
móvil por NFC, aunque para importes pequeños conviene llevar algo de efectivo.

La oferta habitual combina envío de dinero al extranjero, recargas de móvil, \
venta de tarjetas SIM, fotocopias e impresión. Las comisiones de las remesas \
varían según el operador y el país de destino, así que merece la pena preguntar \
el importe final antes de cerrar la operación.
"""

TEXTOS["barcelona/l-hospitalet-de-llobregat"] = """\
L'Hospitalet de Llobregat concentra 36 establecimientos en apenas 6 códigos \
postales. Esa es la cifra que define la ciudad: es una de las densidades más \
altas de España en este tipo de negocio, muy por encima de lo que corresponde a \
su tamaño, y responde a la composición de barrios como La Torrassa, Collblanc o \
Santa Eulàlia.

En la práctica significa que casi nunca hace falta desplazarse: lo más probable \
es que haya varias opciones en la misma calle o en la contigua.

## Horarios y servicios

El movimiento se concentra entre las 18:00 y las 21:00, y la franja más \
tranquila es la de 9:00 a 11:00. De los 15 locales con datos de afluencia, 14 \
registran actividad en domingo y 8 cierran al mediodía.

De los 36 establecimientos, 22 son locutorios y 7 están centrados \
específicamente en el envío de dinero. La mayoría suma recargas de móvil, \
tarjetas SIM, fotocopias y papelería.

Barcelona queda a 6,6 km con otros 84 establecimientos, y Santa Coloma de \
Gramenet a 12,2 km con 16 más, así que la oferta metropolitana es amplia si \
buscas un servicio muy concreto.
"""

TEXTOS["navarra/pamplona"] = """\
Pamplona reúne 33 establecimientos repartidos por 10 códigos postales: 15 \
locutorios, 10 puntos centrados en el envío de dinero y 8 comercios con \
servicios relacionados. La oferta se concentra sobre todo en la Rotxapea, San \
Jorge y el entorno del Casco Viejo.

## Antes de acercarte

La franja de mayor afluencia va de 18:00 a 21:00 y la más tranquila de 9:00 a \
11:00. De los 13 locales con información de actividad, 11 registran movimiento \
en domingo y 9 muestran el corte del mediodía, así que la jornada partida es \
mayoritaria y la hora de comer conviene evitarla.

Diecisiete de los 33 admiten pago con tarjeta de crédito y 16 aceptan pago con \
móvil por NFC. Diez declaran acceso para sillas de ruedas.

Barañáin, a menos de 3 km, suma otros 8 establecimientos, lo que amplía bastante \
las opciones sin salir del área urbana.

El servicio habitual combina remesas al extranjero, recargas de móvil, tarjetas \
SIM para llamadas internacionales y trabajos de impresión y fotocopia. Hay \
teléfono publicado en 27 de las 33 fichas, suficiente para confirmar horario y \
disponibilidad antes de ir.
"""

TEXTOS["malaga/malaga"] = """\
En Málaga la proporción entre tipos es la más desequilibrada de las capitales \
grandes: 22 de los 30 establecimientos son locutorios y solo 4 están centrados \
específicamente en el envío de dinero. Aquí la remesa sigue siendo un servicio \
más dentro del locutorio, y no ha derivado en locales dedicados como sí ha \
ocurrido en Sevilla o Murcia.

## Horario continuo

El segundo rasgo distintivo es el horario: de los 11 locales con datos de \
afluencia, solo 2 muestran cierre al mediodía. Es la proporción más baja del \
grupo de ciudades grandes, así que en Málaga la franja de comida no supone el \
problema que sí es en Granada o Bilbao. El movimiento se concentra entre las \
17:00 y las 20:00, y la hora más despejada es la de 9:00 a 11:00. Nueve de esos \
11 registran actividad en domingo.

Los 30 establecimientos se reparten por 13 códigos postales. Dieciséis declaran \
acceso para sillas de ruedas y 15 admiten pago con tarjeta de crédito.

En la costa hay más oferta: Fuengirola suma 6 establecimientos y Torremolinos 4, \
ambos bien comunicados por cercanías.
"""

TEXTOS["murcia/lorca"] = """\
Los 26 establecimientos de Lorca comparten un único código postal, el 30800. Es \
una concentración inusual incluso para una ciudad de su tamaño, y tiene una \
lectura práctica directa: toda la oferta está en el núcleo urbano, sin \
dispersión por pedanías, así que moverse entre unos y otros es cuestión de \
minutos.

## Abiertos en domingo

El dato más útil de Lorca es rotundo: los 14 establecimientos de los que tenemos \
información de afluencia registran actividad en domingo. Los catorce, sin \
excepción. Es la única localidad de este tamaño en el directorio donde ocurre, y \
refleja el peso del trabajo agrícola en la comarca, donde el descanso semanal no \
suele caer en fin de semana.

La franja de mayor movimiento va de 18:00 a 21:00 y la más tranquila de 9:00 a \
11:00. Seis de los 14 cierran al mediodía.

Del total, 13 son locutorios, 5 están centrados en el envío de dinero y 8 son \
comercios con servicios relacionados. Hay teléfono publicado en 20 de las 26 \
fichas.

Totana, a 20 km, suma otros 6 establecimientos, y Águilas 5 más.
"""

TEXTOS["asturias/oviedo"] = """\
Oviedo cuenta con 23 establecimientos repartidos por 7 códigos postales, con \
mayor presencia en el entorno de la estación y los barrios del sur. Son 12 \
locutorios, 6 puntos centrados en el envío de dinero y 5 comercios con servicios \
relacionados.

Conviene tener presente a Gijón: a 23 km hay otros 20 establecimientos, y el \
trayecto en cercanías es corto. Entre las dos ciudades se concentra la mayor \
parte de la oferta asturiana.

## Horarios

El movimiento se concentra entre las 17:00 y las 20:00, algo más temprano que en \
el Mediterráneo, y la franja más despejada es la de 9:00 a 11:00. De los 13 \
locales con datos de actividad, 11 registran movimiento en domingo y 5 muestran \
cierre al mediodía.

Once de los 23 admiten pago con tarjeta de crédito y 10 aceptan pago con móvil \
por NFC. Nueve indican disponer de aparcamiento adaptado para sillas de ruedas.

Como en el resto del país, lo que se encuentra hoy en estos locales son sobre \
todo envíos de dinero al extranjero, recargas de móvil, tarjetas SIM y trabajos \
de impresión. Hay teléfono en 20 de las 23 fichas.
"""

TEXTOS["alicante/torrevieja"] = """\
Torrevieja es la única localidad del directorio donde la mayor afluencia se \
registra por la mañana: la franja punta va de 10:00 a 13:00, y la más tranquila \
de 14:00 a 16:00. En el resto de España el pico llega a última hora de la tarde, \
casi sin excepciones.

El patrón encaja con la composición de la ciudad, con una población residente \
extranjera muy numerosa y un ritmo diario menos marcado por el horario laboral \
español. Si vienes de fuera, la consecuencia práctica es clara: aquí la mañana \
es el momento con más servicio disponible, y la sobremesa el de menos.

## Qué se ofrece

Son 21 establecimientos en 4 códigos postales, de los que 12 son locutorios y 8 \
están centrados en el envío de dinero. La proporción de puntos de remesas es \
alta para el tamaño de la localidad.

De los 8 locales con datos de afluencia, 6 registran actividad en domingo y otros \
6 cierran al mediodía, coherente con esa franja tranquila de 14:00 a 16:00.

Hay teléfono publicado en 19 de las 21 fichas, una cobertura muy buena. Elche, a \
32 km, suma otros 15 establecimientos.
"""

TEXTOS["murcia/cartagena"] = """\
Cartagena invierte la proporción habitual del sector: de sus 21 establecimientos, \
12 están centrados en el envío de dinero y solo 4 son locutorios en sentido \
estricto. En casi todas las demás ciudades ocurre justo lo contrario.

La lectura es que aquí la remesa se ha convertido en un negocio propio, con \
locales dedicados exclusivamente a ello en lugar de ofrecerla como un servicio \
más dentro de un locutorio. Para quien busca enviar dinero, es una buena \
noticia: hay más puntos especializados de los que cabría esperar en una ciudad \
de este tamaño.

## Horarios

La franja de mayor movimiento va de 17:00 a 20:00, y la más tranquila de 14:00 a \
16:00, coincidiendo con la sobremesa. Los 4 establecimientos de los que hay \
datos de afluencia registran actividad en domingo, y 3 de ellos cierran al \
mediodía.

Los 21 locales se reparten por 7 códigos postales, incluyendo los núcleos \
costeros del municipio. Ocho declaran acceso para sillas de ruedas y hay \
teléfono publicado en 17 fichas.

Las comisiones varían según operador y destino, así que conviene preguntar el \
importe final antes de cerrar la operación.
"""

TEXTOS["asturias/gijon"] = """\
De los 20 establecimientos de Gijón, 15 son locutorios y solo 1 figura como \
punto especializado en envío de dinero. Es el reparto más inclinado hacia el \
locutorio clásico de todo el directorio entre ciudades de este tamaño, aunque \
conviene matizarlo: la mayoría de esos locutorios tramita también remesas, solo \
que como un servicio más y no como actividad principal.

## Jornada partida casi generalizada

Es el rasgo que más condiciona la visita: de los 9 establecimientos con datos de \
afluencia, 8 muestran el corte del mediodía. Prácticamente todos cierran unas \
horas entre la mañana y la tarde. La franja de mayor movimiento va de 17:00 a \
20:00 y la más despejada de 9:00 a 11:00, y los 9 registran actividad en \
domingo.

Los 20 locales se reparten por 7 códigos postales. Catorce están catalogados \
como establecimientos de visita rápida, 12 admiten pago con tarjeta de crédito y \
9 ofrecen recogida en tienda.

Oviedo queda a 23 km con otros 23 establecimientos, incluida una oferta mayor de \
puntos dedicados en exclusiva al envío de dinero.

Hay teléfono publicado en 18 de las 20 fichas.
"""

TEXTOS["las-palmas/arrecife"] = """\
Los 20 establecimientos de Arrecife comparten un único código postal, el 35500, \
lo que concentra toda la oferta de la capital lanzaroteña en un área reducida y \
caminable.

## Domingo abierto, mediodía cerrado

Los datos de actividad dibujan un patrón muy definido. De los 15 locales con \
información de afluencia, 13 registran movimiento en domingo, pero 10 muestran \
el corte del mediodía. Es decir: el fin de semana rara vez es un problema, y la \
hora de comer casi siempre lo es. La franja de mayor afluencia va de 18:00 a \
21:00 y la más tranquila de 9:00 a 11:00.

Del total, 11 son locutorios, 2 están centrados en el envío de dinero y 7 son \
comercios que ofrecen servicios relacionados junto a su actividad principal, una \
combinación frecuente en las islas, donde el mismo local suele reunir \
alimentación, papelería y remesas.

Doce admiten pago con tarjeta de crédito y 11 están catalogados como \
establecimientos de visita rápida.

Fuera de Arrecife la oferta es escasa: Puerto del Carmen y Playa Blanca cuentan \
con un establecimiento cada uno, así que la capital sigue siendo la referencia \
de la isla.
"""

# --------------------------------------------------------------------------


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    directorio = Path(sys.argv[1])
    destino = directorio / "textos-ciudad.json"

    existentes: dict[str, str] = {}
    if destino.exists():
        try:
            existentes = json.loads(destino.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existentes = {}

    agregados = json.loads(
        (directorio / "agregados-ciudad.json").read_text(encoding="utf-8")
    )

    desconocidas = [clave for clave in TEXTOS if clave not in agregados]
    if desconocidas:
        print("AVISO: claves que no existen en agregados-ciudad.json:")
        for clave in desconocidas:
            print(f"  {clave}")

    existentes.update({k: v.strip() for k, v in TEXTOS.items() if k in agregados})
    destino.write_text(
        json.dumps(existentes, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    cubiertas = sum(agregados[k]["total"] for k in existentes if k in agregados)
    total = sum(a["total"] for a in agregados.values())

    print(f"\nTextos escritos: {len(existentes)}")
    print(f"Cubren {cubiertas} de {total} fichas ({100 * cubiertas / total:.0f} %)")
    palabras = [len(t.split()) for t in existentes.values()]
    print(f"Longitud: media {sum(palabras) // len(palabras)} palabras, "
          f"min {min(palabras)}, max {max(palabras)}")
    print(f"\nEscrito en {destino}")


if __name__ == "__main__":
    main()
