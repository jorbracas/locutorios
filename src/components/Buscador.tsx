'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';

/*
  Buscador de localidades.

  El sitio es estático, así que no hay backend contra el que consultar. En su
  lugar recibe el índice completo de 803 localidades (unos 40 KB) y filtra en
  el navegador. Es instantáneo y funciona sin conexión una vez cargada la
  página. Sin JavaScript, la rejilla de provincias que hay debajo sigue
  siendo un camino de navegación completo.
*/

export type EntradaIndice = {
  nombre: string;
  provincia: string;
  ruta: string;
  total: number;
};

function normalizar(texto: string): string {
  return texto
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim();
}

export default function Buscador({ indice }: { indice: EntradaIndice[] }) {
  const [consulta, setConsulta] = useState('');

  // Se precalcula la forma normalizada una sola vez, no en cada pulsación.
  const preparado = useMemo(
    () => indice.map((entrada) => ({ ...entrada, clave: normalizar(entrada.nombre) })),
    [indice],
  );

  const resultados = useMemo(() => {
    const termino = normalizar(consulta);
    if (termino.length < 2) return [];

    return preparado
      .filter((entrada) => entrada.clave.includes(termino))
      // Prioriza las coincidencias por el principio del nombre.
      .sort((a, b) => {
        const inicioA = a.clave.startsWith(termino) ? 0 : 1;
        const inicioB = b.clave.startsWith(termino) ? 0 : 1;
        return inicioA - inicioB || b.total - a.total;
      })
      .slice(0, 8);
  }, [consulta, preparado]);

  const sinResultados = normalizar(consulta).length >= 2 && resultados.length === 0;

  return (
    <div className="relative">
      <label htmlFor="buscador" className="sr-only">
        Buscar tu localidad
      </label>

      <div className="flex items-center gap-2.5 rounded-xl border-2 border-tinta bg-papel-alto px-4 py-3 focus-within:border-verde">
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          className="shrink-0 text-humo"
          aria-hidden="true"
        >
          <circle cx="11" cy="11" r="7" />
          <path d="m20 20-3.5-3.5" />
        </svg>

        <input
          id="buscador"
          type="search"
          value={consulta}
          onChange={(evento) => setConsulta(evento.target.value)}
          placeholder="Escribe tu localidad. Por ejemplo: Alcalá"
          autoComplete="off"
          className="w-full bg-transparent text-base outline-none placeholder:text-humo"
        />
      </div>

      {resultados.length > 0 && (
        <ul className="absolute z-20 mt-2 w-full overflow-hidden rounded-xl border border-linea bg-papel-alto shadow-lg">
          {resultados.map((entrada) => (
            <li key={entrada.ruta} className="border-b border-linea last:border-0">
              <Link
                href={entrada.ruta}
                className="flex items-center justify-between gap-3 px-4 py-2.5 hover:bg-verde-claro"
              >
                <span className="min-w-0">
                  <span className="block truncate font-medium">{entrada.nombre}</span>
                  <span className="block truncate text-micro text-humo">{entrada.provincia}</span>
                </span>
                <span className="shrink-0 font-[family-name:var(--font-dato)] text-micro text-humo">
                  {entrada.total}
                </span>
              </Link>
            </li>
          ))}
        </ul>
      )}

      {sinResultados && (
        <p className="absolute z-20 mt-2 w-full rounded-xl border border-linea bg-papel-alto px-4 py-3 text-sm text-humo">
          No tenemos ninguna localidad con ese nombre. Prueba con el municipio más
          grande que tengas cerca.
        </p>
      )}
    </div>
  );
}
