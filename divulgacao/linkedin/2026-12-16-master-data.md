# Master data puxado por um projeto de negócio

- Data: 2026-12-16 (qua)
- Pilar: ideia
- Origem: cap. *Master data: de projeto eterno a oportunidade* (`capitulos/14-master-data.tex`, `sec:master-data-puxado`, figura `master-data-abordagens`)
- Formato: texto, com imagem
- Status: rascunho
- Link:

## Texto

Muita empresa prefere conviver com a planilha de "de-para" a começar um programa de master data. E, olhando a conta antiga, era uma escolha racional.

O caminho tradicional era um programa grande, separado de qualquer entrega: mapear todas as fontes de todos os domínios, conciliar registro por registro, definir a governança, e só então mostrar alguma coisa. Meses, às vezes anos. E o resultado era difícil de exibir: "dados mais consistentes" não aparece numa reunião de diretoria.

Enquanto isso, o custo da planilha ficava espalhado. Retrabalho a cada fechamento, cada área com a sua versão, a primeira meia hora da reunião gasta discutindo qual número está certo. Ninguém via esse custo numa linha do orçamento, então ele nunca competia com o custo visível do programa.

A abordagem que tem funcionado melhor na minha experiência inverte a lógica. Em vez de abrir um programa de master data e procurar quem vai usá-lo, comece por um projeto de negócio que já foi aprovado e veja que partes dele dependem de master data.

Um exemplo: um projeto comercial precisa juntar a carteira de clientes de três sistemas para acompanhar cada vendedor. Sem cadastro mestre de clientes, ele não fica de pé. É a hora de abrir, em paralelo, um projeto de master data só para o domínio de clientes.
• A necessidade está justificada: sem ele, o projeto de negócio não entrega.
• O recurso está garantido: faz parte do projeto aprovado.
• O escopo é pequeno: um domínio só.

O projeto de negócio vira o primeiro cliente e valida na prática: se os vendedores reconhecem as próprias carteiras no painel, a conciliação funcionou. Quando o próximo projeto precisar de clientes, o domínio já está pronto, e ele puxa só o que falta, digamos, produtos.

A IA ajudou a tornar isso viável no prazo de um projeto. Ela sugere pares prováveis, padroniza nomes e explica por que dois cadastros parecem ser o mesmo. A pessoa continua decidindo.

Dois cuidados: não deixar o prazo do projeto atropelar a qualidade do domínio, e desenhá-lo pensando em quem vai usar depois, como o financeiro e a logística.

Como o seu time lida com master data hoje?

#masterdata #governancadedados #dados

## Notas para o Felipe

- "Na minha experiência" vem do próprio capítulo (`sec:master-data-puxado`). Se quiser
  reforçar, cabe uma frase sua no lugar do exemplo genérico, mas o post funciona sem
  relato.
- Imagem: a figura `master-data-abordagens` (programa único contra um domínio por vez).
- Não citar Fellegi e Sunter aqui; fica para um post próprio depois de conferir
  `fellegi1969`.
