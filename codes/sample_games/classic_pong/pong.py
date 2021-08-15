# classic pong using python + pygame

# classic pong using python + pygame

import pygame

# initialize pygame
pygame.init()

# define colors
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# create the screen
screen = pygame.display.set_mode((800, 600))

# paddle 1
paddle_1 = pygame.Surface((20, 100))
paddle_1.fill(RED)
paddle_1_rect = paddle_1.get_rect()

paddle_1_start_x = paddle_1.get_size()[0]
paddle_1_start_y = screen.get_size()[1]/2 - paddle_1.get_size()[1]/2
paddle_1_rect.update((paddle_1_start_x, paddle_1_start_y), paddle_1.get_size())

# paddle 2
paddle_2 = pygame.Surface((20, 100))
paddle_2.fill(RED)
paddle_2_rect = paddle_2.get_rect()

paddle_2_start_x = screen.get_size()[0] - (2*paddle_2.get_size()[0])
paddle_2_start_y = screen.get_size()[1]/2 - paddle_2.get_size()[1]/2
paddle_2_rect.update((paddle_2_start_x, paddle_2_start_y), paddle_2.get_size())

# ball
ball_radius = 10
ball_y = screen.get_size()[1]/2
ball_x = 30 + paddle_1.get_size()[0] + ball_radius*2
ball = pygame.Surface((20, 20))
pygame.draw.circle(ball, WHITE,(ball.get_size()[0]/2,ball.get_size()[1]/2 ), ball_radius)
ball_rect = ball.get_rect()
ball_rect.top =screen.get_size()[1]/2
ball_rect.left = 2 * paddle_1.get_size()[0] + ball_radius*2

# center separator
mid = screen.get_size()[1]/2 - (paddle_1.get_size()[1]/2)
mid_line = pygame.Surface((2, screen.get_size()[1]))
mid_line.fill(RED)

direction_1 = 1
direction_2 = 1
anti_friction = 3  # the higher the faster
fps_clock = pygame.time.Clock()

# title
title_font = pygame.font.SysFont("calibri", 20)
title = title_font.render("*** PONG ***",1, WHITE)

score_1 =0
score_2 = 0
exit = 0
while True:
    fps_clock.tick(100)
    pygame.key.set_repeat(1)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  
                if paddle_1_rect.top> 0:
                    paddle_1_rect = paddle_1_rect.move(0,-1)
            if event.key == pygame.K_s:
                if paddle_1_rect.bottom <=screen.get_size()[1]:
                    paddle_1_rect = paddle_1_rect.move(0,1)
            if event.key == pygame.K_UP:
                if paddle_2_rect.top >= 0:
                    paddle_2_rect = paddle_2_rect.move(0,-1)
            if event.key == pygame.K_DOWN:
                if paddle_2_rect.bottom <=screen.get_size()[1]:
                    paddle_2_rect = paddle_2_rect.move(0,1)
        if event.type == pygame.QUIT:
            exit = 1


    # bouncing ball
    if ball_rect.right > screen.get_size()[0]:
        score_1 +=1
        direction_1 = -1
    if ball_rect.left < 0 :
        score_2 +=1
        direction_1 = 1

    if ball_rect.bottom > screen.get_size()[1]:
        direction_2 = -1
    if ball_rect.top <0:
        
        direction_2 = 1

    if ball_rect.colliderect(paddle_1_rect):
        direction_1 = 1;
    if ball_rect.colliderect(paddle_2_rect):
        direction_1 = -1;
    #print(score_1, score_2)
    dir_x = 1 * direction_1 * anti_friction
    dir_y = 1 * direction_2 * anti_friction
    ball_rect = ball_rect.move((dir_x, dir_y))

    score_a = title_font.render(str(score_1),1, WHITE)
    score_b = title_font.render(str(score_2),1, WHITE)
   
    if exit == 0:
        screen.fill((0,0,0))
        screen.blit(paddle_1, paddle_1_rect)
        screen.blit(paddle_2, paddle_2_rect)  
        screen.blit(ball, ball_rect)
        screen.blit(mid_line,(screen.get_size()[0]/2,0))
        screen.blit(title, (5,5))
        screen.blit(score_a, (5,screen.get_size()[1] - 25))
        screen.blit(score_b, (screen.get_size()[0]-40,screen.get_size()[1] - 25))
        pygame.display.flip()
    else:
        break
 
pygame.quit()


