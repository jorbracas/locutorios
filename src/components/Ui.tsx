import Link from 'next/link';

import Chapa from '@/components/Chapa';
import type { Ficha } from '@/lib/data';
import { rutaFicha } from '@/lib/data';
import { ETIQUETA_TIPO } from '@/lib/seo';

// --------------------------------------------------------------------------
// Migas de pan
// --------------------------------------------------------------------------

export type Miga = { nombre: string; ruta: string };

export function Migas({ migas }: { migas: Miga[] }) {
  return (
    <nav aria-label="Ruta de navegación" className="mb-6 text-sm">
      <ol className="flex flex-wrap items-center gap-x-1.5 gap-y-1 text-humo">
        {migas.map((miga, indice) => {
          const esUltima = indice === migas.length - 1;
          return (
            <li key={miga.ruta} className="flex items-center gap-1.5">
              {indice > 0 && (
                <span aria-hidden="true" className="text-linea">
                  /
                </span>
              )}
              {esUltima ? (
                <span aria-current="page" className="text-tinta">
                  {miga.nombre}
                </span>
              ) : (
                <Link href={miga.ruta} className="underline-offset-2 hover:text-verde hover:underline">
                  {miga.nombre}
                </Link>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

// --------------------------------------------------------------------------
// Distintivo de tipo
// --------------------------------------------------------------------------

const ESTILO_TIPO: Record<Ficha['tipo'], string> = {
  locutorio: 'bg-verde-claro text-verde',
  envio: 'bg-mostaza-claro text-[#8A6408]',
  otros: 'bg-papel text-humo',
};

export function Distintivo({ tipo }: { tipo: Ficha['tipo'] }) {
  return (
    <span
      className={`inline-flex shrink-0 items-center rounded-full px-2.5 py-0.5 text-micro font-semibold tracking-wide uppercase ${ESTILO_TIPO[tipo]}`}
    >
      {ETIQUETA_TIPO[tipo]}
    </span>
  );
}

export function AvisoCierre() {
  return (
    <p className="mb-5 rounded-lg border-l-4 border-ladrillo bg-ladrillo-claro px-4 py-3 text-sm">
      <strong className="font-semibold">Cerrado temporalmente.</strong> La última comprobación
      indicaba que este establecimiento no estaba en funcionamiento. Conviene llamar antes de ir.
    </p>
  );
}

// --------------------------------------------------------------------------
// Tarjeta de ficha para listados
// --------------------------------------------------------------------------

export function TarjetaFicha({ ficha, mostrarCiudad = false }: { ficha: Ficha; mostrarCiudad?: boolean }) {
  return (
    <li>
      <Link
        href={rutaFicha(ficha)}
        className="group flex gap-4 rounded-xl border border-linea bg-papel-alto p-3 transition-[border-color,transform] hover:border-verde motion-safe:hover:-translate-y-0.5"
      >
        <div className="h-20 w-20 shrink-0 overflow-hidden rounded-lg">
          <Chapa nombre={ficha.nombre} semilla={ficha.id} tipo={ficha.tipo} />
        </div>

        <div className="min-w-0 flex-1">
          <div className="mb-1 flex flex-wrap items-center gap-2">
            <h3 className="truncate text-base font-bold group-hover:text-verde">{ficha.nombre}</h3>
            <Distintivo tipo={ficha.tipo} />
          </div>

          <p className="truncate font-[family-name:var(--font-dato)] text-micro text-humo">
            {ficha.calle || ficha.direccion}
            {mostrarCiudad && ficha.ciudad ? ` · ${ficha.ciudad}` : ''}
          </p>

          {ficha.resumen ? (
            <p className="mt-1.5 line-clamp-2 text-sm text-humo">{ficha.resumen}</p>
          ) : null}
        </div>
      </Link>
    </li>
  );
}

// --------------------------------------------------------------------------
// JSON-LD
// --------------------------------------------------------------------------

export function JsonLd({ datos }: { datos: Record<string, unknown> }) {
  return (
    <script
      type="application/ld+json"
      // El objeto lo construimos nosotros a partir de datos ya saneados.
      dangerouslySetInnerHTML={{ __html: JSON.stringify(datos).replace(/</g, '\\u003c') }}
    />
  );
}
