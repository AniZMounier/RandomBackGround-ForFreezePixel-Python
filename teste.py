import pygame
from pygame.locals import *

pygame.init()
tela = pygame.display.set_mode((720,480))
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

while 1:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            quit()
    for x in cores:
        tela.fill(x)
        pygame.display.update()
        fps.tick(27)