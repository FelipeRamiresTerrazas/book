# Testes como especificação da regra de negócio

- Data: 2026-12-10 (qui)
- Pilar: experiência
- Origem: cap. *Testes e qualidade de dados*, seção *Testes antes do modelo* (`capitulos/21-testes-e-qualidade.tex`, `sec:tdd`)
- Formato: texto
- Status: rascunho (depende de relato)
- Link:

## Texto

A parte mais demorada de um modelo de dados quase nunca foi escrever o SQL. Era validar a regra com quem entende do negócio, uma versão de cada vez, dependendo da agenda dessa pessoa.

[RELATO: um projeto em que a validação com o stakeholder travou o modelo. Quantas rodadas, quanto tempo esperando agenda, que regra só apareceu no fim. Duas ou três frases, sem nomes, números em ordem de grandeza.]

O que mudou com a IA é que escrever testes ficou barato. A partir de uma regra descrita em texto, um assistente escreve os testes em segundos e sugere casos de borda que ninguém tinha pensado.

Isso permite inverter a ordem. Antes do modelo, vêm os testes que descrevem as regras:
• toda venda cancelada sai da receita;
• o saldo nunca fica negativo;
• o frete do modelo bate com o frete dos pedidos.

Os testes são validados uma vez com o stakeholder, em perguntas concretas: "se o pedido for cancelado depois de faturado, ele sai da receita do mês do cancelamento ou do mês do faturamento?". Respondida, a pergunta vira teste. Daí em diante, o time itera sem depender da agenda dele, e mudar uma regra passa a ser mudar um teste, combinado antes de qualquer código.

[RELATO: o que aconteceu quando você trabalhou assim. O que mudou no tempo de validação ou na conversa com a área. Se ainda não aplicou do começo ao fim, dizer que é o que está testando agora.]

Um cuidado: teste gerado depois do modelo, a partir do próprio modelo, tende a confirmar o que ele já faz, inclusive os erros. O teste escrito antes, a partir da regra, verifica. O escrito depois só tira uma fotografia.

No livro, defendo que TDD em dados pode deixar de ser diferencial e virar requisito do time. Você escreve os testes antes ou depois do modelo?

#qualidadededados #tdd #analyticsengineering

## Notas para o Felipe

- Não publicar sem os dois `[RELATO]`. São os mesmos relatos previstos nos `\rascunho{}`
  do capítulo de testes: escrevendo uma vez, serve aos dois lugares.
- Se o relato não estiver pronto até 10/12, trocar a data com o post de 05/01
  (frequência), que não depende de relato.
