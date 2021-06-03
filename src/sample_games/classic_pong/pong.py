# classic pong using python + pygame

import pygame

pygame.init()

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
screen = pygame.display.set_mode((800, 600))
paddle_1 = pygame.Surface((20, 100))
paddle_1.fill(RED)

paddle_2 = pygame.Surface((20, 100))
paddle_2.fill(RED)

x_1 = 30
y_1= screen.get_size()[1]/2 - (paddle_1.get_size()[1]/2)

x_2 = screen.get_size()[0]-30-paddle_2.get_size()[0]
y_2 = y_1

ball_radius = 10
ball_y = screen.get_size()[1]/2
ball_x = 30 + paddle_1.get_size()[0] + ball_radius*2

mid_line = pygame.Surface((2, screen.get_size()[1]))
mid_line.fill(RED)

direction_1 = 1
direction_2 = 1
friction = 0.1

exit = 0
while True:
    pygame.key.set_repeat(1)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if y_1 >= 0:
                    y_1 -= 1 
            if event.key == pygame.K_s:
                if y_1 <=screen.get_size()[1]-paddle_1.get_size()[1]:
                    y_1 += 1 
            if event.key == pygame.K_UP:
                 if y_2 >= 0:
                    y_2 -= 1
            if event.key == pygame.K_DOWN:
                if y_2 <=screen.get_size()[1]-paddle_2.get_size()[1]:
                    y_2 += 1
        if event.type == pygame.QUIT:
            exit = 1

    # bouncing ball
    if ball_y > screen.get_size()[1]:
        direction_1 = -1
    if ball_y < 0 :
        direction_1 = 1

    if ball_x > screen.get_size()[0]:
        direction_2 = -1
    if ball_x <0:
        direction_2 = 1

    ball_y += 1 * direction_1 * friction
    ball_x += 1 * direction_2 * friction
    
    if exit == 0:
        screen.fill((0,0,0))
        screen.blit(paddle_1, (x_1,y_1))
        screen.blit(paddle_2, (x_2,y_2))
        pygame.draw.circle(screen, WHITE,(ball_x, ball_y), ball_radius)
        screen.blit(mid_line,(screen.get_size()[0]/2,0))
        pygame.display.update()
    else:
        break
 
pygame.quit()


