import pygame

def main():        
    pygame.init()
    tela = pygame.display.set_mode([300,300])
    pygame.display.set_caption("Iniciando com Pygame")    
    cor = (255,255,255) # cor branca
    sair = False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True               

            tela.fill(cor) # preenche a tela com a cor branca    

            pygame.display.update() 

    pygame.quit()

main()

