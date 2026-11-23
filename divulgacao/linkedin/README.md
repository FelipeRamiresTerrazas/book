# Posts do LinkedIn

Rascunhos dos posts e das edições da newsletter que divulgam o livro. A estratégia, o
calendário por fase e o checklist de lançamento estão em `notas/04-lancamento.md`.

## Pilares

| Pilar | Peso | O que é |
|---|---|---|
| Ideia | ~40% | Um conceito do livro por post, com a opinião do autor e uma pergunta no fim |
| Bastidores | ~25% | Como o livro está sendo feito: decisões, ferramentas, fontes, título, capa |
| Experiência | ~20% | Uma lição de projeto real. O relato vem sempre do Felipe |
| Enquete | ~15% | Ouvir o público. O resultado vira post ou entra no livro |

## Regras

As mesmas do livro (`CLAUDE.md`), mais algumas próprias do LinkedIn.

- Voz do Felipe, em português brasileiro, falando com o leitor. Opinião em primeira
  pessoa, com moderação.
- Sem travessão. Sem fórmulas de texto de IA: "não é apenas X, é Y", trios de adjetivos
  para soar completo, frase de efeito no fim.
- **Nenhum relato inventado.** Onde cabe uma história vivida, o rascunho traz
  `[RELATO: ...]` dizendo que história caberia ali. Sem nome de empresa, cliente, colega
  ou sistema interno; números só em ordem de grandeza.
- **Fato com fonte.** Data, definição ou número citado precisa de uma chave do
  `referencias.bib`. Enquanto a entrada estiver com `CONFERIR` no `.bib`, o post leva
  `[CONFERIR chave]` e só é publicado depois da checagem.
- As duas primeiras linhas carregam o post: o LinkedIn corta o texto em cerca de 210
  caracteres antes do "ver mais".
- Até 3.000 caracteres no post (a newsletter pode ser mais longa). No máximo 3 hashtags.
- O LinkedIn não interpreta Markdown: nada de negrito com asteriscos. Listas com `•` ou
  números.
- Enquete: até 4 opções, cada uma com até 30 caracteres.
- Carrossel: PDF de 6 a 10 páginas, quadrado ou 4:5, reaproveitando os diagramas TikZ de
  `figuras/` sempre que der, para ter a cara do livro.
- A identidade visual da YMX não se aplica: o livro é projeto pessoal.

## Arquivos

Um arquivo por post: `AAAA-MM-DD-slug.md`, com a data prevista de publicação. Cada um tem
um cabeçalho, o texto pronto para colar e, no fim, notas para o Felipe (o que preencher,
o que conferir, ideias de imagem).

```
# Título interno do post

- Data: 2026-12-01 (ter)
- Pilar: bastidores
- Origem: capítulo ou nota de onde o conteúdo saiu
- Formato: texto | enquete | carrossel | newsletter
- Status: rascunho | revisado | publicado
- Link: (preencher depois de publicar)
```

## Fluxo

1. **Rascunho.** O Claude escreve a partir do capítulo de origem.
2. **Revisado.** O Felipe preenche os `[RELATO]`, resolve os `[CONFERIR]`, ajusta a voz.
3. **Publicado.** O Felipe publica, anota o link e, uma semana depois, os números do post
   na planilha de métricas.

Perguntas boas dos comentários vão para `pautas.md`.
