'use client';

import 'leaflet/dist/leaflet.css';
import 'leaflet.markercluster/dist/MarkerCluster.css';
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';

import { useRouter } from 'next/navigation';
import { useEffect, useRef, useState } from 'react';

/*
  Mapa multipunto.

  Sustituye al iframe de un solo marcador en las páginas de provincia y
  ciudad: aquí cada punto es un negocio (o una localidad, en la provincia) y
  pulsarlo lleva directamente a su ficha. Sigue el mismo patrón de carga bajo
  demanda que el resto del sitio — Leaflet y sus estilos solo se cargan si la
  persona pulsa "Ver mapa", nunca de entrada.

  El agrupamiento (leaflet.markercluster) es imprescindible en ciudades como
  Madrid, con 271 fichas: sin agrupar, el mapa sería un amasijo de chinchetas
  encima unas de otras. Al hacer zoom los grupos se abren solos.
*/

export type PuntoMapa = {
  lat: number;
  lng: number;
  nombre: string;
  href: string;
  /** Antepone un color distinto según el tipo de negocio. */
  tipo?: 'locutorio' | 'envio' | 'otros';
};

type Props = {
  puntos: PuntoMapa[];
  nombreZona: string;
  /** Punto de partida si no hay suficientes puntos para calcular límites. */
  centro?: { lat: number; lng: number };
};

const COLOR_TIPO: Record<string, string> = {
  locutorio: '#0B5C4B', // verde
  envio: '#D9A21B', // mostaza
  otros: '#5D6B66', // humo
};

/** Chincheta SVG en línea: evita el problema clásico de Leaflet con los
 * iconos por defecto (rutas rotas al empaquetar) y usa los colores del sitio. */
function svgChincheta(color: string): string {
  return `
    <svg width="30" height="40" viewBox="0 0 30 40" xmlns="http://www.w3.org/2000/svg">
      <path d="M15 0C6.7 0 0 6.7 0 15c0 10.5 15 25 15 25s15-14.5 15-25C30 6.7 23.3 0 15 0z"
            fill="${color}" stroke="#F7F8F5" stroke-width="1.5"/>
      <circle cx="15" cy="15" r="6" fill="#F7F8F5"/>
    </svg>`;
}

export default function MapaMultiple({ puntos, nombreZona, centro }: Props) {
  const [visible, setVisible] = useState(false);
  const contenedorRef = useRef<HTMLDivElement>(null);
  const mapaRef = useRef<import('leaflet').Map | null>(null);
  const router = useRouter();

  useEffect(() => {
    if (!visible || !contenedorRef.current || mapaRef.current) return;

    let cancelado = false;

    (async () => {
      const L = (await import('leaflet')).default;
      // leaflet.markercluster no importa Leaflet: su build UMD referencia la
      // variable `L` esperando que ya exista en el ámbito global (así está
      // escrito en su propio código fuente, sin `require('leaflet')` en
      // ningún sitio). Sin esta línea, el plugin lanza "L is not defined" en
      // cuanto se carga, y el mapa nunca llega a agrupar los marcadores.
      (window as unknown as { L: typeof L }).L = L;
      await import('leaflet.markercluster');
      if (cancelado || !contenedorRef.current) return;

      const mapa = L.map(contenedorRef.current, {
        scrollWheelZoom: false,
      });
      mapaRef.current = mapa;

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        maxZoom: 19,
      }).addTo(mapa);

      const grupo = (L as any).markerClusterGroup({
        maxClusterRadius: 45,
        spiderfyOnMaxZoom: true,
        showCoverageOnHover: false,
      });

      for (const punto of puntos) {
        const color = COLOR_TIPO[punto.tipo ?? 'otros'] ?? COLOR_TIPO.otros;
        const icono = L.divIcon({
          html: svgChincheta(color),
          className: '', // sin las clases por defecto de Leaflet
          iconSize: [30, 40],
          iconAnchor: [15, 40],
          popupAnchor: [0, -36],
        });

        const marcador = L.marker([punto.lat, punto.lng], { icon: icono, alt: punto.nombre });

        // El popup ofrece un enlace real (funciona incluso sin JS de router)
        // y el propio marcador navega al pulsarlo, que es el atajo esperado.
        const popup = document.createElement('div');
        popup.className = 'text-sm';
        const enlace = document.createElement('a');
        enlace.href = punto.href;
        enlace.textContent = punto.nombre;
        enlace.className = 'font-semibold text-verde hover:underline';
        enlace.addEventListener('click', (evento) => {
          evento.preventDefault();
          router.push(punto.href);
        });
        popup.appendChild(enlace);
        marcador.bindPopup(popup);
        marcador.bindTooltip(punto.nombre, { direction: 'top', offset: [0, -36] });
        marcador.on('click', () => router.push(punto.href));

        grupo.addLayer(marcador);
      }

      mapa.addLayer(grupo);

      if (puntos.length > 0) {
        const limites = L.latLngBounds(puntos.map((p) => [p.lat, p.lng] as [number, number]));
        mapa.fitBounds(limites, { padding: [30, 30], maxZoom: 15 });
      } else if (centro) {
        mapa.setView([centro.lat, centro.lng], 12);
      }
    })();

    return () => {
      cancelado = true;
      mapaRef.current?.remove();
      mapaRef.current = null;
    };
  }, [visible, puntos, centro, router]);

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
        Ver mapa de {nombreZona} ({puntos.length}{' '}
        {puntos.length === 1 ? 'punto' : 'puntos'})
      </button>
    );
  }

  return (
    <div className="overflow-hidden rounded-lg border border-linea bg-papel-alto">
      <div ref={contenedorRef} className="h-[420px] w-full" />
      <p className="border-t border-linea px-3 py-2 text-micro text-humo">
        Pulsa un punto para ir a su ficha. Cartografía de{' '}
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
