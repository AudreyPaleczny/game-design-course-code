import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()
xCenter = 400
yCenter = 300
xCenter2 = 600
yCenter2 = 100
radius = 50
radius2 = 50
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
yVelocity = -10
xVelocity = -4
yVelocity2 = -7
xVelocity2 = -15

RESOLUTION = (WINDOWWIDTH, WINDOWHEIGHT)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
direction = "up"
SPEED = 5 # pixels per frame

DISPLAYSURF.fill(WHITE)
#pygame.draw.circle(DISPLAYSURF, BLUE, (400, 300), 50, 100) #(surface, color, center, radius, thickness)


while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (xCenter, yCenter), radius, 100) #(surface, color, center, radius, thickness)
    pygame.draw.circle(DISPLAYSURF, RED, (xCenter2, yCenter2), radius2, 100) #(surface, color, center, radius, thickness)



    # Fill in drawing and animating here
    # bouncing against the wall
    if direction == "up":
        yCenter += yVelocity
        if yCenter < radius:
            yVelocity = 10
        elif yCenter >= WINDOWHEIGHT - radius:
            yVelocity = -10

        xCenter += xVelocity
        if xCenter < radius:
            xVelocity = 4
        elif xCenter >= WINDOWWIDTH - radius:
            xVelocity = -4

    # second ball
    if direction == "up":
        yCenter2 += yVelocity2
        if yCenter2 < radius:
            yVelocity2 = 7
        elif yCenter2 >= WINDOWHEIGHT - radius2:
            yVelocity2 = -7

        xCenter2 += xVelocity2
        if xCenter2 < radius:
            xVelocity2 = 15
        elif xCenter2 >= WINDOWWIDTH - radius2:
            xVelocity2 = -15

    # if the balls bounce into each other        
    # check for a collision and then create an imaginary wall

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)