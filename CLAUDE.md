# Livro de dados, Felipe

**Sempre responda em português brasileiro.** Mapa do repositório e comandos no `README.md`.

## O que é

Livro autoral sobre análise e engenharia de dados: evolução do BI até a era da IA,
trilhas de aprendizado (tradicional contra hoje), por que ainda estudar SQL e Python,
práticas de DevOps em dados e o modelo de Scrum com Kanban que o Felipe aplicou em
projetos de visualização e de engenharia. É um livro para impressão, não tese nem
livro de regras. Planejamento em `notas/`.

## O texto é do Felipe

- O livro é escrito na voz do Felipe. Em 2026-11-19 ele pediu que o Claude escreva o
  texto dos capítulos a partir das notas do autor, pesquisando e trazendo referências; o
  Felipe revisa e ajusta. Ao escrever uma seção, a nota `\rascunho{}` dela sai e o texto
  entra no lugar.
- Relatos de projetos (`relato`) vêm da experiência dele. Nunca invente um relato,
  um número de projeto ou uma situação vivida: no lugar do relato fica um `\rascunho{}`
  dizendo que história caberia ali.
- Os outros repositórios do Felipe servem só de contexto (domínios, ferramentas, tipo de
  trabalho). Nada deles entra no livro como fato sobre ele, nem nome de empresa, cliente,
  sistema interno ou número.
- Voz: explicações em tom direto, falando com o leitor (você); opiniões do autor em
  primeira pessoa, com moderação.
- Relatos não nomeiam empresas, clientes, colegas nem sistemas internos, e números de
  operação aparecem só em ordem de grandeza.
- Nunca invente referência. Entrada nova no `referencias.bib` leva `note = {CONFERIR}`
  até o Felipe checar na fonte. Fato histórico ou dado sem fonte conferida vira
  `\pendente{conferir ...}`.

## Rigor de pesquisa (o livro não é acadêmico, mas tem fontes)

- O Felipe tem experiência com pesquisa e quer que isso apareça: conceito, definição,
  data histórica e número citado levam referência (`\textcite`/`\parencite`, autor-data).
- Datas históricas citam a primeira edição (ex.: `inmon1992`, `kimball1996`); conceitos
  citam a edição lida (ex.: `inmon2005`, `kimball2013`).
- Figuras e tabelas têm `\fonte{...}`: "elaborado pelo autor com base em ..." ou
  "elaborado pelo autor".
- Capítulos com base bibliográfica terminam com `leituras` ("Para ir além"), de 3 a 6
  obras comentadas em uma ou duas frases.
- A bibliografia mostra as páginas em que cada obra é citada (backref). As notas
  `CONFERIR` só aparecem no rascunho; o `compilar.py` conta quantas faltam.
- Diagramas em TikZ em `figuras/`, com os estilos do `livro.sty`, em tons de cinza.
  Nunca número fixo de figura ou tabela no texto nem em comentário de código: `\ref`.

## Regras de escrita

- Sem travessão (—) nem `---` em texto novo. Use vírgula, dois pontos, parênteses ou
  frases separadas; em títulos, um único separador.
- Evitar sinais de texto de IA: "não é apenas X, é Y", listas de três adjetivos só para
  soar completas, frases de efeito no fim de seção. Frases curtas e diretas.
- Seções não são numeradas. Para remeter a uma seção use `\veja{sec:...}`; para capítulo,
  `capítulo~\ref{cap:...}`. Nunca número fixo no texto.
- Todo capítulo e seção tem `\label` (`cap:`, `sec:`, `tab:`, `fig:`).
- Tabelas com `booktabs`, sem linhas verticais.
- Use as caixas já definidas (`relato`, `destaque`, `dica`, `\antesdepois`) em vez de
  criar estilos novos.

## Estilo visual

- Tudo visual fica em `estilo/livro.sty`. Antes de mudar algo global (fonte, margens,
  formato, caixas, cores), teste em `estilo/amostra.tex` (`python compilar.py amostra`),
  renderize a página e só aplique depois que o Felipe aprovar.
- Miolo em cinza para impressão P&B; nada cobre a página inteira; fundos bem claros.
- A identidade visual da YMX não se aplica: o livro é projeto pessoal.

## Processo

- Depois de editar, recompilar (`python compilar.py`, modo rascunho) e conferir que não
  há erro nem referência indefinida. Informar o número de páginas.
- Antes de uma versão para impressão, `python compilar.py --modo todos` e
  `pendentes=0` no modo final.
- Commits só quando o Felipe pedir, sem atribuição ao Claude. Mensagem começa pela área:
  `capitulos: ...`, `estilo: ...`, `notas: ...`, `infra: ...`.
