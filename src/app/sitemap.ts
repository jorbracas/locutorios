import type { MetadataRoute } from 'next';

import { obtenerProvincias, todasLasFichas } from '@/lib/data';
import { urlAbsoluta } from '@/lib/seo';

/*
  Las páginas de provincia se omiten deliberadamente: llevan `noindex`, y
  declarar en el sitemap una URL que se pide no indexar es una señal
  contradictoria que Search Console marca como error.
*/
export default function sitemap(): MetadataRoute.Sitemap {
  const ahora = new Date();

  const estaticas: MetadataRoute.Sitemap = [
    { url: urlAbsoluta('/'), lastModified: ahora, changeFrequency: 'weekly', priority: 1 },
    { url: urlAbsoluta('/provincias'), lastModified: ahora, changeFrequency: 'monthly', priority: 0.8 },
    { url: urlAbsoluta('/contacto'), lastModified: ahora, changeFrequency: 'yearly', priority: 0.3 },
    { url: urlAbsoluta('/aviso-legal'), lastModified: ahora, changeFrequency: 'yearly', priority: 0.1 },
    { url: urlAbsoluta('/privacidad'), lastModified: ahora, changeFrequency: 'yearly', priority: 0.1 },
  ];

  const ciudades: MetadataRoute.Sitemap = obtenerProvincias().flatMap((provincia) =>
    provincia.ciudades.map((ciudad) => ({
      url: urlAbsoluta(`/${provincia.slug}/${ciudad.slug}`),
      lastModified: ahora,
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    })),
  );

  // Las fichas sin nombre comercial fiable quedan fuera del sitemap: pedir
  // que se indexe una URL que lleva `noindex` es una senal contradictoria.
  const fichas: MetadataRoute.Sitemap = todasLasFichas()
    .filter((ficha) => !ficha.excluirSitemap && !ficha.noIndexar)
    .map((ficha) => ({
    url: urlAbsoluta(`/${ficha.slugProvincia}/${ficha.slugCiudad}/${ficha.slug}`),
    lastModified: ahora,
    changeFrequency: 'monthly' as const,
    priority: 0.6,
  }));

  return [...estaticas, ...ciudades, ...fichas];
}
