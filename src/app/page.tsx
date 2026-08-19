import type { Metadata } from 'next';
import Link from 'next/link';

import Buscador, { type EntradaIndice } from '@/components/Buscador';
import Ilustracion from '@/components/Ilustracion';
import { JsonLd } from '@/components/Ui';
import { obtenerGeo, rutaCiudad, rutaProvincia } from '@/lib/data';
import { SITIO, urlAbsoluta } from '@/lib/seo';

export const metadata: Metadata = {
  title: 'Locutorios y envío de dinero cerca de ti en España',
  description: SITIO.descripcion,
  alternates: { canonical: urlAbsoluta('/') },
};

/** Localidades con más establecimientos: los enlaces que más tráfico van a mover. */
const CIUDADES_DESTACADAS = 24;

export default function Portada() {
  const geo = obtenerGeo();

  const indice: EntradaIndice[] = geo.provincias.flatMap((provincia) =>
    provincia.ciudades.map((ciudad) => ({
      nombre: ciudad.nombre,
      provincia: provincia.nombre,
      ruta: rutaCiudad(provincia.slug, ciudad.slug),
      total: ciudad.total,
    })),
  );

  const destacadas = [...indice].sort((a, b) => b.total - a.total).slice(0, CIUDADES_DESTACADAS);

  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: SITIO.nombre,
    url: SITIO.dominio,
    inLanguage: 'es-ES',
    description: SITIO.descripcion,
  };

  return (
    <>
      <JsonLd datos={jsonLd} />

      {/* -------------------------------------------------- Portada */}
      <section className="border-b border-linea bg-papel-alto">
        <div className="mx-auto max-w-5xl px-4 py-14 sm:py-20">
          <p className="mb-4 font-[family-name:var(--font-dato)] text-micro tracking-[0.18em] text-verde uppercase">
            {geo.totalFichas.toLocaleString('es-ES')} establecimientos ·{' '}
            {geo.totalCiudades.toLocaleString('es-ES')} localidades
          </p>

          <h1 className="mb-5 max-w-3xl text-4xl leading-[1.05] sm:text-5xl">
            Encuentra el locutorio o el punto de envío de dinero que tienes al lado
          </h1>

          <p className="mb-8 max-w-2xl text-lg text-humo">
            Dirección, teléfono y cómo llegar a locutorios, cibercafés y oficinas de
            envío de dinero en toda España. Sin registros y sin intermediarios.
          </p>

          <div className="max-w-xl">
            <Buscador indice={indice} />
          </div>
        </div>
      </section>

      {/* -------------------------------------------------- Localidades destacadas */}
      <section className="mx-auto max-w-5xl px-4 py-14">
        <h2 className="mb-1.5 text-2xl">Las localidades con más establecimientos</h2>
        <p className="mb-6 text-humo">
          Estas son algunas de las localidades con más establecimientos registrados
          en el directorio.
        </p>

        <ul className="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-4">
          {destacadas.map((ciudad) => (
            <li key={ciudad.ruta}>
              <Link
                href={ciudad.ruta}
                className="flex items-baseline justify-between gap-2 rounded-lg border border-linea bg-papel-alto px-3 py-2.5 transition-colors hover:border-verde hover:bg-verde-claro"
              >
                <span className="truncate font-medium">{ciudad.nombre}</span>
                <span className="shrink-0 font-[family-name:var(--font-dato)] text-micro text-humo">
                  {ciudad.total}
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </section>

      {/* -------------------------------------------------- Provincias */}
      <section className="border-y border-linea bg-papel-alto">
        <div className="mx-auto max-w-5xl px-4 py-14">
          <h2 className="mb-1.5 text-2xl">Buscar por provincia</h2>
          <p className="mb-6 text-humo">
            Las {geo.totalProvincias} provincias españolas, con el número de
            establecimientos que tenemos registrados en cada una.
          </p>

          <ul className="grid grid-cols-2 gap-x-6 gap-y-0.5 sm:grid-cols-3 lg:grid-cols-4">
            {geo.provincias.map((provincia) => (
              <li key={provincia.slug} className="border-b border-linea last:border-0">
                <Link
                  href={rutaProvincia(provincia.slug)}
                  className="flex items-baseline justify-between gap-2 py-2 text-sm hover:text-verde"
                >
                  <span className="truncate">{provincia.nombre}</span>
                  <span className="shrink-0 font-[family-name:var(--font-dato)] text-micro text-humo">
                    {provincia.total}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* -------------------------------------------------- Contexto */}
      <section className="mx-auto max-w-5xl px-4 py-14">
        <div className="grid gap-10 lg:grid-cols-[1fr_22rem] lg:items-start">
          <div className="max-w-2xl">
            <h2 className="mb-4 text-2xl">Qué encuentras hoy en un locutorio</h2>

            <div className="editorial text-[0.975rem]">
            <p>
              El locutorio como cabina de llamadas prácticamente ha desaparecido: las
              aplicaciones de mensajería se llevaron por delante ese negocio. Lo que
              sobrevive bajo el mismo rótulo es otra cosa, y suele ser más útil.
            </p>
            <p>
              La mayoría de estos locales funcionan hoy como puntos de envío de dinero
              al extranjero, con corresponsalías de una o varias remesadoras. A eso
              suman recargas de móvil, venta de tarjetas SIM para llamadas
              internacionales, fotocopias e impresión, y con frecuencia paquetería o
              cambio de divisa.
            </p>
            <p>
              Las comisiones de envío varían bastante entre operadores y según el país
              de destino, así que merece la pena preguntar antes de cerrar la
              operación. Y como muchos son negocios pequeños de barrio, conviene llamar
              para confirmar el horario: es el dato que más cambia.
            </p>
            </div>
          </div>

          <Ilustracion tipo="envio" semilla="portada" />
        </div>
      </section>
    </>
  );
}
