import pygame
from pygame.locals import *
import Randon

pygame.init()
tela = pygame.display.set_mode((1000,720))
pygame.display.set_caption('Randonmizador de Cores')
fps = pygame.time.Clock()
icone = pygame.display.set_icon(pygame.image.load("C:\\Users\\AniZ\\Desktop\\JOKENPO\\alou.png"))

Branco = (255, 255, 255)
Azul = (0, 0, 255)
Vermelho = (255, 0, 0)
Verde = (0, 255, 0)
Amarelo = (255, 255, 0)
Magenta = (255, 0, 255)
Ciano = (0, 255, 255)
Preto = (0, 0, 0)

cores = [ Branco, Azul, Vermelho, Verde, Amarelo, Magenta, Preto, Ciano]

contador = 0

while 1:
    fps.tick(27)
    contador += 1
    for eventos in pygame.event.get():
        pygame.display.update()
        if eventos.type == pygame.QUIT:
            quit()
    Randon.limite_cor(tela, contador)
    if contador > 216:
        contador = 0

    pygame.display.update()