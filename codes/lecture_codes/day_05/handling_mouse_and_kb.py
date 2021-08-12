# clone the bouncing text and replace it with a ball image
import pygame

pygame.init()
pygame.font.init()

# define colors
BLACK = (0,0,0)
PINK = (255,105,180)
BLUE=(100,149,237)

def play_bounce_sound():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(bounce_sound)

screen = pygame.display.set_mode((800,600))
"""
hide the mouse pointer
"""

title_font = pygame.font.SysFont("calibri", 20)
title = title_font.render("**** CONTROLLING BALL WITH MOUSE AND KB****",1,BLUE)

image = pygame.image.load(".\\codes\\assets\\images\\beach_ball.png")
image = pygame.transform.scale(image,(100,100))

text_rect = image.get_rect()
text_rect = text_rect.move((100,100))

bounce_sound = pygame.mixer.Sound(".\\codes\\assets\\sounds\\bubble.wav")

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
        """
        add kb event to handle UP and DOWN key
        """

    """
    get mouse position
    """
    
    """
    set the text_rect center = mouse position
    """

    if text_rect.left  < 0:
        play_bounce_sound()
        
    if text_rect.right > screen.get_size()[0]:
        play_bounce_sound()

    if text_rect.top < 0:
        play_bounce_sound()

    if text_rect.bottom > screen.get_size()[1]:
        play_bounce_sound()
    

    screen.fill(BLACK)
    screen.blit(image, text_rect)
    screen.blit(title, (5,5))
    pygame.display.flip()

pygame.quit()

