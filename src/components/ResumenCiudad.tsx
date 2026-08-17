import type { AgregadoCiudad } from '@/lib/data';

/*
  Ficha resumen de la localidad.

  Este bloque es lo que diferencia una pagina de localidad de las otras 802.
  No lo hace con redaccion, sino con hechos calculados sobre los propios
  establecimientos: cuantos aceptan tarjeta, cuantos abren domingo, en que
  franja hay mas cola, que codigos postales cubre.

  Ademas de diferenciar, responde directamente al long-tail por el que se puede
  competir de verdad: "locutorio abierto domingo en X", "locutorio que acepte
  tarjeta en X". Ninguna de esas consultas la resuelve el pack de Maps.
*/

type Props = {
  ciudad: string;
  datos: AgregadoCiudad;
};

function Dato({
  valor,
  etiqueta,
  detalle,
}: {
  valor: string;
  etiqueta: string;
  detalle?: string;
}) {
  return (
    <div className="border-l-2 border-verde pl-3">
      <p className="font-[family-name:var(--font-display)] text-2xl leading-none font-extrabold">
        {valor}
      </p>
      <p className="mt-1 text-sm font-medium">{etiqueta}</p>
      {detalle ? <p className="text-micro text-humo">{detalle}</p> : null}
    </div>
  );
}

export default function ResumenCiudad({ ciudad, datos }: Props) {
  const { tipos, actividad, atributos, codigosPostales, conTelefono, total } = datos;

  // Solo se muestran los atributos de pago y accesibilidad, que son los que
  // condicionan si merece la pena desplazarse. El resto es ruido.
  const relevantes = atributos.filter((atributo) =>
    ['Pagos', 'Accesibilidad', 'Servicios', 'Opciones de servicio'].includes(atributo.grupo),
  );

  return (
    <section className="mb-10 rounded-xl border border-linea bg-papel-alto p-5 sm:p-6">
      <h2 className="mb-5 text-xl">Los locutorios de {ciudad} en datos</h2>

      <div className="grid grid-cols-2 gap-5 sm:grid-cols-4">
        <Dato
          valor={String(total)}
          etiqueta={total === 1 ? 'establecimiento' : 'establecimientos'}
          detalle={codigosPostales.length > 1 ? `en ${codigosPostales.length} códigos postales` : undefined}
        />

        {tipos.envio > 0 && (
          <Dato
            valor={String(tipos.envio + tipos.locutorio)}
            etiqueta="con envío de dinero"
            detalle={tipos.envio > 0 ? `${tipos.envio} especializados` : undefined}
          />
        )}

        {actividad && actividad.abrenDomingo > 0 && (
          <Dato
            valor={String(actividad.abrenDomingo)}
            etiqueta="abren en domingo"
            detalle={`de ${actividad.muestra} con datos`}
          />
        )}

        {conTelefono > 0 && (
          <Dato
            valor={String(conTelefono)}
            etiqueta="con teléfono"
            detalle="para confirmar antes de ir"
          />
        )}
      </div>

      {(actividad || relevantes.length > 0) && (
        <dl className="mt-6 space-y-2.5 border-t border-linea pt-5 text-sm">
          {actividad && (
            <>
              <div className="flex flex-col gap-0.5 sm:flex-row sm:gap-4">
                <dt className="shrink-0 text-humo sm:w-44">Franja con más movimiento</dt>
                <dd className="font-[family-name:var(--font-dato)]">{actividad.franjaPunta}</dd>
              </div>
              <div className="flex flex-col gap-0.5 sm:flex-row sm:gap-4">
                <dt className="shrink-0 text-humo sm:w-44">Mejor hora para evitar cola</dt>
                <dd className="font-[family-name:var(--font-dato)]">{actividad.franjaTranquila}</dd>
              </div>
              {actividad.cierreMediodia > 0 && (
                <div className="flex flex-col gap-0.5 sm:flex-row sm:gap-4">
                  <dt className="shrink-0 text-humo sm:w-44">Cierran al mediodía</dt>
                  <dd>
                    {actividad.cierreMediodia} de {actividad.muestra} con datos de actividad
                  </dd>
                </div>
              )}
            </>
          )}

          {relevantes.map((atributo) => (
            <div
              key={`${atributo.grupo}-${atributo.valor}`}
              className="flex flex-col gap-0.5 sm:flex-row sm:gap-4"
            >
              <dt className="shrink-0 text-humo sm:w-44">{atributo.valor}</dt>
              <dd>
                {atributo.todos
                  ? `los ${atributo.total}`
                  : `${atributo.cantidad} de ${atributo.total}`}
              </dd>
            </div>
          ))}
        </dl>
      )}

      {codigosPostales.length > 1 && (
        <p className="mt-5 border-t border-linea pt-4 text-micro text-humo">
          Códigos postales cubiertos:{' '}
          <span className="font-[family-name:var(--font-dato)]">
            {codigosPostales.join(' · ')}
          </span>
        </p>
      )}

      {actividad && (
        <p className="mt-3 text-micro text-humo">
          Los datos de actividad son estimaciones a partir de la afluencia registrada en{' '}
          {actividad.muestra} de los {total} establecimientos, no horarios facilitados por
          los locales.
        </p>
      )}
    </section>
  );
}
