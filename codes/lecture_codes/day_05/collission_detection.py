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
# pygame.mouse.set_visible(False)

title_font = pygame.font.SysFont("calibri", 20)
title = title_font.render("**** COLLISSION DETECTION ****",1,BLUE)

"""
create a text for the collision message
"""

ball = pygame.image.load(".\\codes\\assets\\images\\beach_ball.png")
ball = pygame.transform.scale(ball,(100,100))

box = pygame.image.load(".\\codes\\assets\\images\\box.png")
box = pygame.transform.scale(box,(300,300))

ball_rect = ball.get_rect()
ball_rect = ball_rect.move((500,200))

box_rect = box.get_rect()
box_rect = box_rect.move((100,100))

bounce_sound = pygame.mixer.Sound(".\\codes\\assets\\sounds\\bounce.wav")

direction_x = 1
direction_y = 1
ball_speed = 2

fps_clock = pygame.time.Clock()

done = False
while not done:
    fps_clock.tick(100)

    # get mouse
    #mouse_xy = pygame.mouse.get_pos()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("DOWN!")
            if event.key == pygame.K_UP:
                print("UP!")
                

    # get mouse
    mouse_xy = pygame.mouse.get_pos()
    
    ball_rect.center = mouse_xy

    screen.fill(BLACK)

    """
    determine if the object collided. if yes, play a sound and display message
    """
    
    screen.blit(ball, ball_rect)
    screen.blit(box, box_rect)
    screen.blit(title, (5,5))
    pygame.display.flip()

pygame.quit()

