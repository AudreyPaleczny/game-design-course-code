import pygame, sys
from pygame.locals import *

pygame.init()

# group work

FPS = 30
fpsClock = pygame.time.Clock()
xCenter = 400
yCenter = 300
radius = 50
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
yVelocity = -10
xVelocity = -4

RESOLUTION = (WINDOWWIDTH, WINDOWHEIGHT)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
direction = "up"
SPEED = 5 # pixels per frame

DISPLAYSURF.fill(WHITE)
#pygame.draw.circle(DISPLAYSURF, BLUE, (400, 300), 50, 100) #(surface, color, center, radius, thickness)


while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (xCenter, yCenter), radius, 100) #(surface, color, center, radius, thickness)


    # Fill in drawing and animating here
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
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)