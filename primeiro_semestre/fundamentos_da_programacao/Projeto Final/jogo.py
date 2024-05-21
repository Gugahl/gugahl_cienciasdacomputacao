from pygame import *
from pygame.event import get
from pygame.locals import *
import sys

def main():
    init()
    largura = 640
    altura = 480
    x = largura / 2
    y = 0
    tela = display.set_mode((largura, altura))
    display.set_caption('Game')
    relogio = time.Clock()
    sair = False
    while sair != True:
        relogio.tick(60)
        tela.fill((0, 0, 0))
        for event in get():
            if type == QUIT:
                sair = True
        draw.rect(tela, (0, 0, 255), (x, y, 50, 50))
        display.update()
        if y >= altura:
            y = 0
        y += 1 
    quit()
main()
