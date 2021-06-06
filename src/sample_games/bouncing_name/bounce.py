import pygame

# initialize pygame
pygame.init()
pygame.font.init()

# define colors
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,105,180)
BLUE=(100,149,237)

# create the screen
screen = pygame.display.set_mode((800,600))
direction_x = 1
direction_y = 1
anti_friction = 7  # the higher the faster
fps_clock = pygame.time.Clock()

# title
title_font = pygame.font.SysFont("calibri", 20)
title = title_font.render("*** BOUNCE ***",1, WHITE)

text_font = pygame.font.Font(".\\src\\assets\\fonts\\crackman.ttf", 40)
text = text_font.render("Hello, World!",1, PINK)

text_rect =  text.get_rect()
text_rect = text_rect.move((100,100))

while True:
    fps_clock.tick(100)
    

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    if text_rect.left <0:
        direction_x = 1
    if text_rect.right>screen.get_size()[0]:
        direction_x = -1

    if text_rect.top < 0:
        direction_y = 1
    if text_rect.bottom>screen.get_size()[1]:
        direction_y = -1

    text_rect = text_rect.move((direction_x, direction_y))
    #print(direction_x, direction_y)

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    screen.blit(title, (5,5))
    pygame.display.flip()

pygame.quit()