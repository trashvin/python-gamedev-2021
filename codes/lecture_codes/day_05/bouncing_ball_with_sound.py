# clone the bouncing text and replace it with a ball image
import pygame

pygame.init()
pygame.font.init()

# define colors
BLACK = (0,0,0)
PINK = (255,105,180)
BLUE=(100,149,237)

"""
create a function to play sound
"""

screen = pygame.display.set_mode((800,600))

title_font = pygame.font.SysFont("calibri", 20)
title = title_font.render("**** BOUNCING BALL ****",1,BLUE)

"""
load the ball image and set size to 100,100
"""

text_rect = image.get_rect()
text_rect = text_rect.move((100,100))

"""
instantiate the sound bounce.wav
"""

direction_x = 1
direction_y = 1
ball_speed = 2

fps_clock = pygame.time.Clock()

done = False
while not done:
    fps_clock.tick(100)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True

    if text_rect.left < 0:
        direction_x = 1
        """
        play a sound when the ball bounce
        """
        
    
    if text_rect.right > screen.get_size()[0]:
        direction_x = -1
        """
        play a sound when the ball bounce
        """

    if text_rect.top < 0:
        direction_y = 1
        """
        play a sound when the ball bounce
        """

    if text_rect.bottom > screen.get_size()[1]:
        direction_y = -1
        """
        play a sound when the ball bounce
        """
    
    text_rect = text_rect.move((direction_x * ball_speed   , direction_y * ball_speed))

    screen.fill(BLACK)
    """
    blit the ball image
    """
    screen.blit(title, (5,5))
    pygame.display.flip()

pygame.quit()

