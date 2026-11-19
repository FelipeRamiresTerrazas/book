# Proposta do livro

## Ideia em uma frase

Um panorama da análise e da engenharia de dados, do BI dos anos 1990 até a era da IA,
escrito por quem trabalha no meio disso e aplica DevOps e ágil no dia a dia.

## Para quem

- Quem está começando ou mudando de área e quer saber o que estudar hoje.
- Analistas e engenheiros que já trabalham e querem organizar o que sabem e trazer
  práticas de engenharia (versionamento, testes, CI/CD) e de fluxo (Scrum com Kanban).
- Gestores de times de dados que precisam entender como o trabalho mudou com a IA.

## O que diferencia

- Visão "antes e depois da IA" vinda da prática, não de previsão.
- Defesa argumentada de estudar linguagens (SQL, Python) mesmo com IA.
- Um modelo ágil concreto, aplicado em visualização e em engenharia, que outro time
  consegue copiar.
- TDD como requisito, não como "nice to have": com IA, escrever testes ficou barato, os
  testes viram a especificação da regra de negócio, validada uma vez com o stakeholder,
  e o time itera sem depender da presença dele ("Testes e qualidade de dados", seção
  "Testes antes do modelo"; reflexos em "Scrum com Kanban" e "Antes e depois da IA").
- Conhecimento de negócio como diferencial: com a parte técnica mais ágil, o excelente
  profissional é o que antecipa necessidades e entrega o que ainda não foi pedido.
  Relatos de agricultura, finanças e logística ("Conhecer o negócio").
- Kimball e Inmon com diagramas e fontes, e o rigor de quem pesquisa: referência para
  conceitos e datas, fonte em figuras, "Para ir além" nos capítulos ("O data warehouse
  e a modelagem dimensional").
- Uma parte inteira sobre modelar e governar o mesmo dado para usos diferentes:
  medalhão contra modelagem tradicional, master data, governança, ciência de dados,
  treino de IA e dados como contexto para IA (Parte III).
- Master data como oportunidade, não como projeto eterno: cada domínio (clientes,
  produtos) puxado por um projeto de negócio já aprovado, em paralelo a ele.
- Governança na era da IA, com o data steward como tutor e revisor do que a IA propõe,
  e um guia para construir a própria aplicação de master data e governança (pouco
  material existe sobre isso).
- Frequência de atualização como decisão de negócio, com métricas de uso dos próprios
  produtos de dados, e a passagem da licença por usuário para o consumo em créditos e
  tokens.
- A estrutura tradicional dos times de dados, como a IA pode reduzi-la e uma previsão
  para o futuro.

## Estrutura atual (ver `main.tex`; números de capítulo mudam, nomes não)

- Abertura: prefácio, como ler este livro
- Parte I, De onde viemos: origens do BI, data warehouse, self-service, nuvem e modern
  data stack, chegada da IA
- Parte II, Trilhas de aprendizado: trilha tradicional, trilha hoje, ainda vale
  programar, fundamentos, conhecer o negócio, mapas por carreira
- Parte III, Modelar e governar dados: arquitetura medalhão, master data, governança,
  aplicação própria de master data e governança, ciência de dados, dados para treinar
  IA, dados como contexto para IA
- Parte IV, Dados com práticas de DevOps: dados como código, testes e TDD, CI/CD, do
  pipeline ao dashboard, frequência de atualização, custo e consumo
- Parte V, Ágil em times de dados: estrutura dos times, ágil de prateleira, Scrum com
  Kanban, projetos de visualização, projetos de engenharia, antes e depois da IA
- Epílogo, glossário, referências, sobre o autor

A estrutura é um ponto de partida: capítulos podem ser juntados, cortados ou trocados
de lugar. Meta inicial de tamanho a definir (livros do gênero ficam entre 200 e 300 páginas).

## Decisões em aberto

- [ ] Título definitivo (`notas/02-titulos.md`)
- [ ] Tamanho alvo por capítulo
- [ ] Incluir exercícios ou roteiros de estudo no fim dos capítulos da Parte II?
- [ ] Capítulo sobre R, ou só Python e SQL?
- [ ] Prefácio de convidado?
