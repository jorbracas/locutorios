import Link from 'next/link';

export default function NoEncontrado() {
  return (
    <div className="mx-auto max-w-xl px-4 py-24 text-center">
      <p className="mb-3 font-[family-name:var(--font-dato)] text-micro tracking-[0.18em] text-verde uppercase">
        Error 404
      </p>
      <h1 className="mb-4 text-3xl">Esta página no existe</h1>
      <p className="mb-8 text-humo">
        Puede que el establecimiento ya no esté en el directorio o que la dirección
        tenga alguna errata. Busca tu localidad desde la portada.
      </p>
      <Link
        href="/"
        className="inline-block rounded-lg bg-verde px-5 py-2.5 font-semibold text-papel-alto hover:opacity-90"
      >
        Volver a la portada
      </Link>
    </div>
  );
}
