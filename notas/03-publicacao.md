# Publicação e impressão

Lista do que é preciso para a primeira edição impressa. Conferir cada item na fonte
oficial antes de agir; regras e preços mudam.

## Arquivos

- **Miolo**: `output/Livro_Felipe_Terrazas.pdf` (16 x 23 cm, sem marcas). É o que as
  plataformas de impressão sob demanda pedem.
- **Gráfica offset ou prova em casa**: `output/Livro_Felipe_Terrazas_GRAFICA.pdf`
  (A4 com marcas de corte). Confirmar com a gráfica se ela quer marcas e sangria.
- **Capa**: arquivo separado, feito quando o número de páginas estiver fechado, porque
  a largura da lombada depende dele e do papel.

## Registro

- [ ] ISBN (no Brasil, emitido pela Câmara Brasileira do Livro desde 2020; conferir)
- [ ] Ficha catalográfica (CIP), feita por bibliotecário com registro no CRB
- [ ] Preencher `\isbnlivro`, `\cidadelivro` e a ficha em `abertura/folha-de-rosto.tex`

## Revisão

- [ ] Revisão de texto por outra pessoa (preencher o crédito de revisão)
- [ ] `python compilar.py --modo final` com `pendentes=0`
- [ ] Imprimir uma prova em casa (modo gráfica) e ler no papel

## Onde imprimir (pesquisar condições atuais)

- Impressão sob demanda: UICLAP, Clube de Autores, Amazon KDP
- Tiragem pequena em gráfica digital, ou offset para tiragens maiores
