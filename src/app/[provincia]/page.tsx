import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';

import Mapa from '@/components/Mapa';
import { Migas } from '@/components/Ui';
import { obtenerProvincia, obtenerProvincias, rutaCiudad } from '@/lib/data';
import { urlAbsoluta } from '@/lib/seo';

type Props = { params: Promise<{ provincia: string }> };

export function generateStaticParams() {
  return obtenerProvincias().map((provincia) => ({ provincia: provincia.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { provincia: slug } = await params;
  const provincia = obtenerProvincia(slug);
  if (!provincia) return {};

  return {
    title: `Locutorios en ${provincia.nombre}`,
    description: `Localidades de ${provincia.nombre} con locutorios y puntos de envío de dinero.`,
    alternates: { canonical: urlAbsoluta(`/${provincia.slug}`) },
    /*
      La página de provincia es un nodo de navegación, no un destino de
      búsqueda: su contenido es un listado de enlaces que compite con las
      páginas de localidad, que sí responden a una intención real.

      `follow` es imprescindible: sin él se cortaría el rastreo hacia las
      localidades y las fichas que cuelgan de aquí.
    */
    robots: { index: false, follow: true },
  };
}

export default async function PaginaProvincia({ params }: Props) {
  const { provincia: slug } = await params;
  const provincia = obtenerProvincia(slug);
  if (!provincia) notFound();

  // Con muchas localidades, agrupar por inicial hace la lista navegable.
  const agrupadas = new Map<string, typeof provincia.ciudades>();
  for (const ciudad of [...provincia.ciudades].sort((a, b) =>
    a.nombre.localeCompare(b.nombre, 'es'),
  )) {
    const inicial = ciudad.nombre.charAt(0).toUpperCase();
    const grupo = agrupadas.get(inicial) ?? [];
    grupo.push(ciudad);
    agrupadas.set(inicial, grupo);
  }

  return (
    <div className="mx-auto max-w-5xl px-4 py-8">
      <Migas
        migas={[
          { nombre: 'Inicio', ruta: '/' },
          { nombre: provincia.nombre, ruta: `/${provincia.slug}` },
        ]}
      />

      <h1 className="mb-2 text-3xl sm:text-4xl">Locutorios en {provincia.nombre}</h1>
      <p className="mb-8 max-w-2xl text-humo">
        {provincia.total.toLocaleString('es-ES')} establecimientos repartidos en{' '}
        {provincia.ciudades.length.toLocaleString('es-ES')}{' '}
        {provincia.ciudades.length === 1 ? 'localidad' : 'localidades'}. Elige la tuya
        para ver las direcciones y los teléfonos.
      </p>

      <div className="mb-10">
        <Mapa
          lat={provincia.lat}
          lng={provincia.lng}
          nombre={provincia.nombre}
          margen={0.5}
        />
      </div>

      <h2 className="mb-4 text-xl">Localidades</h2>

      <div className="space-y-6">
        {[...agrupadas.entries()].map(([inicial, ciudades]) => (
          <section key={inicial}>
            <h3 className="mb-2 font-[family-name:var(--font-dato)] text-micro tracking-[0.18em] text-verde uppercase">
              {inicial}
            </h3>
            <ul className="grid grid-cols-2 gap-x-6 gap-y-0.5 sm:grid-cols-3 lg:grid-cols-4">
              {ciudades.map((ciudad) => (
                <li key={ciudad.slug} className="border-b border-linea">
                  <Link
                    href={rutaCiudad(provincia.slug, ciudad.slug)}
                    className="flex items-baseline justify-between gap-2 py-2 text-sm hover:text-verde"
                  >
                    <span className="truncate">{ciudad.nombre}</span>
                    <span className="shrink-0 font-[family-name:var(--font-dato)] text-micro text-humo">
                      {ciudad.total}
                    </span>
                  </Link>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}
