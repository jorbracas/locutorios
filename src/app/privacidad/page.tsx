import type { Metadata } from 'next';

import { Migas } from '@/components/Ui';
import { SITIO, urlAbsoluta } from '@/lib/seo';

export const metadata: Metadata = {
  title: 'Política de privacidad',
  description: `Cómo trata los datos personales ${SITIO.nombre}.`,
  alternates: { canonical: urlAbsoluta('/privacidad') },
  robots: { index: false, follow: true },
};

export default function PaginaPrivacidad() {
  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <Migas
        migas={[
          { nombre: 'Inicio', ruta: '/' },
          { nombre: 'Privacidad', ruta: '/privacidad' },
        ]}
      />

      <h1 className="mb-6 text-3xl">Política de privacidad</h1>

      <div className="editorial">
        <p className="rounded-lg border-l-4 border-mostaza bg-mostaza-claro px-4 py-3">
          <strong>Pendiente de completar.</strong> Este texto refleja el estado actual
          del sitio, sin analítica ni publicidad. Si añades Analytics, AdSense o un
          formulario, hay que revisarlo y añadir un banner de consentimiento.
        </p>

        <h2>Qué datos recogemos</h2>
        <p>
          Ahora mismo, ninguno. El sitio no usa cookies propias, no incorpora analítica
          ni publicidad, y no dispone de formularios ni de registro de usuarios.
        </p>

        <h2>Servicios de terceros</h2>
        <p>
          Al pulsar «Ver mapa» se carga un mapa de OpenStreetMap, que recibirá tu
          dirección IP para poder servirlo. El mapa no se carga hasta que lo solicitas
          expresamente. Las tipografías se sirven desde Google Fonts.
        </p>

        <h2>Enlaces salientes</h2>
        <p>
          Los enlaces de «Cómo llegar» abren Google Maps, que aplica su propia política
          de privacidad. No controlamos qué datos recoge.
        </p>

        <h2>Tus derechos</h2>
        <p>
          Puedes ejercer los derechos de acceso, rectificación, supresión, oposición,
          limitación y portabilidad escribiendo a hola@locutorioscercademi.com. Si
          consideras que no atendemos correctamente tu solicitud, puedes reclamar ante
          la Agencia Española de Protección de Datos.
        </p>
      </div>
    </div>
  );
}
