import type { Actividad as DatosActividad } from '@/lib/data';

/*
  Actividad observada.

  No son horarios de apertura y la página nunca los llama así. Es la afluencia
  por hora que Google calcula a partir de señales de ubicación, y de ella se
  deduce una franja plausible: un local con movimiento de 10 a 14 y de 17 a 21
  está describiendo su jornada partida sin decirlo.

  La diferencia importa y por eso el aviso va al pie del bloque: una hora sin
  afluencia puede significar que el local está cerrado o simplemente que no
  había nadie dentro.
*/

function formatearTramo(inicio: number, fin: number): string {
  const hora = (valor: number) => `${valor === 24 ? 24 : valor}:00`;
  return `${hora(inicio)}–${hora(fin)}`;
}

/** Barras de 24 horas. Se recorta a 6–24, donde ocurre casi toda la actividad. */
function Barras({ curva }: { curva: number[] }) {
  const desde = 6;
  const visibles = curva.slice(desde);

  return (
    <div className="flex h-9 items-end gap-px" aria-hidden="true">
      {visibles.map((valor, indice) => (
        <div
          key={indice}
          className="flex-1 rounded-t-[1px]"
          style={{
            height: `${Math.max(valor, 3)}%`,
            backgroundColor: valor === 0 ? 'var(--color-linea)' : 'var(--color-verde)',
            opacity: valor === 0 ? 1 : 0.35 + (valor / 100) * 0.65,
          }}
        />
      ))}
    </div>
  );
}

export default function Actividad({ datos }: { datos: DatosActividad }) {
  return (
    <section className="mt-10">
      <h2 className="mb-1.5 text-xl">Cuándo suele haber movimiento</h2>
      <p className="mb-5 max-w-2xl text-sm text-humo">
        Franjas en las que se ha registrado actividad en el local. Sirven para
        hacerse una idea de cuándo está abierto y de cuándo hay menos cola, pero no
        sustituyen al horario oficial.
      </p>

      <div className="overflow-hidden rounded-xl border border-linea bg-papel-alto">
        <ul>
          {datos.dias.map((dia) => {
            const cerrado = dia.tramos.length === 0;
            return (
              <li
                key={dia.dia}
                className="flex items-center gap-3 border-b border-linea px-4 py-2.5 last:border-0"
              >
                <span className="w-20 shrink-0 text-sm font-medium capitalize">{dia.dia}</span>

                <div className="w-24 shrink-0 sm:w-32">
                  {cerrado ? null : <Barras curva={dia.curva} />}
                </div>

                <span
                  className={`flex-1 text-right font-[family-name:var(--font-dato)] text-micro ${
                    cerrado ? 'text-humo' : 'text-tinta'
                  }`}
                >
                  {cerrado
                    ? 'sin actividad'
                    : dia.tramos.map(([inicio, fin]) => formatearTramo(inicio, fin)).join(' · ')}
                </span>
              </li>
            );
          })}
        </ul>

        <p className="border-t border-linea bg-papel px-4 py-2.5 text-micro text-humo">
          Dato estimado a partir de la afluencia registrada, no facilitado por el
          establecimiento. Una franja sin actividad puede significar que estaba cerrado
          o simplemente que no hubo visitas.
        </p>
      </div>
    </section>
  );
}
