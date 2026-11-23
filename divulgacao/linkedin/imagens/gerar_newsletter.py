"""Imagem da newsletter: cubo (OLAP, antes) -> brilho (IA, depois), tons de cinza do livro."""
import math
import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
S = 2400  # desenha grande e reduz, para suavizar as bordas
g = lambda v: (round(v * 255),) * 3
TINTA, CINZA, FIO, FUNDO = g(0.10), g(0.40), g(0.70), g(0.95)

img = Image.new("RGB", (S, S), FUNDO)
d = ImageDraw.Draw(img)

# Cubo isométrico com grade 3x3 em cada face
cx, cy, a = 700, 900, 340
cos30 = math.cos(math.radians(30))
top = (cx, cy - a)
left_t = (cx - a * cos30, cy - a / 2)
right_t = (cx + a * cos30, cy - a / 2)
center = (cx, cy)
left_b = (cx - a * cos30, cy + a / 2)
right_b = (cx + a * cos30, cy + a / 2)
bottom = (cx, cy + a)

faces = [
    ([top, right_t, center, left_t], g(0.86)),
    ([left_t, center, bottom, left_b], g(0.62)),
    ([center, right_t, right_b, bottom], g(0.38)),
]
for pts, cor in faces:
    d.polygon(pts, fill=cor)

def lerp(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)

def grade(p0, p1, p2, p3, cor, w=6):
    # p0-p1 e p3-p2 são lados opostos; linhas a 1/3 e 2/3 nas duas direções
    for t in (1 / 3, 2 / 3):
        d.line([lerp(p0, p1, t), lerp(p3, p2, t)], fill=cor, width=w)
        d.line([lerp(p0, p3, t), lerp(p1, p2, t)], fill=cor, width=w)

grade(top, right_t, center, left_t, FUNDO)
grade(left_t, center, bottom, left_b, FUNDO)
grade(center, right_t, right_b, bottom, FUNDO)
contorno = [top, right_t, right_b, bottom, left_b, left_t, top]
d.line(contorno, fill=TINTA, width=10, joint="curve")
d.line([left_t, center, right_t], fill=TINTA, width=10, joint="curve")
d.line([center, bottom], fill=TINTA, width=10)

# Seta tracejada
y = cy
x0, x1 = 1110, 1370
for x in range(x0, x1 - 60, 60):
    d.line([(x, y), (x + 34, y)], fill=CINZA, width=12)
d.polygon([(x1, y), (x1 - 60, y - 36), (x1 - 60, y + 36)], fill=CINZA)

# Brilho de quatro pontas (IA)
def brilho(cx, cy, r, cor):
    pts = []
    n = 120
    for i in range(n):
        th = 2 * math.pi * i / n
        # astroide: pontas finas e lados côncavos
        x = r * math.copysign(abs(math.cos(th)) ** 3, math.cos(th))
        y_ = r * math.copysign(abs(math.sin(th)) ** 3, math.sin(th))
        pts.append((cx + x, cy + y_))
    d.polygon(pts, fill=cor)

brilho(1790, 900, 360, TINTA)
brilho(2070, 600, 120, CINZA)
brilho(1560, 1180, 80, FIO)

# Rótulos
fonte_rot = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 92)
for txt, x in (("ANTES", cx), ("DEPOIS", 1790)):
    w = d.textlength(txt, font=fonte_rot)
    # espaçamento entre letras
    esp = 18
    total = w + esp * (len(txt) - 1)
    xx = x - total / 2
    for ch in txt:
        d.text((xx, 1330), ch, font=fonte_rot, fill=CINZA)
        xx += d.textlength(ch, font=fonte_rot) + esp

# Fio separador e título
d.line([(300, 1560), (S - 300, 1560)], fill=FIO, width=6)
fonte_tit = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 200)
for i, linha in enumerate(("Dados antes e", "depois da IA")):
    w = d.textlength(linha, font=fonte_tit)
    d.text(((S - w) / 2, 1640 + i * 250), linha, font=fonte_tit, fill=TINTA)

img.resize((1200, 1200), Image.LANCZOS).save(OUT + "/newsletter.png", optimize=True)
img.resize((300, 300), Image.LANCZOS).save(OUT + "/newsletter-300.png", optimize=True)
print("ok")
