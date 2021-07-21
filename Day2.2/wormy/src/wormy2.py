import random, pygame, sys
from pygame.locals import *

FPS = 10 #FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window width must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

# Define Colors
# Name      = (  R,   G,   B)
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
DARKGREEN   = (  0, 155,   0)
DARKGRAY    = ( 40,  40,  40)
BLUE        = (  0,   0, 255)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


HEAD = 0 # The index of the worm's head

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    #BASICFONT = pygame.font.FONT('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    # Spawn at a random starting point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    direction = RIGHT
    wormCoords = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]

    apple = getRandomLocation()

    # Game loop (while)
    while True:
        # Event Handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # Detect "collisions"
        # check to see if the worm has hit itself or the wall
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == CELLHEIGHT: # highlight text & control z for text wrap
            return
        for wormSegment in wormCoords[3:]:
            if wormSegment['x'] == wormCoords[HEAD]['x'] and wormSegment['y'] == wormCoords[HEAD]['y']:
                return
        
        # check to see if the worm has eaten the apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()
        else:
            del wormCoords[-1]

        # move the worm
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}

        wormCoords.insert(0, newHead)

        # LAST THING WE DO
        # Paint on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords) # coords defined later
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomLocation():
    return {'x': random.randint(3, CELLWIDTH - 3), 'y': random.randint(3, CELLHEIGHT - 3)}

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def drawWorm(wormCoords):
    for segment in wormCoords:
        x = segment['x'] * CELLSIZE
        y = segment['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, BLUE, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x+4, y+4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)

def drawApple(apple):
    x = apple['x'] * CELLSIZE
    y = apple['y'] * CELLSIZE
    appleSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleSegmentRect)

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def terminate():
    pygame.quit()
    sys.exit()

def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2, 10)
    overRect.midtop = (WINDOWWIDTH/2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)

    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear the event cache

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return

def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            else:
                return True
    return False

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, BLUE)
    titleSurf2 = titleFont.render('Wormy!', True, RED)
    
    degrees1 = 0
    degrees2 = 0
    while(True): #looks like a game loop
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get() #clear the event cache
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

if __name__ == '__main__':
    main()
