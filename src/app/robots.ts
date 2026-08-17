import type { MetadataRoute } from 'next';

import { SITIO, urlAbsoluta } from '@/lib/seo';

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: '*',
        allow: '/',
        // Las provincias se bloquean por meta robots, no aquí: si se
        // impidiera el rastreo, Google no llegaría a leer el `noindex`
        // ni seguiría los enlaces hacia las localidades.
        disallow: ['/api/'],
      },
    ],
    sitemap: urlAbsoluta('/sitemap.xml'),
    host: SITIO.dominio,
  };
}
