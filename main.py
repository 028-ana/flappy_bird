import pygame
from scripts.cenas import Partida, Menu

pygame.init()

tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# cena inicial
cenaAtual = "menu"
cenas = {
    "menu": Menu(tela),
    "partida": Partida(tela)
}

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((86, 148, 214))

    proximaCena = cenas[cenaAtual].atualizar()

    # se trocar de cena
    if proximaCena != cenaAtual:
        cenaAtual = proximaCena

        if cenaAtual == "partida":
            cenas["partida"] = Partida(tela)  # RECRIAR PARTIDA DO ZERO

    pygame.display.flip()
    clock.tick(60)
