import type { AgregadoCiudad } from '@/lib/data';

/*
  Preguntas frecuentes de la localidad.

  Se generan a partir de los datos agregados, nunca a mano y nunca inventadas:
  cada respuesta sale de un recuento real sobre los establecimientos de esa
  localidad. Por eso el texto cambia de una ciudad a otra sin ser una plantilla
  con el nombre intercambiado.

  La actividad observada se mantiene separada de los horarios oficiales. Una
  curva de afluencia permite comparar tramos, pero no confirmar apertura.
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
  if (tipos.envio > 0) {
    preguntas.push({
      pregunta: `¿Dónde puedo enviar dinero al extranjero desde ${ciudad}?`,
      respuesta: `En ${ciudad} hay ${tipos.envio} ${
        tipos.envio === 1
          ? 'establecimiento clasificado como punto especializado en envío de dinero'
          : 'establecimientos clasificados como puntos especializados en envío de dinero'
      }. El servicio y sus condiciones deben confirmarse directamente con cada local.`,
    });
  }

  // 3. Domingo: se responde con afluencia, sin convertirla en apertura.
  if (actividad && actividad.abrenDomingo > 0) {
    preguntas.push({
      pregunta: `¿Se registra actividad en domingo en los locutorios de ${ciudad}?`,
      respuesta: `Se observa actividad en domingo en ${actividad.abrenDomingo} de los ${actividad.muestra} establecimientos de la muestra de ${ciudad}. Este dato de afluencia no confirma el horario ni que un local concreto esté abierto.`,
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
        ? `Los ${tarjeta.total} establecimientos de ${ciudad} tienen publicado el atributo «${tarjeta.valor.toLowerCase()}». La forma de pago debe confirmarse antes de acudir.`
        : `${tarjeta.cantidad} de los ${tarjeta.total} establecimientos de ${ciudad} tienen publicado el atributo «${tarjeta.valor.toLowerCase()}». Que no aparezca en los demás no permite concluir que no acepten tarjeta.`,
    });
  }

  // 6. Accesibilidad.
  const accesible = atributos.find((a) => a.grupo === 'Accesibilidad');
  if (accesible) {
    preguntas.push({
      pregunta: `¿Hay locutorios accesibles en ${ciudad}?`,
      respuesta: `${accesible.cantidad} de los ${accesible.total} establecimientos registrados en ${ciudad} tienen publicado «${accesible.valor.toLowerCase()}». En los demás casos conviene confirmar la accesibilidad directamente.`,
    });
  }

  // 7. Telefono, solo cuando falta en una parte apreciable.
  if (conTelefono > 0 && conTelefono < total) {
    preguntas.push({
      pregunta: `¿Puedo llamar antes de ir?`,
      respuesta: `${conTelefono} de los ${total} establecimientos de ${ciudad} tienen teléfono publicado. Llamar permite confirmar el horario y el servicio concreto antes de desplazarse.`,
    });
  }

  // 8. Alternativa cercana. Clave en las 442 localidades con un solo local.
  if (vecinas.length > 0 && total <= 3) {
    const mejor = vecinas[0];
    preguntas.push({
      pregunta: `¿Y si no encuentro lo que busco en ${ciudad}?`,
      respuesta: `La referencia cercana con más oferta es ${mejor.nombre}, a ${mejor.distancia} km, con ${mejor.total} establecimientos registrados. Puede ampliar las opciones, pero el servicio concreto debe comprobarse antes de ir.`,
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
