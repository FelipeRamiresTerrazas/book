"""Converte a seção '## Texto' de um rascunho de newsletter em HTML simples para colar no LinkedIn.

Uso: python md_para_html.py entrada.md saida.html
"""
import html
import re
import sys

src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
corpo = re.search(r"## Texto\n\n(.*?)\n## Notas", t, re.S).group(1).strip()

partes = []
lista = []

def fecha_lista():
    if lista:
        partes.append("<ol>\n" + "\n".join(lista) + "\n</ol>")
        lista.clear()

for bloco in corpo.split("\n\n"):
    bloco = bloco.strip()
    m_item = re.match(r"^\d+\.\s+([^.]+\.)\s*(.*)$", bloco, re.S)
    if m_item:
        nome, resto = m_item.groups()
        lista.append(f"<li><strong>{html.escape(nome)}</strong> {html.escape(resto)}</li>")
        continue
    fecha_lista()
    if bloco.startswith("### "):
        partes.append(f"<h2>{html.escape(bloco[4:])}</h2>")
    elif bloco.startswith('"') and bloco.endswith('"'):
        partes.append(f"<blockquote><p>{html.escape(bloco)}</p></blockquote>")
    else:
        linhas = [html.escape(l) for l in bloco.split("\n")]
        partes.append("<p>" + "<br>".join(linhas) + "</p>")
fecha_lista()

conteudo = "\n".join(partes)
pagina = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Newsletter</title>
<style>body{{max-width:700px;margin:40px auto;font:17px/1.6 Georgia,serif;padding:0 16px}}
blockquote{{border-left:3px solid #999;margin-left:0;padding-left:16px;color:#333}}</style>
</head><body>
<!--CONTEUDO-->
{conteudo}
<!--/CONTEUDO-->
</body></html>
"""
open(out, "w", encoding="utf-8").write(pagina)
print(f"ok: {len(partes)} blocos")
