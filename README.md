# Livro: análise e engenharia de dados antes e depois da IA

Projeto LaTeX de um livro para impressão (primeira edição), no formato 16 x 23 cm.
Título de trabalho: *Do Cubo ao Copiloto* (provisório, ver `notas/02-titulos.md`).

## Compilar

Precisa de MiKTeX (ou TeX Live) com `latexmk` e `biber`, e Python 3.

```
python compilar.py                  # rascunho: mostra notas do autor e pendências
python compilar.py --modo final     # limpo, 16 x 23 cm, para gráfica por demanda
python compilar.py --modo grafica   # limpo, em A4 com marcas de corte
python compilar.py --modo todos     # os três
python compilar.py amostra          # página de teste do estilo
```

Os PDFs saem em `output/` (fora do git). O script informa páginas, pendências e
referências indefinidas. No VS Code, as receitas do LaTeX Workshop fazem o mesmo.

## Mapa

| Caminho | O que é |
|---|---|
| `main.tex` | Documento principal: ordem das partes e capítulos |
| `metadados.tex` | Título, subtítulo, autor, edição, ISBN (um lugar só) |
| `estilo/livro.sty` | Todo o visual: formato, margens, fontes, capítulos, caixas, código |
| `estilo/amostra.tex` | Capítulo de teste com todos os elementos, para validar mudanças de estilo |
| `abertura/` | Folha de rosto, créditos, dedicatória, prefácio, como ler |
| `capitulos/` | Um arquivo por capítulo, na ordem do livro, e o epílogo por último (a ordem oficial é a do `main.tex`) |
| `apendices/` | Glossário e sobre o autor |
| `referencias.bib` | Bibliografia (biblatex, autor-data) |
| `figuras/` | Imagens e diagramas |
| `notas/` | Planejamento: proposta, títulos, decisões |

## Comandos do estilo

| Comando | Uso |
|---|---|
| `\rascunho{...}` | Nota de planejamento, só aparece no PDF de rascunho |
| `\pendente{...}` | Algo a resolver; marcado no rascunho e contado pelo `compilar.py` |
| `\veja{sec:rotulo}` | Remissão a seção (sem número): *Nome da seção* (p. 42) |
| `\codigo{...}` | Código no meio da frase |
| `relato` | Caixa "Da minha experiência", para relatos de projetos reais |
| `destaque` | Ideia-chave em uma ou duas frases |
| `dica` | Caixa "Na prática" (título opcional: `\begin{dica}[Outro título]`) |
| `\antesdepois{antes}{depois}` | Comparação lado a lado, antes e depois da IA |
| `sql`, `python`, `terminal` | Blocos de código |
| `\epigraph{texto}{fonte}` | Epígrafe na abertura do capítulo |
| `\fonte{...}` | Linha "Fonte:" embaixo de figura ou tabela |
| `leituras` + `\leitura{chave}{comentário}` | Seção "Para ir além" no fim do capítulo, com leituras comentadas |
| `\textcite{chave}`, `\parencite{chave}` | Citação: Kimball e Ross (2013) / (Kimball e Ross, 2013) |

Diagramas em TikZ ficam em `figuras/*.tex` e usam os estilos do `livro.sty`
(`caixa`, `banco`, `tabela`, `seta`, `rotulo`, `moldura`), para todos terem a mesma cara.

## Formato e impressão

- 16 x 23 cm, margem interna (lombada) 22 mm, externa 17 mm. Para outro formato
  (14 x 21 cm, ou 6 x 9 pol. da Amazon KDP), mude `\larguralivro` e `\alturalivro`
  no começo de `estilo/livro.sty`.
- Miolo em tons de cinza, pensado para impressão P&B. Fundos de caixa bem claros.
- Partes e capítulos abrem sempre em página ímpar.
- A capa é um arquivo separado, feito depois, quando o número de páginas (e a
  largura da lombada) estiver fechado.
