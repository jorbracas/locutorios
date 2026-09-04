/** @type {import('next').NextConfig} */

/*
  Redirects permanentes por movimientos geograficos.

  Cada entrada corresponde a una ficha o una localidad que cambio de URL en la
  pasada de correccion geografica (ver data/informe-migracion-geografica.json
  para el detalle y el motivo de cada movimiento). El sitio ya esta publicado,
  asi que ninguna URL antigua puede quedar en 404: todas resuelven en un solo
  salto, nunca en cadena (A -> B -> C), directamente a su destino final.
*/
const redirects = [
  { source: '/barcelona/santa-coloma-de-gramenet/badalinks', destination: '/barcelona/badalona/badalinks', permanent: true },
  { source: '/bizkaia/elexalde/locutorio-bar-caferteria', destination: '/bizkaia/basauri/locutorio-bar-caferteria', permanent: true },
  { source: '/bizkaia/elexalde/besmi-allah', destination: '/bizkaia/leioa/besmi-allah', permanent: true },
  { source: '/bizkaia/lejona/noshi-locutorio', destination: '/bizkaia/leioa/noshi-locutorio', permanent: true },
  { source: '/cadiz/el/ciber-locutorio-el-puerto', destination: '/cadiz/el-puerto-de-sta-maria/ciber-locutorio-el-puerto', permanent: true },
  { source: '/castellon/alcossebre-castellon/prensa-locutorio-paris-tombuctu', destination: '/castellon/alcossebre/prensa-locutorio-paris-tombuctu', permanent: true },
  { source: '/girona/girona/locutorio-euroenvia', destination: '/girona/salt/locutorio-euroenvia', permanent: true },
  { source: '/girona/girona/moneygram', destination: '/girona/salt/moneygram', permanent: true },
  { source: '/illes-balears/santa-eulalia-del-rio/locutorio-kafoul', destination: '/illes-balears/santa-eularia-des-riu/locutorio-kafoul', permanent: true },
  { source: '/murcia/murcia/locutorio-mundo', destination: '/murcia/puente-tocinos/locutorio-mundo', permanent: true },
  { source: '/murcia/murcia/locutorio-essallam', destination: '/murcia/beniajan/locutorio-essallam', permanent: true },
  { source: '/valencia/valencia/locutorio-danish', destination: '/valencia/mislata/locutorio-danish', permanent: true },
  { source: '/valencia/valencia/international-locutorio-sanfer', destination: '/valencia/mislata/international-locutorio-sanfer', permanent: true },
  { source: '/bizkaia/arizgoiti/moon-mart-locutorio-basauri-productos-latinos-locutorio-servicio-de-paqueteria-accesorios-y-reparacion-de-moviles', destination: '/bizkaia/basauri/moon-mart-locutorio-basauri-productos-latinos-locutorio-servicio-de-paqueteria-accesorios-y-reparacion-de-moviles', permanent: true },
  { source: '/castellon/castellon/pak-movil-store-reparacion-moviles-envios-dinero', destination: '/castellon/castellon-de-la-plana/pak-movil-store-reparacion-moviles-envios-dinero', permanent: true },
  // Localidades que se quedaron sin fichas: redirect de la pagina de ciudad.
  { source: '/bizkaia/lejona', destination: '/bizkaia/leioa', permanent: true },
  { source: '/cadiz/el', destination: '/cadiz/el-puerto-de-sta-maria', permanent: true },
  { source: '/castellon/alcossebre-castellon', destination: '/castellon/alcossebre', permanent: true },
  { source: '/illes-balears/santa-eulalia-del-rio', destination: '/illes-balears/santa-eularia-des-riu', permanent: true },
  { source: '/bizkaia/arizgoiti', destination: '/bizkaia/basauri', permanent: true },
  { source: '/castellon/castellon', destination: '/castellon/castellon-de-la-plana', permanent: true },
];

/*
  Redirect de dominio, forzado desde la propia aplicacion.

  Motivo: el canonical de este sitio (SITIO.dominio en src/lib/seo.ts) ha
  cambiado varias veces entre 'con www' y 'sin www' en pocos dias, por obra de
  distintas herramientas trabajando sobre el mismo repositorio sin
  coordinarse. El resultado medido en Search Console: al 4 de septiembre de
  2026, cerca del 10% de las URLs con impresiones seguian apareciendo bajo la
  forma sin www, señal de que Google tiene el mismo contenido indexado bajo
  dos dominios distintos.

  Hasta ahora el redirect apex -> www solo existia a nivel de plataforma
  (configuracion de dominios en Vercel). Esta entrada lo fuerza tambien desde
  el codigo, para que el comportamiento no dependa de un ajuste externo que
  cualquier herramienta podria tocar sin saber por que esta ahi. Si esto
  vuelve a necesitar cambiarse, que sea una decision explicita, documentada
  aqui, no un efecto secundario de otra tarea.
*/
const redirectDominioWWW = {
  source: '/:path*',
  has: [{ type: 'host', value: 'locutorioscercademi.com' }],
  destination: 'https://www.locutorioscercademi.com/:path*',
  permanent: true,
};


const nextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  // El directorio se sirve como HTML estatico: sin barra final en las URLs.
  trailingSlash: false,
  eslint: { ignoreDuringBuilds: true },
  async redirects() {
    // El de dominio va primero: si alguien llega por el apex sin www, debe
    // saltar directo a la version con www antes de evaluar cualquier otra
    // regla, para que nunca haya un A -> B -> C.
    return [redirectDominioWWW, ...redirects];
  },
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
          { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
        ],
      },
    ];
  },
};

export default nextConfig;
