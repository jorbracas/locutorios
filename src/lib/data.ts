import 'server-only';

import fs from 'node:fs';
import path from 'node:path';

/*
  Acceso a los datos del directorio.

  Los JSON se generan con `pipeline/build_data.py` a partir del CSV maestro.
  Todo se lee en tiempo de compilación: no hay base de datos ni llamadas en
  tiempo de ejecución. Los ficheros se cachean en memoria porque Next.js
  invoca estas funciones miles de veces durante el build.
*/

export type Telefono = { visible: string; enlace: string };
export type GrupoAtributos = { grupo: string; valores: string[] };
export type TipoFicha = 'locutorio' | 'envio' | 'otros';

/** Afluencia por hora derivada de `popular_times`. No es el horario oficial. */
export type DiaActividad = {
  dia: string;
  /** Tramos [inicio, fin) con afluencia registrada. */
  tramos: [number, number][];
  /** 24 valores de 0 a 100, uno por hora. */
  curva: number[];
};

export type Actividad = {
  dias: DiaActividad[];
  horaPunta: number | null;
};

export interface Ficha {
  id: string;
  nombre: string;
  slug: string;
  slugCiudad: string;
  slugProvincia: string;
  ciudad: string;
  provincia: string;
  tipo: TipoFicha;
  calle: string;
  codigoPostal: string;
  direccion: string;
  plusCode: string;
  lat: number;
  lng: number;
  telefono: Telefono | null;
  web: string;
  categoria: string;
  categorias: string[];
  atributos: GrupoAtributos[];
  actividad: Actividad | null;
  cerradoTemporalmente: boolean;
  sinVerificar: boolean;
  tier: string;
  enlaceMaps: string;
  titulo: string;
  metaTitulo: string;
  metaDescripcion: string;
  resumen: string;
  cuerpo: string;
}

export interface Ciudad {
  slug: string;
  nombre: string;
  total: number;
  lat: number;
  lng: number;
}

export interface Provincia {
  slug: string;
  nombre: string;
  total: number;
  lat: number;
  lng: number;
  ciudades: Ciudad[];
}

interface Geo {
  totalFichas: number;
  totalProvincias: number;
  totalCiudades: number;
  provincias: Provincia[];
}

const DIRECTORIO_DATOS = path.join(process.cwd(), 'data');

let geoCache: Geo | null = null;
const fichasCache = new Map<string, Ficha[]>();

function leerJSON<T>(rutaRelativa: string): T {
  const contenido = fs.readFileSync(path.join(DIRECTORIO_DATOS, rutaRelativa), 'utf8');
  return JSON.parse(contenido) as T;
}

// --------------------------------------------------------------------------
// Índice geográfico
// --------------------------------------------------------------------------

export function obtenerGeo(): Geo {
  if (!geoCache) geoCache = leerJSON<Geo>('geo.json');
  return geoCache;
}

export function obtenerProvincias(): Provincia[] {
  return obtenerGeo().provincias;
}

export function obtenerProvincia(slug: string): Provincia | null {
  return obtenerProvincias().find((provincia) => provincia.slug === slug) ?? null;
}

export function obtenerCiudad(slugProvincia: string, slugCiudad: string): Ciudad | null {
  const provincia = obtenerProvincia(slugProvincia);
  if (!provincia) return null;
  return provincia.ciudades.find((ciudad) => ciudad.slug === slugCiudad) ?? null;
}

// --------------------------------------------------------------------------
// Fichas
// --------------------------------------------------------------------------

export function fichasDeProvincia(slugProvincia: string): Ficha[] {
  const cacheada = fichasCache.get(slugProvincia);
  if (cacheada) return cacheada;

  let fichas: Ficha[] = [];
  try {
    fichas = leerJSON<Ficha[]>(path.join('listings', `${slugProvincia}.json`));
  } catch {
    fichas = [];
  }
  fichasCache.set(slugProvincia, fichas);
  return fichas;
}

export function fichasDeCiudad(slugProvincia: string, slugCiudad: string): Ficha[] {
  return fichasDeProvincia(slugProvincia).filter((ficha) => ficha.slugCiudad === slugCiudad);
}

export function obtenerFicha(
  slugProvincia: string,
  slugCiudad: string,
  slugNegocio: string,
): Ficha | null {
  return (
    fichasDeProvincia(slugProvincia).find(
      (ficha) => ficha.slugCiudad === slugCiudad && ficha.slug === slugNegocio,
    ) ?? null
  );
}

/**
 * Otras fichas de la misma ciudad, para el bloque de enlazado interno.
 * Si la ciudad tiene pocas, completa con fichas cercanas de la provincia
 * usando distancia euclídea sobre las coordenadas, que a escala provincial
 * es suficiente y evita depender de una librería geoespacial.
 */
export function fichasRelacionadas(ficha: Ficha, limite = 6): Ficha[] {
  const mismaCiudad = fichasDeCiudad(ficha.slugProvincia, ficha.slugCiudad).filter(
    (candidata) => candidata.slug !== ficha.slug,
  );

  if (mismaCiudad.length >= limite) return mismaCiudad.slice(0, limite);

  const yaIncluidas = new Set(mismaCiudad.map((candidata) => candidata.id));
  const cercanas = fichasDeProvincia(ficha.slugProvincia)
    .filter(
      (candidata) =>
        candidata.id !== ficha.id &&
        !yaIncluidas.has(candidata.id) &&
        candidata.slugCiudad !== ficha.slugCiudad,
    )
    .map((candidata) => ({
      ficha: candidata,
      distancia: (candidata.lat - ficha.lat) ** 2 + (candidata.lng - ficha.lng) ** 2,
    }))
    .sort((a, b) => a.distancia - b.distancia)
    .slice(0, limite - mismaCiudad.length)
    .map((entrada) => entrada.ficha);

  return [...mismaCiudad, ...cercanas];
}

// --------------------------------------------------------------------------
// Rutas
// --------------------------------------------------------------------------

export function rutaProvincia(slug: string): string {
  return `/${slug}`;
}

export function rutaCiudad(slugProvincia: string, slugCiudad: string): string {
  return `/${slugProvincia}/${slugCiudad}`;
}

export function rutaFicha(ficha: Pick<Ficha, 'slugProvincia' | 'slugCiudad' | 'slug'>): string {
  return `/${ficha.slugProvincia}/${ficha.slugCiudad}/${ficha.slug}`;
}

/** Todas las fichas del país. Solo para sitemaps: recorre los 52 ficheros. */
export function todasLasFichas(): Ficha[] {
  return obtenerProvincias().flatMap((provincia) => fichasDeProvincia(provincia.slug));
}
