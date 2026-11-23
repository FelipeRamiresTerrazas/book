# Inmon e Kimball, três décadas depois

- Data: 2026-12-09 (qua)
- Pilar: ideia
- Origem: cap. *O data warehouse e a modelagem dimensional* (`capitulos/02-data-warehouse.tex`); destaque do cap. *Arquitetura medalhão* (`capitulos/13-arquitetura-medalhao.tex`); `\veja{sec:consulta-errada}`
- Formato: texto, com imagem
- Status: rascunho
- Link:

## Texto

Em 1992, Bill Inmon publicou o livro que popularizou o termo data warehouse. Quatro anos depois, Ralph Kimball publicou o dele, com outra proposta. [CONFERIR inmon1992, kimball1996]

Três décadas, uma nuvem e uma IA depois, ainda vale estudar os dois? Acho que sim, e o capítulo sobre data warehouse do livro que estou escrevendo existe por isso.

Em poucas linhas:

Inmon propõe começar de cima. Primeiro se modela a empresa, depois se carrega um armazém central e normalizado, e os data marts de cada área derivam dele. A força é a consistência: todas as áreas partem dos mesmos dados. A fraqueza é o tempo até a primeira entrega.

Kimball propõe começar por um processo de negócio de cada vez: vendas, depois estoque, depois compras. Cada um ganha um modelo dimensional, e o que impede o conjunto de virar um amontoado de bases isoladas são as dimensões conformadas, as mesmas tabelas de data, produto e cliente em todos os modelos.

O que eu levo dos dois para o trabalho de hoje:

1. A pergunta do grão. "Uma linha desta tabela representa o quê?" É ela que evita somar o frete de um pedido uma vez para cada item, com ou sem IA escrevendo a consulta.
2. Dimensão conformada é master data com outro nome. Sem um cadastro mestre por trás, nenhuma se sustenta.
3. A arquitetura medalhão diz em que estágio cada dado está. A modelagem diz como ele deve ser desenhado. Uma não substitui a outra.

Você aprendeu Inmon, Kimball, os dois ou nenhum?

#datawarehouse #modelagemdedados #engenhariadedados

## Notas para o Felipe

- O primeiro parágrafo cita datas: só publicar depois de conferir `inmon1992` e
  `kimball1996` na fonte. Se quiser publicar antes, tirar as datas e começar pelo
  segundo parágrafo.
- Imagem: as figuras `dw-inmon` e `dw-kimball` lado a lado (são do livro, em cinza).
  Legenda: "elaborado pelo autor com base em Inmon (2005) e Kimball e Ross (2013)".
- O item 1 prepara o post de retorno da enquete do SQL (exemplo do frete).
