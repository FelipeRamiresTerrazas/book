"""Compila o livro nas tres versoes.

O modo sai do nome do PDF (-jobname), como define estilo/livro.sty:
    <base>_RASCUNHO.pdf  com notas do autor e marcas de pendente (para escrever)
    <base>.pdf           limpo, no tamanho final 16 x 23 cm (para a grafica por demanda)
    <base>_GRAFICA.pdf   limpo, em folha A4 com marcas de corte (offset ou prova em casa)
Os PDFs e os auxiliares do LaTeX saem em output/.

Uso (na raiz do repo):
    python compilar.py                  # rascunho (o modo do dia a dia)
    python compilar.py --modo final
    python compilar.py --modo todos     # rascunho, final e grafica
    python compilar.py amostra          # pagina de teste do estilo (estilo/amostra.tex)
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
SAIDA = "output"
BASE = "Livro_Felipe_Terrazas"
DOCS = {"livro": ("main.tex", BASE), "amostra": ("estilo/amostra.tex", "Amostra_Estilo")}
SUFIXO = {"rascunho": "_RASCUNHO", "final": "", "grafica": "_GRAFICA"}


def compilar(doc, modo):
    principal, base = DOCS[doc]
    job = base + SUFIXO[modo]
    r = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", f"-outdir={SAIDA}",
                        f"-jobname={job}", principal],
                       cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
    arq_log = RAIZ / SAIDA / f"{job}.log"
    log = arq_log.read_text(encoding="utf-8", errors="replace") if arq_log.exists() else ""
    paginas = re.search(r"Output written on .*?\((\d+) pages?", log, flags=re.S)
    indef = len(re.findall(r"(?:Reference|Citation) .*? undefined", log))
    pendentes = len(re.findall(r"Package livro Warning: Pendente", log))
    erros = re.findall(r"^! .*", log, flags=re.M)
    status = "ok" if r.returncode == 0 and not erros else "ERRO"
    bib = (RAIZ / "referencias.bib").read_text(encoding="utf-8")
    conferir = len(re.findall(r"note\s*=\s*\{CONFERIR\}", bib))
    print(f"{status:4s} {SAIDA}/{job}.pdf  páginas={paginas.group(1) if paginas else '?'}  "
          f"pendentes={pendentes}  referências indefinidas={indef}  bib a conferir={conferir}")
    for e in erros[:5]:
        print("     ", e)
    return status == "ok"


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # acentos no terminal do Windows
    ap =argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("doc", nargs="?", default="livro", choices=list(DOCS))
    ap.add_argument("--modo", default="rascunho", choices=[*SUFIXO, "todos"])
    a = ap.parse_args()
    modos = list(SUFIXO) if a.modo == "todos" else [a.modo]
    ok = all([compilar(a.doc, m) for m in modos])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
