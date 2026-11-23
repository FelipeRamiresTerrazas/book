# O livro escrito como código

- Data: 2026-12-08 (ter)
- Pilar: bastidores
- Origem: `compilar.py`, `README.md`; cap. *Dados como código* (`capitulos/20-dados-como-codigo.tex`)
- Formato: texto, com imagem
- Status: rascunho
- Link:

## Texto

O meu livro tem repositório Git, compilação automatizada e um contador de pendências que precisa chegar a zero antes da impressão.

Pode parecer exagero para um livro. Para mim foi o jeito natural de escrever sobre dados como código praticando o que o livro defende.

Como funciona:
• O texto é LaTeX, um arquivo por capítulo. A ordem dos capítulos fica num arquivo só, então mudar a estrutura é mudar uma linha.
• Tudo é versionado. Cada mudança tem histórico, e dá para voltar a qualquer versão ou comparar duas.
• Um script compila o livro em três versões: o rascunho, com minhas notas e pendências visíveis; a final, em 16 x 23 cm, para a gráfica; e uma em A4 com marcas de corte, para imprimir uma prova em casa.
• Toda afirmação que ainda precisa de fonte vira uma marca de pendência no texto. Toda referência nova entra marcada para conferir na fonte original. O script conta as duas a cada compilação.
• Os diagramas também são código, com um estilo único, então todos têm a mesma cara.

É o mesmo raciocínio que uso com modelos de dados. Se não está versionado, não dá para revisar. Se não tem teste, não dá para confiar. No livro, o teste é o contador.

Os números de hoje: 200 páginas no rascunho, 22 pendências abertas e 105 referências esperando conferência na fonte. Vou atualizando esses números por aqui até a versão final.

Quem mais escreve documentação ou texto longo como código? Que ferramentas você usa?

#dataascode #engenhariadedados #latex

## Notas para o Felipe

- Números tirados de `python compilar.py` em 2026-11-23. Rodar de novo no dia da
  publicação e atualizar.
- Imagem: print do terminal com a linha do `compilar.py`
  (`páginas=... pendentes=... bib a conferir=...`) ao lado de uma página do rascunho com
  as notas aparecendo.
- O repositório é privado? Se for, não prometer link. Se quiser abrir parte dele (o
  `livro.sty`, por exemplo), isso rende outro post.
