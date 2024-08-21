import pygame
import shooter_game

pygame.init()

window = pygame.display.set_mode((800, 600))

bg = pygame.transform.scale(pygame.image.load('galaxy.jpg'), (800, 600))

fps = pygame.time.Clock()

buttom = pygame.Rect((25, 450, 200, 50))
buttom_exit = pygame.Rect((25, 525, 200, 50))

running = True

pygame.font.init()
bed = pygame.font.SysFont('Arial', 35).render('Начать игру', True, (255, 255, 255))
bed_exit = pygame.font.SysFont('Arial', 35).render('Выход', True, (255, 255, 255))

while running:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if buttom.collidepoint(event.pos):
                shooter_game.game()
                pygame.quit()

            elif buttom_exit.collidepoint(event.pos):
                running = False
                pygame.quit()

    pygame.draw.rect(window, (100, 123, 213), buttom)
    pygame.draw.rect(window, (100, 123, 213), buttom_exit)
    
    window.blit(bed, (25,450))
    window.blit(bed_exit, (25,525))

    pygame.display.update()
    fps.tick(60)