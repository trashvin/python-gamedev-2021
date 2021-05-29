# classic pong using python + pygame

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))
square = pygame.Surface((20, 20))
square.fill((255, 0, 0))
while True:
    screen.blit(square, (100, 100))
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()
 
pygame.quit()


