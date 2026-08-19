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

const nextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  // El directorio se sirve como HTML estatico: sin barra final en las URLs.
  trailingSlash: false,
  eslint: { ignoreDuringBuilds: true },
  async redirects() {
    return redirects;
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
