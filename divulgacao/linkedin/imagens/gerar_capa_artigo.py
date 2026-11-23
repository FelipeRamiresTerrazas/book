"""Capa larga (1920 x 1080) para artigos da newsletter, nos tons de cinza do livro.

Uso: python gerar_capa_artigo.py pasta_saida nome_arquivo "Título|em linhas" "Rótulo superior"
O '|' no título separa as linhas.
"""
import math
import sys
from PIL import Image, ImageDraw, ImageFont

OUT, NOME, TITULO, ROTULO = sys.argv[1:5]
K = 2  # desenha em dobro e reduz, para suavizar
W, H = 1920 * K, 1080 * K
g = lambda v: (round(v * 255),) * 3
TINTA, CINZA, FIO, FUNDO = g(0.10), g(0.40), g(0.70), g(0.95)
FONTES = "C:/Windows/Fonts/"

img = Image.new("RGB", (W, H), FUNDO)
d = ImageDraw.Draw(img)
s = lambda v: v * K  # coordenadas em pixels finais


def lerp(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


def cubo(cx, cy, a, lw):
    c30 = math.cos(math.radians(30))
    top, lt, rt = (cx, cy - a), (cx - a * c30, cy - a / 2), (cx + a * c30, cy - a / 2)
    ce, lb, rb, bo = (cx, cy), (cx - a * c30, cy + a / 2), (cx + a * c30, cy + a / 2), (cx, cy + a)
    faces = [([top, rt, ce, lt], g(0.86)), ([lt, ce, bo, lb], g(0.62)), ([ce, rt, rb, bo], g(0.38))]
    for pts, cor in faces:
        d.polygon(pts, fill=cor)
        p0, p1, p2, p3 = pts
        for t in (1 / 3, 2 / 3):
            d.line([lerp(p0, p1, t), lerp(p3, p2, t)], fill=FUNDO, width=lw // 2)
            d.line([lerp(p0, p3, t), lerp(p1, p2, t)], fill=FUNDO, width=lw // 2)
    d.line([top, rt, rb, bo, lb, lt, top], fill=TINTA, width=lw, joint="curve")
    d.line([lt, ce, rt], fill=TINTA, width=lw, joint="curve")
    d.line([ce, bo], fill=TINTA, width=lw)


def brilho(cx, cy, r, cor):
    pts = []
    for i in range(160):
        th = 2 * math.pi * i / 160
        x = r * math.copysign(abs(math.cos(th)) ** 3, math.cos(th))
        y = r * math.copysign(abs(math.sin(th)) ** 3, math.sin(th))
        pts.append((cx + x, cy + y))
    d.polygon(pts, fill=cor)


def espacado(txt, x, y, fonte, cor, esp, centro=False):
    total = sum(d.textlength(c, font=fonte) for c in txt) + esp * (len(txt) - 1)
    xx = x - total / 2 if centro else x
    for c in txt:
        d.text((xx, y), c, font=fonte, fill=cor)
        xx += d.textlength(c, font=fonte) + esp


# Ilustração à esquerda
cy = s(500)
cubo(s(340), cy, s(190), s(7))
for x in range(s(560), s(660), s(36)):
    d.line([(x, cy), (x + s(20), cy)], fill=CINZA, width=s(8))
d.polygon([(s(690), cy), (s(656), cy - s(22)), (s(656), cy + s(22))], fill=CINZA)
brilho(s(900), cy, s(200), TINTA)
brilho(s(1075), cy - s(170), s(64), CINZA)
brilho(s(745), cy + s(160), s(44), FIO)

rot = ImageFont.truetype(FONTES + "segoeuib.ttf", s(30))
espacado("ANTES", s(340), cy + s(250), rot, CINZA, s(8), centro=True)
espacado("DEPOIS", s(900), cy + s(250), rot, CINZA, s(8), centro=True)

# Fio vertical e texto à direita
d.line([(s(1210), s(270)), (s(1210), s(810))], fill=FIO, width=s(3))
x0 = s(1280)
pequeno = ImageFont.truetype(FONTES + "segoeuib.ttf", s(26))
espacado(ROTULO.upper(), x0, s(330), pequeno, CINZA, s(5))
titulo = ImageFont.truetype(FONTES + "georgiab.ttf", s(76))
yy = s(390)
for linha in TITULO.split("|"):
    d.text((x0, yy), linha, font=titulo, fill=TINTA)
    yy += s(96)
sub = ImageFont.truetype(FONTES + "georgiai.ttf", s(34))
d.text((x0, yy + s(36)), "Dados antes e depois da IA", font=sub, fill=CINZA)

img.resize((1920, 1080), Image.LANCZOS).save(f"{OUT}/{NOME}.png", optimize=True)
print("ok")
