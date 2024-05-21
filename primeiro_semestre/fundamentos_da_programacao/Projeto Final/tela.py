from pygame import *

init()
janela = display.set_mode((290, 174))
display.set_caption('The legend of the warrior')

fundo = image.load("download.jpeg").convert_alpha()
fundo = transform.scale(fundo, (290, 174))

loop = True
while loop:
    for events in event.get():
        if events.type == QUIT:
            loop = False
    display.blit(fundo, (0, 0))
    display.update()
