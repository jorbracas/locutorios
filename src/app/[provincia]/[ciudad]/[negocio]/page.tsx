import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';

import Actividad from '@/components/Actividad';
import Chapa from '@/components/Chapa';
import Ilustracion from '@/components/Ilustracion';
import Mapa from '@/components/Mapa';
import { AvisoCierre, Distintivo, JsonLd, Migas, TarjetaFicha } from '@/components/Ui';
import {
  fichasRelacionadas,
  obtenerFicha,
  obtenerProvincias,
  fichasDeProvincia,
  rutaCiudad,
  rutaFicha,
  rutaProvincia,
  type Ficha,
} from '@/lib/data';
import { renderizarEditorial } from '@/lib/markdown';
import { jsonLdMigas, jsonLdNegocio, urlAbsoluta } from '@/lib/seo';

type Props = { params: Promise<{ provincia: string; ciudad: string; negocio: string }> };

export function generateStaticParams() {
  return obtenerProvincias().flatMap((provincia) =>
    fichasDeProvincia(provincia.slug).map((ficha) => ({
      provincia: ficha.slugProvincia,
      ciudad: ficha.slugCiudad,
      negocio: ficha.slug,
    })),
  );
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { provincia, ciudad, negocio } = await params;
  const ficha = obtenerFicha(provincia, ciudad, negocio);
  if (!ficha) return {};

  return {
    /*
      `absolute` evita que la plantilla añada « · Locutorios cerca de mí ».
      El título del negocio ya consume el presupuesto de ~60 caracteres que
      Google muestra, y la marca añadiría 24 más que se cortarían siempre.
    */
    title: { absolute: ficha.metaTitulo },
    description: ficha.metaDescripcion,
    alternates: { canonical: urlAbsoluta(rutaFicha(ficha)) },
    openGraph: {
      title: ficha.metaTitulo,
      description: ficha.metaDescripcion,
      url: urlAbsoluta(rutaFicha(ficha)),
      type: 'website',
    },
  };
}

// --------------------------------------------------------------------------

function FilaDato({ etiqueta, children }: { etiqueta: string; children: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-0.5 border-b border-linea py-2.5 last:border-0 sm:flex-row sm:gap-4">
      <dt className="shrink-0 font-[family-name:var(--font-dato)] text-micro tracking-wide text-humo uppercase sm:w-32 sm:pt-1">
        {etiqueta}
      </dt>
      <dd className="min-w-0 flex-1">{children}</dd>
    </div>
  );
}

function BloqueDatos({ ficha }: { ficha: Ficha }) {
  const destinoMaps = `https://www.google.com/maps/dir/?api=1&destination=${ficha.lat},${ficha.lng}`;

  return (
    <dl className="rounded-xl border border-linea bg-papel-alto px-4 py-1">
      <FilaDato etiqueta="Dirección">
        <p>{ficha.calle || ficha.direccion}</p>
        <p className="text-sm text-humo">
          {[ficha.codigoPostal, ficha.ciudad, ficha.provincia].filter(Boolean).join(' · ')}
        </p>
      </FilaDato>

      {ficha.telefono && (
        <FilaDato etiqueta="Teléfono">
          <a
            href={`tel:${ficha.telefono.enlace}`}
            className="font-[family-name:var(--font-dato)] font-medium text-verde underline-offset-4 hover:underline"
          >
            {ficha.telefono.visible}
          </a>
        </FilaDato>
      )}

      {ficha.web && (
        <FilaDato etiqueta="Web">
          <a
            href={ficha.web}
            rel="nofollow noopener"
            target="_blank"
            className="break-all text-verde underline-offset-4 hover:underline"
          >
            {ficha.web.replace(/^https?:\/\//, '').replace(/\/$/, '')}
          </a>
        </FilaDato>
      )}

      {ficha.categorias.length > 0 && (
        <FilaDato etiqueta="Actividad">
          <p className="text-sm">{ficha.categorias.join(' · ')}</p>
        </FilaDato>
      )}

      <FilaDato etiqueta="Cómo llegar">
        <a
          href={destinoMaps}
          rel="nofollow noopener"
          target="_blank"
          className="inline-flex items-center gap-1.5 rounded-lg bg-verde px-3.5 py-2 text-sm font-semibold text-papel-alto transition-opacity hover:opacity-90"
        >
          Abrir indicaciones
          <svg
            width="15"
            height="15"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <path d="M7 17 17 7M9 7h8v8" />
          </svg>
        </a>
      </FilaDato>
    </dl>
  );
}

// --------------------------------------------------------------------------

export default async function PaginaFicha({ params }: Props) {
  const { provincia: slugProvincia, ciudad: slugCiudad, negocio } = await params;
  const ficha = obtenerFicha(slugProvincia, slugCiudad, negocio);
  if (!ficha) notFound();

  const relacionadas = fichasRelacionadas(ficha);

  const migas = [
    { nombre: 'Inicio', ruta: '/' },
    { nombre: ficha.provincia, ruta: rutaProvincia(ficha.slugProvincia) },
    { nombre: ficha.ciudad, ruta: rutaCiudad(ficha.slugProvincia, ficha.slugCiudad) },
    { nombre: ficha.nombre, ruta: rutaFicha(ficha) },
  ];

  return (
    <article className="mx-auto max-w-5xl px-4 py-8">
      <JsonLd datos={jsonLdNegocio(ficha)} />
      <JsonLd datos={jsonLdMigas(migas)} />

      <Migas migas={migas} />

      {/* ---------------------------------------------- Encabezado */}
      <header className="mb-8 flex flex-col gap-5 sm:flex-row sm:items-start">
        <div className="h-28 w-28 shrink-0 overflow-hidden rounded-xl sm:h-36 sm:w-36">
          <Chapa nombre={ficha.nombre} semilla={ficha.id} tipo={ficha.tipo} tamano="grande" />
        </div>

        <div className="min-w-0 flex-1">
          <div className="mb-2.5 flex flex-wrap items-center gap-2">
            <Distintivo tipo={ficha.tipo} />
            <Link
              href={rutaCiudad(ficha.slugProvincia, ficha.slugCiudad)}
              className="text-micro text-humo underline-offset-2 hover:text-verde hover:underline"
            >
              {ficha.ciudad}
            </Link>
          </div>

          <h1 className="mb-3 text-3xl sm:text-4xl">{ficha.nombre}</h1>

          {ficha.resumen && <p className="max-w-2xl text-lg text-humo">{ficha.resumen}</p>}
        </div>
      </header>

      {ficha.cerradoTemporalmente && <AvisoCierre />}

      {/* ---------------------------------------------- Cuerpo */}
      <div className="grid gap-10 lg:grid-cols-[1fr_20rem] lg:gap-12">
        <div className="min-w-0">
          {ficha.titulo && ficha.titulo !== ficha.nombre && (
            <h2 className="sr-only">{ficha.titulo}</h2>
          )}

          <div className="editorial">{renderizarEditorial(ficha.cuerpo)}</div>

          {ficha.actividad && <Actividad datos={ficha.actividad} />}

          {ficha.atributos.length > 0 && (
            <section className="mt-10">
              <h2 className="mb-4 text-xl">Servicios y accesibilidad</h2>
              <div className="grid gap-4 sm:grid-cols-2">
                {ficha.atributos.map((grupo) => (
                  <div
                    key={grupo.grupo}
                    className="rounded-xl border border-linea bg-papel-alto p-4"
                  >
                    <h3 className="mb-2 font-[family-name:var(--font-dato)] text-micro tracking-[0.14em] text-verde uppercase">
                      {grupo.grupo}
                    </h3>
                    <ul className="space-y-1 text-sm">
                      {grupo.valores.map((valor) => (
                        <li key={valor} className="flex gap-2">
                          <span aria-hidden="true" className="text-verde">
                            ·
                          </span>
                          <span>{valor}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </section>
          )}
          <Ilustracion tipo={ficha.tipo} semilla={ficha.id} className="mt-10" />
        </div>

        {/* ---------------------------------------------- Columna de datos */}
        <aside className="min-w-0 space-y-5 lg:sticky lg:top-6 lg:self-start">
          <BloqueDatos ficha={ficha} />

          <Mapa lat={ficha.lat} lng={ficha.lng} nombre={ficha.nombre} />

          {/*
            Canal de rectificacion visible en cada ficha. Ademas de ser util,
            es la primera defensa practica ante una reclamacion: lo primero
            que pregunta un abogado es si existia una via de correccion y si
            se atendio. Aqui existe y esta a la vista.
          */}
          <div className="rounded-xl border border-linea bg-papel-alto px-4 py-3 text-sm text-humo">
            <p>
              ¿Falta el horario o hay algún dato incorrecto?{' '}
              <Link href="/contacto" className="text-verde underline underline-offset-2">
                Cuéntanoslo
              </Link>{' '}
              y lo corregimos.
            </p>
            <p className="mt-2 border-t border-linea pt-2 text-micro">
              Si eres el titular del negocio, puedes pedir la modificación o la
              retirada de esta ficha y la atendemos sin más trámite.
            </p>
          </div>
        </aside>
      </div>

      {/* ---------------------------------------------- Enlazado interno */}
      {relacionadas.length > 0 && (
        <section className="mt-16 border-t border-linea pt-10">
          <h2 className="mb-1.5 text-xl">Otros establecimientos cerca</h2>
          <p className="mb-5 text-sm text-humo">
            Alternativas en {ficha.ciudad} y alrededores, por si esta no te encaja.
          </p>

          <ul className="grid gap-3 sm:grid-cols-2">
            {relacionadas.map((relacionada) => (
              <TarjetaFicha
                key={relacionada.id}
                ficha={relacionada}
                mostrarCiudad={relacionada.slugCiudad !== ficha.slugCiudad}
              />
            ))}
          </ul>

          <p className="mt-6 text-sm">
            <Link
              href={rutaCiudad(ficha.slugProvincia, ficha.slugCiudad)}
              className="font-medium text-verde underline underline-offset-4"
            >
              Ver todos los locutorios de {ficha.ciudad}
            </Link>
          </p>
        </section>
      )}
    </article>
  );
}
