def limite_cor (a, x):
    Branco = (255, 255, 255)
    Azul = (0, 0, 255)
    Vermelho = (255, 0, 0)
    Verde = (0, 255, 0)
    Amarelo = (255, 255, 0)
    Magenta = (255, 0, 255)
    Ciano = (0, 255, 255)
    Preto = (0, 0, 0)

    if x <= 27:
        a.fill(Branco)
        x += 1
    if 27 < x <= 54:
        a.fill(Azul)
    if 54 < x <= 81:
        a.fill(Vermelho)
    if 81 < x <= 108:
        a.fill(Verde)
    if 108 < x <= 135:
        a.fill(Amarelo)
    if 135 < x <= 162:
        a.fill(Magenta)
    if 162 < x <= 189:
        a.fill(Ciano)
    if 189 < x <= 216:
        a.fill(Preto)