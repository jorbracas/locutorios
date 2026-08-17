import type { TipoFicha } from '@/lib/data';

/*
  Ilustraciones

  40 imágenes generadas específicamente para este proyecto: 20 fachadas
  (día y noche) y 20 interiores y detalles de mostrador. No son fotos de los
  establecimientos reales, así que se usan con dos reglas fijas:

  - Nunca en la cabecera de la ficha. Ahí manda la chapa, que sí es única de
    cada negocio. Estas van dentro del contenido, acompañando al texto.
  - Siempre con pie de foto que aclara que la imagen no corresponde a ese
    establecimiento.

  El reparto por tipo importa: una imagen de mostrador de envío de dinero en
  una ficha de tipo "locutorio" sin ese servicio sería contradictoria con el
  propio texto editorial. Las fachadas (día y noche) son neutras y sirven
  para cualquier tipo; los interiores y detalles sí están acotados.
*/

const FACHADAS = [
  'facade_dia_madrid_estrecha',
  'facade_dia_barcelona_eixample',
  'facade_dia_andalucia_cal',
  'facade_dia_valencia_naranjos',
  'facade_dia_sevilla_entre_comercios',
  'facade_dia_norte_nublado',
  'facade_dia_suburbio_moderno',
  'facade_dia_peatonal',
  'facade_dia_persiana_a_medias',
  'facade_dia_pueblo_castellano',
  'facade_noche_lluvia',
  'facade_noche_hora_azul',
  'facade_noche_invierno_frio',
  'facade_noche_casco_antiguo',
  'facade_noche_persiana_bajada',
  'facade_noche_verano_puerta_abierta',
  'facade_noche_calle_comercial',
  'facade_noche_terraza_bar',
  'facade_noche_desde_dentro_lluvia',
  'facade_noche_reflejo_charco',
];

const POR_TIPO: Record<TipoFicha, string[]> = {
  locutorio: [
    ...FACHADAS,
    'interior_vista_general',
    'interior_fila_ordenadores',
    'interior_reformado_moderno',
    'interior_antiguo_cuidado',
    'interior_estrecho_largo',
    'interior_rincon_impresion',
    'interior_sala_espera',
    'interior_desde_mostrador',
    'interior_tarde_tranquila',
    'detalle_impresora_copia',
    'detalle_foto_carnet',
    'detalle_laminadora_papeleria',
  ],
  envio: [
    ...FACHADAS,
    'interior_mostrador_cliente',
    'detalle_formulario_envios',
    'detalle_terminal_pago',
    'detalle_paquetes_sobres',
    'detalle_euros_mostrador',
    'detalle_mostrador_cliente',
  ],
  otros: [
    ...FACHADAS,
    'detalle_tarjetas_sim',
    'detalle_accesorios_telefonia',
    'interior_vista_general',
    'interior_reformado_moderno',
  ],
};

const DESCRIPCION: Record<string, string> = {
  facade_dia_madrid_estrecha: 'Fachada estrecha de un locutorio en una calle de ciudad',
  facade_dia_barcelona_eixample: 'Locutorio en un edificio de fachada alta con grandes ventanales',
  facade_dia_andalucia_cal: 'Locutorio de fachada encalada con luz de mediodía',
  facade_dia_valencia_naranjos: 'Locutorio en una calle con naranjos y una moto aparcada',
  facade_dia_sevilla_entre_comercios: 'Locutorio entre una peluquería y una frutería',
  facade_dia_norte_nublado: 'Fachada de locutorio con cielo nublado y pavimento húmedo',
  facade_dia_suburbio_moderno: 'Locutorio de fachada amplia en un bloque residencial moderno',
  facade_dia_peatonal: 'Locutorio en una calle peatonal empedrada',
  facade_dia_persiana_a_medias: 'Locutorio con la persiana metálica medio subida por la mañana',
  facade_dia_pueblo_castellano: 'Locutorio de un pueblo, edificio bajo y acera amplia',
  facade_noche_lluvia: 'Fachada de locutorio de noche con lluvia, reflejos en el asfalto',
  facade_noche_hora_azul: 'Locutorio al anochecer con el rótulo recién encendido',
  facade_noche_invierno_frio: 'Locutorio en una tarde fría de invierno, interior cálido',
  facade_noche_casco_antiguo: 'Locutorio en una calle estrecha del casco antiguo, de noche',
  facade_noche_persiana_bajada: 'Locutorio cerrado con la persiana bajada, farola encendida',
  facade_noche_verano_puerta_abierta: 'Locutorio con la puerta abierta en una noche de verano',
  facade_noche_calle_comercial: 'Locutorio en una calle comercial concurrida al anochecer',
  facade_noche_terraza_bar: 'Locutorio junto a una terraza de bar por la noche',
  facade_noche_desde_dentro_lluvia: 'Vista desde dentro del locutorio hacia la calle con lluvia',
  facade_noche_reflejo_charco: 'Rótulo de locutorio reflejado en un charco por la noche',
  interior_vista_general: 'Vista general del interior de un locutorio',
  interior_mostrador_cliente: 'Mostrador de un locutorio con una persona siendo atendida',
  interior_fila_ordenadores: 'Fila de puestos de ordenador en un locutorio',
  interior_reformado_moderno: 'Interior reformado de un locutorio, madera y tonos claros',
  interior_antiguo_cuidado: 'Interior de un locutorio clásico, bien conservado',
  interior_estrecho_largo: 'Interior alargado de un locutorio, mostrador y puestos a los lados',
  interior_rincon_impresion: 'Rincón de impresión y fotocopias de un locutorio',
  interior_sala_espera: 'Pequeña zona de espera dentro de un locutorio',
  interior_desde_mostrador: 'Interior de un locutorio visto desde detrás del mostrador',
  interior_tarde_tranquila: 'Interior de un locutorio en un momento tranquilo de la tarde',
  detalle_formulario_envios: 'Persona rellenando un formulario de envío de dinero',
  detalle_terminal_pago: 'Datáfono con un recibo de pago en un mostrador',
  detalle_tarjetas_sim: 'Expositor de tarjetas SIM y recargas prepago',
  detalle_impresora_copia: 'Impresora multifunción haciendo una copia',
  detalle_accesorios_telefonia: 'Estantería de accesorios y fundas para el móvil',
  detalle_paquetes_sobres: 'Paquetes y sobres preparados para su envío',
  detalle_foto_carnet: 'Rincón para hacer fotografías de carné',
  detalle_mostrador_cliente: 'Mostrador de atención visto desde el lado del cliente',
  detalle_euros_mostrador: 'Billetes y monedas de euro sobre un mostrador',
  detalle_laminadora_papeleria: 'Plastificadora y material de papelería en un locutorio',
};

function hash(cadena: string): number {
  let valor = 0;
  for (let indice = 0; indice < cadena.length; indice += 1) {
    valor = (valor << 5) - valor + cadena.charCodeAt(indice);
    valor |= 0;
  }
  return Math.abs(valor);
}

type Props = {
  /** Determina qué conjunto de imágenes es apropiado. */
  tipo: TipoFicha;
  /** Reparte las imágenes de forma estable: el mismo negocio, la misma imagen. */
  semilla: string;
  ancho?: 720 | 1400;
  className?: string;
};

export default function Ilustracion({ tipo, semilla, ancho = 720, className = '' }: Props) {
  const candidatas = POR_TIPO[tipo];
  const elegida = candidatas[hash(semilla) % candidatas.length];
  const sufijo = ancho === 720 ? '-720' : '';

  return (
    <figure className={className}>
      <img
        src={`/ilustraciones/${elegida}${sufijo}.webp`}
        alt={DESCRIPCION[elegida] ?? 'Interior de un locutorio'}
        width={ancho}
        height={Math.round(ancho * 0.75)}
        loading="lazy"
        decoding="async"
        className="w-full rounded-xl border border-linea object-cover"
      />
      <figcaption className="mt-1.5 text-micro text-humo">
        Imagen ilustrativa. No corresponde a este establecimiento.
      </figcaption>
    </figure>
  );
}
