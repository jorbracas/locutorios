import type { TipoFicha } from '@/lib/data';

/*
  La chapa

  No usamos fotos: todas las imágenes disponibles eran de Google (Street View
  y `lh3.googleusercontent.com`), enlazarlas incumple sus términos y esas URLs
  caducan sin aviso. En su lugar cada negocio recibe un rótulo propio.

  Es un SVG determinista: el mismo negocio produce siempre la misma chapa,
  porque el color se deriva de un hash de su identificador. Las franjas
  superiores evocan el toldo del escaparate, y el monograma toma las iniciales
  del nombre. Cero peticiones de red, cero desplazamiento de layout.
*/

type Props = {
  nombre: string;
  semilla: string;
  tipo: TipoFicha;
  /** `grande` en la ficha; `lista` en los listados. */
  tamano?: 'grande' | 'lista';
};

const PALETAS = [
  { fondo: '#0B5C4B', toldo: '#D9A21B', texto: '#F7F8F5' },
  { fondo: '#B8432B', toldo: '#F0D9A8', texto: '#F7F8F5' },
  { fondo: '#1F3A5F', toldo: '#D9A21B', texto: '#F7F8F5' },
  { fondo: '#D9A21B', toldo: '#0B5C4B', texto: '#141C1A' },
  { fondo: '#4A3B6B', toldo: '#E8C9A0', texto: '#F7F8F5' },
  { fondo: '#2C5F2D', toldo: '#E8DAB2', texto: '#F7F8F5' },
];

function hash(cadena: string): number {
  let valor = 0;
  for (let indice = 0; indice < cadena.length; indice += 1) {
    valor = (valor << 5) - valor + cadena.charCodeAt(indice);
    valor |= 0; // fuerza entero de 32 bits
  }
  return Math.abs(valor);
}

/** Iniciales del negocio, ignorando artículos y la propia palabra "locutorio". */
function iniciales(nombre: string): string {
  const ignoradas = new Set([
    'locutorio', 'locutorios', 'de', 'del', 'la', 'el', 'los', 'las',
    'y', 'en', 'ciber', 'cyber', 'call', 'shop', 'center', 'centro',
  ]);

  const palabras = nombre
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .split(/[\s.\-_/&]+/)
    .map((palabra) => palabra.replace(/[^A-Za-z0-9]/g, ''))
    .filter(Boolean);

  const significativas = palabras.filter((palabra) => !ignoradas.has(palabra.toLowerCase()));
  const elegidas = significativas.length ? significativas : palabras;

  if (!elegidas.length) return '??';
  if (elegidas.length === 1) return elegidas[0].slice(0, 2).toUpperCase();
  return (elegidas[0][0] + elegidas[1][0]).toUpperCase();
}

export default function Chapa({ nombre, semilla, tipo, tamano = 'lista' }: Props) {
  const paleta = PALETAS[hash(semilla || nombre) % PALETAS.length];
  const monograma = iniciales(nombre);
  const esGrande = tamano === 'grande';

  const alturaToldo = 22;
  const anchoCaja = 200;
  const altoCaja = esGrande ? 150 : 200;

  return (
    <svg
      viewBox={`0 0 ${anchoCaja} ${altoCaja}`}
      preserveAspectRatio="xMidYMid slice"
      className="h-full w-full"
      role="img"
      aria-label={`Rótulo de ${nombre}`}
      focusable="false"
    >
      <rect width={anchoCaja} height={altoCaja} fill={paleta.fondo} />

      {/* Toldo: franjas verticales en la banda superior. */}
      <g>
        <rect width={anchoCaja} height={alturaToldo} fill={paleta.toldo} />
        {Array.from({ length: 10 }, (_, indice) => (
          <rect
            key={indice}
            x={indice * 20}
            y={0}
            width={10}
            height={alturaToldo}
            fill={paleta.fondo}
            opacity={0.28}
          />
        ))}
      </g>

      {/* Monograma centrado bajo el toldo. */}
      <text
        x={anchoCaja / 2}
        y={alturaToldo + (altoCaja - alturaToldo) / 2}
        textAnchor="middle"
        dominantBaseline="central"
        fill={paleta.texto}
        fontFamily="'Bricolage Grotesque', system-ui, sans-serif"
        fontSize={esGrande ? 62 : 72}
        fontWeight={800}
        letterSpacing="-2"
      >
        {monograma}
      </text>

      {/* Marca discreta del tipo de establecimiento. */}
      {esGrande ? (
        <text
          x={anchoCaja / 2}
          y={altoCaja - 16}
          textAnchor="middle"
          fill={paleta.texto}
          opacity={0.65}
          fontFamily="'JetBrains Mono', monospace"
          fontSize={9}
          letterSpacing="1.5"
        >
          {tipo === 'envio' ? 'ENVÍO DE DINERO' : tipo === 'locutorio' ? 'LOCUTORIO' : 'SERVICIOS'}
        </text>
      ) : null}
    </svg>
  );
}
