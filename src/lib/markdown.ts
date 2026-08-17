import type { ReactNode } from 'react';
import { createElement, Fragment } from 'react';

/*
  Renderizador mínimo de markdown.

  El texto editorial solo usa encabezados `##`, párrafos, alguna lista `-`
  y negrita ocasional. Escribir estas 60 líneas evita añadir una dependencia
  de parseo y, sobre todo, evita `dangerouslySetInnerHTML`: el contenido se
  convierte en nodos de React, así que no hay superficie de inyección.
*/

type Bloque =
  | { tipo: 'h2'; texto: string }
  | { tipo: 'p'; texto: string }
  | { tipo: 'ul'; elementos: string[] };

function trocearBloques(markdown: string): Bloque[] {
  const bloques: Bloque[] = [];
  let listaAbierta: string[] = [];

  const cerrarLista = () => {
    if (listaAbierta.length) {
      bloques.push({ tipo: 'ul', elementos: listaAbierta });
      listaAbierta = [];
    }
  };

  for (const parrafo of markdown.split(/\n{2,}/)) {
    const limpio = parrafo.trim();
    if (!limpio) continue;

    if (limpio.startsWith('## ')) {
      cerrarLista();
      bloques.push({ tipo: 'h2', texto: limpio.slice(3).trim() });
      continue;
    }

    if (/^[-*]\s/.test(limpio)) {
      for (const linea of limpio.split('\n')) {
        const elemento = linea.replace(/^[-*]\s+/, '').trim();
        if (elemento) listaAbierta.push(elemento);
      }
      continue;
    }

    cerrarLista();
    bloques.push({ tipo: 'p', texto: limpio.replace(/\n/g, ' ') });
  }

  cerrarLista();
  return bloques;
}

/** Convierte `**negrita**` en <strong>, dejando el resto como texto plano. */
function conNegrita(texto: string, clave: string): ReactNode {
  if (!texto.includes('**')) return texto;

  const partes = texto.split(/(\*\*[^*]+\*\*)/g).filter(Boolean);
  return createElement(
    Fragment,
    null,
    ...partes.map((parte, indice) =>
      parte.startsWith('**') && parte.endsWith('**')
        ? createElement('strong', { key: `${clave}-${indice}` }, parte.slice(2, -2))
        : parte,
    ),
  );
}

/**
 * Devuelve los nodos del cuerpo editorial.
 * Los `id` de los H2 permiten enlazar secciones desde un índice si hiciera falta.
 */
export function renderizarEditorial(markdown: string): ReactNode[] {
  return trocearBloques(markdown).map((bloque, indice) => {
    const clave = `bloque-${indice}`;

    if (bloque.tipo === 'h2') {
      return createElement('h2', { key: clave }, bloque.texto);
    }

    if (bloque.tipo === 'ul') {
      return createElement(
        'ul',
        { key: clave },
        bloque.elementos.map((elemento, posicion) =>
          createElement('li', { key: `${clave}-${posicion}` }, conNegrita(elemento, clave)),
        ),
      );
    }

    return createElement('p', { key: clave }, conNegrita(bloque.texto, clave));
  });
}

/** Cuenta palabras del cuerpo, para mostrar tiempo de lectura si se quisiera. */
export function contarPalabras(markdown: string): number {
  return markdown.replace(/[#*_-]/g, ' ').split(/\s+/).filter(Boolean).length;
}
