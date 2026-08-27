import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';

import Ilustracion from '@/components/Ilustracion';
import MapaMultiple, { type PuntoMapa } from '@/components/MapaMultiple';
import PreguntasCiudad, { construirPreguntas } from '@/components/PreguntasCiudad';
import ResumenCiudad from '@/components/ResumenCiudad';
import { Distintivo, JsonLd, Migas, TarjetaFicha } from '@/components/Ui';
import {
  fichasDeCiudad,
  obtenerAgregado,
  obtenerCiudad,
  obtenerProvincia,
  obtenerProvincias,
  obtenerTextoCiudad,
  rutaCiudad,
  rutaFicha,
  rutaProvincia,
} from '@/lib/data';
import { renderizarEditorial } from '@/lib/markdown';
import { jsonLdListado, jsonLdMigas, urlAbsoluta } from '@/lib/seo';

type Props = { params: Promise<{ provincia: string; ciudad: string }> };

export function generateStaticParams() {
  return obtenerProvincias().flatMap((provincia) =>
    provincia.ciudades.map((ciudad) => ({
      provincia: provincia.slug,
      ciudad: ciudad.slug,
    })),
  );
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { provincia: slugProvincia, ciudad: slugCiudad } = await params;
  const ciudad = obtenerCiudad(slugProvincia, slugCiudad);
  const provincia = obtenerProvincia(slugProvincia);
  if (!ciudad || !provincia) return {};

  const agregado = obtenerAgregado(slugProvincia, slugCiudad);
  const sufijo = ciudad.nombre === provincia.nombre ? '' : ` (${provincia.nombre})`;

  /*
    La descripcion se compone con datos reales de la localidad, no con una
    plantilla fija. Dos localidades del mismo tamano dan descripciones
    distintas porque cambian el recuento y la disponibilidad de contacto.
  */
  const piezas: string[] = [];
  if (agregado) {
    piezas.push(
      agregado.total === 1
        ? 'Un establecimiento'
        : `${agregado.total} locutorios y puntos de envío de dinero`,
    );
    if (agregado.conTelefono > 0) {
      piezas.push(`${agregado.conTelefono} con teléfono publicado`);
    }
  }
  piezas.push('dirección, teléfono y cómo llegar');

  return {
    title: `Locutorios en ${ciudad.nombre}${sufijo}`,
    description: `${piezas.join('. ')}.`,
    alternates: { canonical: urlAbsoluta(rutaCiudad(slugProvincia, slugCiudad)) },
  };
}

export default async function PaginaCiudad({ params }: Props) {
  const { provincia: slugProvincia, ciudad: slugCiudad } = await params;
  const provincia = obtenerProvincia(slugProvincia);
  const ciudad = obtenerCiudad(slugProvincia, slugCiudad);
  if (!provincia || !ciudad) notFound();

  const fichas = fichasDeCiudad(slugProvincia, slugCiudad);
  if (!fichas.length) notFound();

  const agregado = obtenerAgregado(slugProvincia, slugCiudad);
  const texto = obtenerTextoCiudad(slugProvincia, slugCiudad);
  const preguntas = agregado ? construirPreguntas(ciudad.nombre, agregado) : [];

  const migas = [
    { nombre: 'Inicio', ruta: '/' },
    { nombre: provincia.nombre, ruta: rutaProvincia(provincia.slug) },
    { nombre: ciudad.nombre, ruta: rutaCiudad(provincia.slug, ciudad.slug) },
  ];

  // Se agrupa por tipo: quien busca enviar dinero no busca lo mismo que quien
  // busca un locutorio, aunque a menudo acaben en el mismo local.
  const locutorios = fichas.filter((ficha) => ficha.tipo === 'locutorio');
  const envios = fichas.filter((ficha) => ficha.tipo === 'envio');
  const otros = fichas.filter((ficha) => ficha.tipo === 'otros');

  const secciones = [
    { clave: 'locutorio' as const, titulo: `Locutorios en ${ciudad.nombre}`, fichas: locutorios },
    { clave: 'envio' as const, titulo: `Envío de dinero en ${ciudad.nombre}`, fichas: envios },
    {
      clave: 'otros' as const,
      titulo: 'Otros establecimientos con servicios similares',
      fichas: otros,
    },
  ].filter((seccion) => seccion.fichas.length > 0);

  const jsonLdPreguntas = preguntas.length
    ? {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: preguntas.map((item) => ({
          '@type': 'Question',
          name: item.pregunta,
          acceptedAnswer: { '@type': 'Answer', text: item.respuesta },
        })),
      }
    : null;

  return (
    <div className="mx-auto max-w-5xl px-4 py-8">
      <JsonLd datos={jsonLdMigas(migas)} />
      <JsonLd datos={jsonLdListado(fichas, `Locutorios en ${ciudad.nombre}`)} />
      {jsonLdPreguntas && <JsonLd datos={jsonLdPreguntas} />}

      <Migas migas={migas} />

      <h1 className="mb-3 text-3xl sm:text-4xl">Locutorios en {ciudad.nombre}</h1>

      <p className="mb-8 max-w-2xl text-lg text-humo">
        {fichas.length === 1
          ? `Un establecimiento con servicios de locutorio o envío de dinero en ${ciudad.nombre}`
          : `${fichas.length} establecimientos en ${ciudad.nombre}`}
        {locutorios.length > 0 && envios.length > 0
          ? ', entre locutorios y puntos de envío de dinero'
          : ''}
        . Dirección, teléfono y cómo llegar a cada uno.
      </p>

      {agregado && <ResumenCiudad ciudad={ciudad.nombre} datos={agregado} />}

      {texto && (
        <div className="editorial mb-10 max-w-2xl">{renderizarEditorial(texto)}</div>
      )}

      <div className="mb-10">
        <MapaMultiple
          puntos={fichas.map(
            (ficha): PuntoMapa => ({
              lat: ficha.lat,
              lng: ficha.lng,
              nombre: ficha.nombre,
              href: rutaFicha(ficha),
              tipo: ficha.tipo,
            }),
          )}
          nombreZona={ciudad.nombre}
          centro={{ lat: ciudad.lat, lng: ciudad.lng }}
        />
      </div>

      <div className="space-y-10">
        {secciones.map((seccion) => (
          <section key={seccion.clave}>
            <div className="mb-4 flex flex-wrap items-center gap-3">
              <h2 className="text-xl">{seccion.titulo}</h2>
              <Distintivo tipo={seccion.clave} />
              <span className="font-[family-name:var(--font-dato)] text-micro text-humo">
                {seccion.fichas.length}
              </span>
            </div>

            <ul className="grid gap-3 sm:grid-cols-2">
              {seccion.fichas.map((ficha) => (
                <TarjetaFicha key={ficha.id} ficha={ficha} />
              ))}
            </ul>
          </section>
        ))}
      </div>

      {otros.length > 0 && (
        <p className="mt-8 rounded-lg border border-linea bg-papel-alto px-4 py-3 text-sm text-humo">
          Los establecimientos de la última sección aparecen catalogados con otra actividad
          principal, pero ofrecen servicios relacionados. Merece la pena llamar antes de
          acercarse.
        </p>
      )}

      <PreguntasCiudad preguntas={preguntas} />

      <Ilustracion
        tipo={envios.length > locutorios.length ? 'envio' : 'locutorio'}
        semilla={`${slugProvincia}-${slugCiudad}`}
        className="mt-12 max-w-2xl"
      />

      {/*
        Enlazado lateral entre localidades cercanas. Ademas de ser util cuando
        la localidad tiene un solo establecimiento, reparte autoridad en
        horizontal en vez de obligar a subir siempre a la provincia, que va
        con noindex.
      */}
      {agregado && agregado.vecinas.length > 0 && (
        <section className="mt-12 border-t border-linea pt-8">
          <h2 className="mb-4 text-xl">Locutorios cerca de {ciudad.nombre}</h2>
          <ul className="grid grid-cols-2 gap-2 sm:grid-cols-4">
            {agregado.vecinas.map((vecina) => (
              <li key={`${vecina.slugProvincia}-${vecina.slug}`}>
                <Link
                  href={rutaCiudad(vecina.slugProvincia, vecina.slug)}
                  className="block rounded-lg border border-linea bg-papel-alto px-3 py-2.5 transition-colors hover:border-verde hover:bg-verde-claro"
                >
                  <span className="block truncate font-medium">{vecina.nombre}</span>
                  <span className="block font-[family-name:var(--font-dato)] text-micro text-humo">
                    {vecina.total} · a {vecina.distancia} km
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
