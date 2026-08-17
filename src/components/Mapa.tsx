'use client';

import { useState } from 'react';

/*
  Mapa bajo demanda.

  El iframe de OpenStreetMap solo se inserta cuando la persona lo pide. Cargarlo
  de entrada añadiría ~300 KB y un tercero bloqueante a cada una de las 3.050
  fichas, justo en el elemento que compite por el LCP. El marcador estático
  cubre el caso mayoritario: la mayoría de la gente quiere la dirección y el
  botón de "cómo llegar", no explorar el mapa.
*/

type Props = {
  lat: number;
  lng: number;
  nombre: string;
  /** Grados de margen alrededor del punto. Más pequeño = más zoom. */
  margen?: number;
};

export default function Mapa({ lat, lng, nombre, margen = 0.004 }: Props) {
  const [visible, setVisible] = useState(false);

  const bbox = [lng - margen, lat - margen / 2, lng + margen, lat + margen / 2].join('%2C');
  const src =
    `https://www.openstreetmap.org/export/embed.html?bbox=${bbox}` +
    `&layer=mapnik&marker=${lat}%2C${lng}`;

  if (!visible) {
    return (
      <button
        type="button"
        onClick={() => setVisible(true)}
        className="group flex w-full items-center justify-center gap-2 rounded-lg border border-dashed border-linea bg-papel-alto px-4 py-10 text-sm font-medium text-humo transition-colors hover:border-verde hover:text-verde"
      >
        <svg
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <path d="M12 21s-7-6.4-7-11a7 7 0 1 1 14 0c0 4.6-7 11-7 11z" />
          <circle cx="12" cy="10" r="2.6" />
        </svg>
        Ver mapa de la ubicación
      </button>
    );
  }

  return (
    <div className="overflow-hidden rounded-lg border border-linea bg-papel-alto">
      <iframe
        src={src}
        title={`Mapa de la ubicación de ${nombre}`}
        loading="lazy"
        className="block h-[320px] w-full border-0"
        referrerPolicy="no-referrer-when-downgrade"
      />
      <p className="border-t border-linea px-3 py-2 text-micro text-humo">
        Cartografía de{' '}
        <a
          href="https://www.openstreetmap.org/copyright"
          className="underline underline-offset-2 hover:text-verde"
          rel="noopener nofollow"
          target="_blank"
        >
          OpenStreetMap
        </a>
        , bajo licencia ODbL.
      </p>
    </div>
  );
}
