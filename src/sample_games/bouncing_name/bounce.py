import pygame

# initialize pygame
pygame.init()

# define colors
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# create the screen
screen = pygame.display.set_mode((800, 600))

direction_1 = 1
direction_2 = 1
anti_friction = 7  # the higher the faster
fps_clock = pygame.time.Clock()

# title
title_font = pygame.font.SysFont("calibri", 20)
title = title_font.render("*** BOUNCE ***",1, WHITE)

text_font = pygame.font.SysFont("calibri", 40)
text = text_font.render("Hello, World!",1, RED)
text_rect =  text.get_rect()
user_text = ""
name = ""
while True:
    fps_clock.tick(100)
    screen.blit(title, (5,5))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    if text_rect.left <0:
        direction_1 = 1
    elif text_rect.right>screen.get_rect()[0]:
        direction_1 = -1

    if text_rect.top < 0:
        direction_2 = 1
    elif text_rect.bottom>screen.get_rect()[1]:
        direction_2 = -1

    text_rect = text_rect.move((direction_1, direction_2))
    print(direction_1, direction_2)

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    
    pygame.display.flip()