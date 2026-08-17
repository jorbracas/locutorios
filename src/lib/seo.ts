import type { Ficha } from './data';

export const SITIO = {
  nombre: 'Locutorios cerca de mí',
  dominio: 'https://locutorioscercademi.com',
  descripcion:
    'Directorio de locutorios y puntos de envío de dinero en España. Dirección, teléfono y cómo llegar, provincia a provincia.',
  idioma: 'es-ES',
} as const;

export function urlAbsoluta(ruta: string): string {
  return `${SITIO.dominio}${ruta.startsWith('/') ? ruta : `/${ruta}`}`;
}

/**
 * Etiqueta legible del tipo de establecimiento.
 * `otros` agrupa negocios cuya categoría en origen no era concluyente:
 * se publican, pero el texto nunca afirma que sean locutorios.
 */
export const ETIQUETA_TIPO: Record<Ficha['tipo'], string> = {
  locutorio: 'Locutorio',
  envio: 'Envío de dinero',
  otros: 'Servicios varios',
};

/*
  JSON-LD

  Decisión deliberada: NO se emite `aggregateRating` ni `review`.
  Las valoraciones proceden de Google, no las hemos recogido nosotros, y
  marcarlas como propias incumple la política de datos estructurados de
  Google y expone el dominio a una acción manual. El marcado se limita a los
  hechos verificables del negocio: nombre, dirección, coordenadas y teléfono.
*/

export function jsonLdNegocio(ficha: Ficha) {
  const datos: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    '@id': urlAbsoluta(`/${ficha.slugProvincia}/${ficha.slugCiudad}/${ficha.slug}#negocio`),
    name: ficha.nombre,
    url: urlAbsoluta(`/${ficha.slugProvincia}/${ficha.slugCiudad}/${ficha.slug}`),
    address: {
      '@type': 'PostalAddress',
      streetAddress: ficha.calle || undefined,
      addressLocality: ficha.ciudad,
      addressRegion: ficha.provincia,
      postalCode: ficha.codigoPostal || undefined,
      addressCountry: 'ES',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: ficha.lat,
      longitude: ficha.lng,
    },
  };

  if (ficha.telefono) datos.telephone = ficha.telefono.visible;
  if (ficha.web) datos.sameAs = [ficha.web];
  if (ficha.categoria) datos.description = ficha.resumen || undefined;

  return datos;
}

export function jsonLdMigas(migas: { nombre: string; ruta: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: migas.map((miga, indice) => ({
      '@type': 'ListItem',
      position: indice + 1,
      name: miga.nombre,
      item: urlAbsoluta(miga.ruta),
    })),
  };
}

export function jsonLdListado(fichas: Ficha[], titulo: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: titulo,
    numberOfItems: fichas.length,
    itemListElement: fichas.slice(0, 50).map((ficha, indice) => ({
      '@type': 'ListItem',
      position: indice + 1,
      name: ficha.nombre,
      url: urlAbsoluta(`/${ficha.slugProvincia}/${ficha.slugCiudad}/${ficha.slug}`),
    })),
  };
}
