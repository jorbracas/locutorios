import type { AgregadoCiudad } from '@/lib/data';

/*
  Preguntas frecuentes de la localidad.

  Se generan a partir de los datos agregados, nunca a mano y nunca inventadas:
  cada respuesta sale de un recuento real sobre los establecimientos de esa
  localidad. Por eso el texto cambia de una ciudad a otra sin ser una plantilla
  con el nombre intercambiado.

  Es tambien la pieza que ataca el long-tail donde el pack de Maps no compite:
  "locutorio abierto domingo en X", "locutorio que acepte tarjeta en X",
  "a que hora hay menos cola en el locutorio". Esas consultas se resuelven con
  texto, no con un mapa.
*/

export type Pregunta = { pregunta: string; respuesta: string };

export function construirPreguntas(
  ciudad: string,
  datos: AgregadoCiudad,
): Pregunta[] {
  const preguntas: Pregunta[] = [];
  const { total, tipos, actividad, atributos, conTelefono, vecinas } = datos;

  // 1. Cuantos hay. La consulta cabecera de la pagina.
  preguntas.push({
    pregunta: `¿Cuántos locutorios hay en ${ciudad}?`,
    respuesta:
      total === 1
        ? `Tenemos registrado un establecimiento en ${ciudad} con servicios de locutorio o envío de dinero. Puedes ver su dirección y su teléfono en esta misma página.`
        : `Tenemos registrados ${total} establecimientos en ${ciudad}: ${tipos.locutorio} ${
            tipos.locutorio === 1 ? 'locutorio' : 'locutorios'
          }, ${tipos.envio} ${
            tipos.envio === 1
              ? 'punto especializado en envío de dinero'
              : 'puntos especializados en envío de dinero'
          }${
            tipos.otros > 0
              ? ` y ${tipos.otros} ${
                  tipos.otros === 1
                    ? 'comercio con servicios relacionados'
                    : 'comercios con servicios relacionados'
                }`
              : ''
          }. Todos aparecen listados en esta página con su dirección.`,
  });

  // 2. Envio de dinero: la intencion comercial real del sector.
  const conEnvio = tipos.envio + tipos.locutorio;
  if (conEnvio > 0) {
    preguntas.push({
      pregunta: `¿Dónde puedo enviar dinero al extranjero desde ${ciudad}?`,
      respuesta: `En ${ciudad} hay ${conEnvio} ${
        conEnvio === 1 ? 'establecimiento' : 'establecimientos'
      } donde se tramitan envíos de dinero, entre locutorios y oficinas especializadas. Las comisiones varían según el operador y el país de destino, así que conviene preguntar el importe final antes de cerrar la operación.`,
    });
  }

  // 3. Domingo: consulta muy repetida y que el pack no responde bien.
  if (actividad && actividad.abrenDomingo > 0) {
    preguntas.push({
      pregunta: `¿Hay algún locutorio abierto los domingos en ${ciudad}?`,
      respuesta: `Se ha registrado actividad en domingo en ${actividad.abrenDomingo} de los ${actividad.muestra} establecimientos de ${ciudad} de los que tenemos datos de afluencia. No es un horario oficial, así que conviene llamar antes de desplazarse.`,
    });
  }

  // 4. Cola: intencion practica pura.
  if (actividad) {
    preguntas.push({
      pregunta: `¿A qué hora hay menos cola en los locutorios de ${ciudad}?`,
      respuesta: `La franja con menos movimiento suele ser de ${actividad.franjaTranquila}, mientras que la de mayor afluencia va de ${actividad.franjaPunta}. Son estimaciones basadas en la actividad registrada, no en horarios declarados por los locales.`,
    });
  }

  // 5. Pago con tarjeta.
  const tarjeta = atributos.find((a) => a.valor.toLowerCase().includes('tarjeta'));
  if (tarjeta) {
    preguntas.push({
      pregunta: `¿Se puede pagar con tarjeta en los locutorios de ${ciudad}?`,
      respuesta: tarjeta.todos
        ? `Los ${tarjeta.total} establecimientos de ${ciudad} de los que tenemos información admiten pago con ${tarjeta.valor.toLowerCase()}. Aun así, para importes pequeños algunos locales prefieren efectivo.`
        : `${tarjeta.cantidad} de los ${tarjeta.total} establecimientos de ${ciudad} admiten pago con ${tarjeta.valor.toLowerCase()}. En el resto conviene llevar efectivo.`,
    });
  }

  // 6. Accesibilidad.
  const accesible = atributos.find((a) => a.grupo === 'Accesibilidad');
  if (accesible) {
    preguntas.push({
      pregunta: `¿Hay locutorios accesibles en ${ciudad}?`,
      respuesta: `${accesible.cantidad} de los ${accesible.total} establecimientos registrados en ${ciudad} indican disponer de ${accesible.valor.toLowerCase()}. Cada ficha detalla las características concretas del local.`,
    });
  }

  // 7. Telefono, solo cuando falta en una parte apreciable.
  if (conTelefono > 0 && conTelefono < total) {
    preguntas.push({
      pregunta: `¿Puedo llamar antes de ir?`,
      respuesta: `${conTelefono} de los ${total} establecimientos de ${ciudad} tienen teléfono publicado. Como los horarios de estos negocios cambian con frecuencia y no siempre están actualizados, llamar antes es la forma más fiable de no hacer el viaje en balde.`,
    });
  }

  // 8. Alternativa cercana. Clave en las 442 localidades con un solo local.
  if (vecinas.length > 0 && total <= 3) {
    const mejor = vecinas[0];
    preguntas.push({
      pregunta: `¿Y si no encuentro lo que busco en ${ciudad}?`,
      respuesta: `La localidad más cercana con más oferta es ${mejor.nombre}, a unos ${mejor.distancia} km, donde hay ${mejor.total} establecimientos registrados. Es la alternativa más práctica si necesitas un servicio concreto que aquí no se ofrece.`,
    });
  }

  return preguntas;
}

export default function PreguntasCiudad({ preguntas }: { preguntas: Pregunta[] }) {
  if (!preguntas.length) return null;

  return (
    <section className="mt-12">
      <h2 className="mb-5 text-xl">Preguntas frecuentes</h2>

      <div className="divide-y divide-linea overflow-hidden rounded-xl border border-linea bg-papel-alto">
        {preguntas.map((item) => (
          <details key={item.pregunta} className="group">
            <summary className="cursor-pointer list-none px-4 py-3.5 font-medium hover:text-verde">
              <span className="flex items-start justify-between gap-3">
                {item.pregunta}
                <span
                  aria-hidden="true"
                  className="mt-0.5 shrink-0 text-humo transition-transform group-open:rotate-45"
                >
                  +
                </span>
              </span>
            </summary>
            <p className="px-4 pb-4 text-sm text-humo">{item.respuesta}</p>
          </details>
        ))}
      </div>
    </section>
  );
}
