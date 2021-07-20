import pygame, sys
from pygame.locals import *

pygame.init()

# Color         = (  R,   G,   B)
BLACK           = (  0,   0,   0)
WHITE           = (255, 255, 255)
RED             = (255,   0,   0)
GREEN           = (  0, 255,   0)
BLUE            = (  0,   0, 255)
PURPLE          = (128,   0, 128)
BGCOLOR         = WHITE

FPS = 30
fpsClock = pygame.time.Clock()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

direction = "right"
SPEED = 5 # pixels per frame

while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (400, 300), 50, 100) #(surface, color, center, radius, thickness)


    # Fill in drawing and animating here
    if direction == "right":
        #beardManRect.left += 5
        #if beardManRect.right >= 790:
            direction = "down"
    elif direction == "down":
        #beardManRect.top += 5
        #if beardManRect.bottom >= 590:
            direction = "left"
            #currentBeardMan = beardManImgLeft
    elif direction == "left":
        #beardManRect.left -= 5
        #if beardManRect.left <= 10:
            direction = "up"
    elif direction == "up":
        #beardManRect.top -= 5
        #if beardManRect.top <= 10:
            direction = "right"
            #currentBeardMan = beardManImgRight

    #DISPLAYSURF.blit(currentBeardMan, beardManRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exist()

    pygame.display.update()
    fpsClock.tick(FPS)