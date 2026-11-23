# Frequência de atualização é decisão de negócio

- Data: 2027-01-05 (ter)
- Pilar: ideia
- Origem: cap. *Com que frequência os dados precisam atualizar?* (`capitulos/24-frequencia-de-atualizacao.tex`, figura `frequencia-consumo`)
- Formato: texto, com imagem
- Status: rascunho
- Link:

## Texto

Um painel que atualiza 24 vezes por dia e é aberto duas vezes por semana tem mais de 80 atualizações para cada acesso.

Poucas decisões num projeto de dados são tomadas tão no automático quanto a frequência de atualização. O stakeholder pede "o mais atualizado possível", ninguém pede dado velho, e o pipeline vai para o agendamento de hora em hora porque a ferramenta permite.

A pergunta que costuma ser feita, "com que frequência você quer que atualize?", tem resposta previsível. A pergunta útil é outra: quando e como você decide com esse número?
• Decisão operacional (despachar, repor, bloquear uma transação) pede minutos ou horas.
• Decisão tática (escala da semana, preço de uma linha) convive bem com o dado de ontem.
• Decisão estratégica (metas, orçamento, safra) usa dado fechado, uma vez por mês ou por ano.

E as fontes impõem limite. Se o sistema de origem consolida as vendas uma vez por dia, rodar o pipeline de hora em hora copia o mesmo dado 24 vezes.

A regra que defendo no livro: atualize o mais rápido que as fontes permitem, mas só o quanto a decisão precisa. E meça o uso, porque a primeira definição quase sempre está errada.

Quase toda ferramenta de BI e todo armazém de dados guarda quem acessou o quê e quanto custou cada execução. Com isso dá para listar, por produto de dados, atualizações, acessos e custo por acesso. No topo da lista ficam os candidatos a desligar; logo abaixo, os candidatos a atualizar menos.

Duas práticas simples:
• todo painel mostra a data e a hora da última atualização, e avisa quando a carga falhou;
• uma vez por mês ou por trimestre, revisar os produtos mais caros e os menos acessados.

Baixar a frequência também é entrega: precisa ser combinado com o dono do produto e comunicado a quem usa.

Quantos painéis do seu ambiente atualizam mais do que são abertos?

#dados #finops #analyticsengineering

## Notas para o Felipe

- A conta do primeiro parágrafo: 24 × 7 = 168 atualizações por semana, divididas por 2
  acessos = 84. É exemplo, não relato.
- O capítulo prevê um relato de abertura (pedido de "tempo real" que era uma reunião
  semanal). Se ele já estiver escrito, pode substituir o primeiro parágrafo e deixar o
  post mais forte.
- Imagem: figura `frequencia-consumo` (quadrantes de desperdício e risco).
