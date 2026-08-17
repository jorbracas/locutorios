import type { Metadata } from 'next';
import { notFound } from 'next/navigation';

import Ilustracion from '@/components/Ilustracion';
import Mapa from '@/components/Mapa';
import { Distintivo, JsonLd, Migas, TarjetaFicha } from '@/components/Ui';
import {
  fichasDeCiudad,
  obtenerCiudad,
  obtenerProvincia,
  obtenerProvincias,
  rutaCiudad,
  rutaProvincia,
} from '@/lib/data';
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

  const cuantos = ciudad.total;
  const sufijo = ciudad.nombre === provincia.nombre ? '' : ` (${provincia.nombre})`;

  return {
    title: `Locutorios en ${ciudad.nombre}${sufijo}`,
    description:
      cuantos === 1
        ? `Un locutorio en ${ciudad.nombre}: dirección, teléfono y cómo llegar.`
        : `Los ${cuantos} locutorios y puntos de envío de dinero de ${ciudad.nombre}: dirección, teléfono y cómo llegar.`,
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

  const migas = [
    { nombre: 'Inicio', ruta: '/' },
    { nombre: provincia.nombre, ruta: rutaProvincia(provincia.slug) },
    { nombre: ciudad.nombre, ruta: rutaCiudad(provincia.slug, ciudad.slug) },
  ];

  // Agrupa por tipo: quien busca enviar dinero no busca lo mismo que quien
  // busca un locutorio, aunque a menudo acaben en el mismo local.
  const locutorios = fichas.filter((ficha) => ficha.tipo === 'locutorio');
  const envios = fichas.filter((ficha) => ficha.tipo === 'envio');
  const otros = fichas.filter((ficha) => ficha.tipo === 'otros');

  const secciones = [
    { clave: 'locutorio' as const, titulo: 'Locutorios', fichas: locutorios },
    { clave: 'envio' as const, titulo: 'Puntos de envío de dinero', fichas: envios },
    { clave: 'otros' as const, titulo: 'Otros establecimientos con servicios similares', fichas: otros },
  ].filter((seccion) => seccion.fichas.length > 0);

  return (
    <div className="mx-auto max-w-5xl px-4 py-8">
      <JsonLd datos={jsonLdMigas(migas)} />
      <JsonLd datos={jsonLdListado(fichas, `Locutorios en ${ciudad.nombre}`)} />

      <Migas migas={migas} />

      <h1 className="mb-2 text-3xl sm:text-4xl">
        Locutorios en {ciudad.nombre}
      </h1>

      <p className="mb-8 max-w-2xl text-humo">
        {fichas.length === 1
          ? `Tenemos registrado un establecimiento en ${ciudad.nombre}`
          : `Tenemos registrados ${fichas.length} establecimientos en ${ciudad.nombre}`}
        {locutorios.length > 0 && envios.length > 0
          ? `, entre locutorios y puntos de envío de dinero`
          : ''}
        . Cada ficha incluye la dirección exacta, el teléfono cuando está disponible y
        un enlace para llegar.
      </p>

      <div className="mb-10">
        <Mapa lat={ciudad.lat} lng={ciudad.lng} nombre={ciudad.nombre} margen={0.03} />
      </div>

      <div className="space-y-10">
        {secciones.map((seccion) => (
          <section key={seccion.clave}>
            <div className="mb-4 flex items-center gap-3">
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

      <Ilustracion
        tipo={envios.length > locutorios.length ? 'envio' : 'locutorio'}
        semilla={`${slugProvincia}-${slugCiudad}`}
        className="mt-12 max-w-2xl"
      />

      {otros.length > 0 && (
        <p className="mt-8 rounded-lg border border-linea bg-papel-alto px-4 py-3 text-sm text-humo">
          Los establecimientos de la última sección aparecen catalogados con otra
          actividad principal, pero ofrecen servicios relacionados. Merece la pena
          llamar antes de acercarse.
        </p>
      )}
    </div>
  );
}
