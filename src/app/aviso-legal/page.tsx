import type { Metadata } from 'next';

import { Migas } from '@/components/Ui';
import { SITIO, urlAbsoluta } from '@/lib/seo';

export const metadata: Metadata = {
  title: 'Aviso legal',
  description: `Condiciones de uso y titularidad de ${SITIO.nombre}.`,
  alternates: { canonical: urlAbsoluta('/aviso-legal') },
  robots: { index: false, follow: true },
};

export default function PaginaAvisoLegal() {
  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <Migas
        migas={[
          { nombre: 'Inicio', ruta: '/' },
          { nombre: 'Aviso legal', ruta: '/aviso-legal' },
        ]}
      />

      <h1 className="mb-6 text-3xl">Aviso legal</h1>

      <div className="editorial">
        <p className="rounded-lg border-l-4 border-mostaza bg-mostaza-claro px-4 py-3">
          <strong>Pendiente de completar.</strong> Sustituye los campos entre corchetes
          por los datos reales del titular antes de publicar. La LSSI obliga a
          identificar al responsable del sitio.
        </p>

        <h2>Titularidad</h2>
        <p>
          Este sitio web es titularidad de [nombre o razón social], con NIF [NIF] y
          domicilio en [dirección]. Correo de contacto: hola@locutorioscercademi.com.
        </p>

        <h2>Objeto del sitio</h2>
        <p>
          {SITIO.nombre} es un directorio informativo de locutorios y puntos de envío
          de dinero en España. No prestamos servicios de telecomunicaciones, de envío
          de dinero ni de cambio de divisa, ni mantenemos relación comercial con los
          establecimientos listados salvo que se indique expresamente.
        </p>

        <h2>Exactitud de la información</h2>
        <p>
          La información procede de fuentes públicas y puede estar desactualizada.
          Horarios, servicios, tarifas y comisiones deben confirmarse directamente con
          cada establecimiento. No respondemos de las decisiones tomadas a partir de
          los datos publicados aquí.
        </p>

        <h2>Retirada de contenidos</h2>
        <p>
          Cualquier titular de un establecimiento puede solicitar la corrección o la
          retirada de su ficha escribiendo a la dirección de contacto. Atendemos estas
          peticiones sin necesidad de justificación.
        </p>

        <h2>Propiedad intelectual</h2>
        <p>
          Los textos descriptivos y el diseño del sitio son originales y están
          protegidos. Los nombres comerciales y marcas de los establecimientos
          pertenecen a sus respectivos titulares y se emplean únicamente con fines
          identificativos.
        </p>
      </div>
    </div>
  );
}
