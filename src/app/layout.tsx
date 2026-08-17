import type { Metadata } from 'next';
import Link from 'next/link';

import { SITIO } from '@/lib/seo';

import './globals.css';

export const metadata: Metadata = {
  metadataBase: new URL(SITIO.dominio),
  title: {
    default: `${SITIO.nombre} · Locutorios y envío de dinero en España`,
    template: `%s · ${SITIO.nombre}`,
  },
  description: SITIO.descripcion,
  applicationName: SITIO.nombre,
  openGraph: {
    type: 'website',
    locale: 'es_ES',
    siteName: SITIO.nombre,
  },
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true, 'max-image-preview': 'large', 'max-snippet': -1 },
  },
  // Se rellena cuando estén disponibles los códigos de Search Console.
  verification: {},
};

export const viewport = {
  themeColor: '#0B5C4B',
  width: 'device-width',
  initialScale: 1,
};

function Cabecera() {
  return (
    <header className="border-b border-linea bg-papel-alto">
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-4 py-3.5">
        <Link href="/" className="group flex items-center gap-2.5" aria-label="Ir a la portada">
          <span
            aria-hidden="true"
            className="chapa-toldo h-7 w-7 shrink-0 rounded-md bg-verde text-mostaza"
          />
          <span className="font-[family-name:var(--font-display)] text-[1.05rem] leading-none font-extrabold tracking-tight">
            locutorios<span className="text-verde">cercademi</span>
          </span>
        </Link>

        <nav aria-label="Navegación principal">
          <Link
            href="/provincias"
            className="text-sm font-medium underline-offset-4 hover:text-verde hover:underline"
          >
            Todas las provincias
          </Link>
        </nav>
      </div>
    </header>
  );
}

function Pie() {
  return (
    <footer className="mt-20 border-t border-linea bg-papel-alto">
      <div className="mx-auto max-w-5xl px-4 py-10">
        <p className="mb-5 max-w-prose text-sm text-humo">
          {SITIO.nombre} recopila información pública sobre locutorios y puntos de envío de dinero
          en España. No gestionamos ninguno de estos establecimientos ni tramitamos envíos.
          Confirma siempre horarios y tarifas con el local antes de desplazarte.
        </p>

        <nav aria-label="Enlaces legales" className="mb-6 flex flex-wrap gap-x-5 gap-y-2 text-sm">
          <Link href="/provincias" className="underline-offset-4 hover:text-verde hover:underline">
            Provincias
          </Link>
          <Link href="/aviso-legal" className="underline-offset-4 hover:text-verde hover:underline">
            Aviso legal
          </Link>
          <Link href="/privacidad" className="underline-offset-4 hover:text-verde hover:underline">
            Privacidad
          </Link>
          <Link href="/contacto" className="underline-offset-4 hover:text-verde hover:underline">
            Corregir una ficha
          </Link>
        </nav>

        <p className="text-micro text-humo">
          © {new Date().getFullYear()} {SITIO.nombre}
        </p>
      </div>
    </footer>
  );
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head>
        {/*
          Las fuentes se cargan por enlace y no con `next/font` porque el
          entorno de construcción de este repositorio no tiene salida a
          fonts.googleapis.com. En Vercel sí la hay: migrar a `next/font/google`
          es una mejora directa de rendimiento (autoalojado, sin FOUT).
        */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=Public+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"
        />
      </head>
      <body className="flex min-h-screen flex-col">
        <a
          href="#contenido"
          className="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:z-50 focus:rounded-md focus:bg-verde focus:px-4 focus:py-2 focus:text-papel-alto"
        >
          Saltar al contenido
        </a>

        <Cabecera />
        <main id="contenido" className="flex-1">
          {children}
        </main>
        <Pie />
      </body>
    </html>
  );
}
