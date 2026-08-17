import type { Metadata } from 'next';
import Link from 'next/link';

import { Migas } from '@/components/Ui';
import { obtenerGeo, rutaProvincia } from '@/lib/data';
import { urlAbsoluta } from '@/lib/seo';

export const metadata: Metadata = {
  title: 'Locutorios por provincia en España',
  description:
    'Las 52 provincias españolas con locutorios y puntos de envío de dinero registrados. Entra en la tuya para ver las localidades.',
  alternates: { canonical: urlAbsoluta('/provincias') },
};

/*
  Este índice existe porque las páginas de provincia van con `noindex`.
  Sin él, el rastreo perdería el único camino corto entre la portada y las
  803 páginas de localidad. Aquí sí interesa que Google entre y siga.
*/
export default function PaginaProvincias() {
  const geo = obtenerGeo();

  return (
    <div className="mx-auto max-w-5xl px-4 py-8">
      <Migas
        migas={[
          { nombre: 'Inicio', ruta: '/' },
          { nombre: 'Provincias', ruta: '/provincias' },
        ]}
      />

      <h1 className="mb-2 text-3xl sm:text-4xl">Locutorios por provincia</h1>
      <p className="mb-10 max-w-2xl text-humo">
        {geo.totalFichas.toLocaleString('es-ES')} establecimientos registrados en{' '}
        {geo.totalProvincias} provincias y {geo.totalCiudades.toLocaleString('es-ES')}{' '}
        localidades de toda España.
      </p>

      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {geo.provincias.map((provincia) => (
          <li key={provincia.slug}>
            <Link
              href={rutaProvincia(provincia.slug)}
              className="flex h-full flex-col justify-between gap-2 rounded-xl border border-linea bg-papel-alto p-4 transition-colors hover:border-verde hover:bg-verde-claro"
            >
              <span className="font-[family-name:var(--font-display)] text-lg font-bold">
                {provincia.nombre}
              </span>
              <span className="font-[family-name:var(--font-dato)] text-micro text-humo">
                {provincia.total} establecimientos ·{' '}
                {provincia.ciudades.length}{' '}
                {provincia.ciudades.length === 1 ? 'localidad' : 'localidades'}
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
