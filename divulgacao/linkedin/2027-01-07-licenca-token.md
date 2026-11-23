# Da licença por usuário ao consumo em créditos e tokens

- Data: 2027-01-07 (qui)
- Pilar: ideia
- Origem: cap. *De usuários a tokens: custo e consumo* (`capitulos/25-custo-e-consumo.tex`, tabela `tab:usuario-consumo`)
- Formato: texto
- Status: rascunho
- Link:

## Texto

Durante muito tempo, o custo de uma ferramenta de dados era uma linha fixa no orçamento. Hoje ele acompanha cada consulta, cada atualização e cada pergunta feita à IA.

No modelo por usuário, paga-se uma licença por pessoa. O custo é previsível, negociado na renovação, quase sempre por compras e TI. A alavanca do gerente é o acesso: quem precisa de licença e de qual nível. O que esse modelo não faz é ligar o custo ao uso. Um painel que atualiza de hora em hora custa o mesmo que um que atualiza uma vez por dia. Para o orçamento, a eficiência técnica é invisível.

No modelo por consumo, paga-se pelo que foi processado: horas de computação, dados lidos, atualizações, tokens de entrada e de saída. Começou com os armazéns de dados na nuvem, a IA acelerou, e ferramentas de BI passaram a cobrar por capacidade ou por crédito.

O que muda para quem lidera um time de dados:
• O gerente passa a gerir um orçamento variável, de forma contínua, e não só na renovação.
• O desperdício deixa de ser a licença de quem não usa e passa a ser a atualização ou a consulta que ninguém aproveita.
• Um agente em laço ou uma consulta pesada agendada por engano pode consumir o orçamento do mês em poucos dias.
• O custo pode ser mostrado a quem pede. Quando o stakeholder vê quanto custa atualizar o painel de hora em hora, a conversa sobre frequência muda.

Com IA, três coisas costumam inflar a conta: contexto grande demais em cada pergunta, a mesma pergunta processada dez vezes por dez pessoas, e o modelo mais caro usado para tudo, inclusive para tarefas que um menor faria igualmente bem.

A métrica que proponho no livro é a mesma para painel e para assistente: custo por uso efetivo. Créditos por acesso num caso, tokens por resposta útil no outro.

[RELATO opcional: que indicador de consumo você acompanha hoje e com que frequência, sem números absolutos.]

Como o seu time acompanha o custo de dados e de IA hoje?

#finops #dados #ia

## Notas para o Felipe

- O post não cita fontes. Se quiser mencionar FinOps como disciplina, a referência é
  `storment2023` [CONFERIR].
- O capítulo tem um `\pendente` pedindo exemplos atuais de ferramentas de BI com cobrança
  por crédito. O post fala do movimento sem nomear ferramenta; manter assim.
- O `[RELATO]` é opcional: o post funciona sem ele. Se usar, o "reduziu pela metade o
  custo do armazém" do `sobre-o-autor.tex` é um bom gancho, mas confirme se quer tornar
  isso público.
