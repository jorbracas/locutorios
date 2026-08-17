import type { Metadata } from 'next';

import { Migas } from '@/components/Ui';
import { urlAbsoluta } from '@/lib/seo';

export const metadata: Metadata = {
  title: 'Corregir una ficha',
  description:
    'Cómo comunicar un error, un cambio de horario o la baja de un establecimiento del directorio.',
  alternates: { canonical: urlAbsoluta('/contacto') },
};

export default function PaginaContacto() {
  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <Migas
        migas={[
          { nombre: 'Inicio', ruta: '/' },
          { nombre: 'Corregir una ficha', ruta: '/contacto' },
        ]}
      />

      <h1 className="mb-6 text-3xl">Corregir una ficha</h1>

      <div className="editorial">
        <p>
          Los datos de este directorio proceden de fuentes públicas y no siempre están
          al día. Si algo no cuadra, escríbenos y lo revisamos.
        </p>

        <h2>Qué nos ayuda más recibir</h2>
        <ul>
          <li>El horario de apertura, que es el dato que más nos falta.</li>
          <li>Un teléfono o una dirección que hayan cambiado.</li>
          <li>Establecimientos que hayan cerrado.</li>
          <li>Locutorios que no aparezcan en el directorio.</li>
        </ul>

        <h2>Si eres el titular del negocio</h2>
        <p>
          Puedes pedirnos que actualicemos la información de tu establecimiento o que
          lo retiremos del directorio. Indícanos el nombre y la dirección exacta y nos
          ocupamos.
        </p>

        <h2>Escríbenos</h2>
        <p>
          <a
            href="mailto:hola@locutorioscercademi.com"
            className="font-medium text-verde underline underline-offset-4"
          >
            hola@locutorioscercademi.com
          </a>
        </p>
      </div>
    </div>
  );
}
