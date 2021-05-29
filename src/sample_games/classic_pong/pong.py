# classic pong using python + pygame

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))
square = pygame.Surface((20, 20))
square.fill((255, 0, 0))

x =100
y=100
exit = 0
while True:

    screen.blit(square, (x,y))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10
        if event.type == pygame.QUIT:
            exit = 1

    if exit == 0:
        pygame.display.update()
    else:
        break
 
pygame.quit()


