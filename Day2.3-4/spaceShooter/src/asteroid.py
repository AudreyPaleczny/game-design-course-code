import pygame
import numpy as np

class Asteroid:

    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT, speed, startPos = -100):
        self.speed = speed
        self.image = pygame.image.load("ArtAssets7/asteroid.png")
        self.image.convert_alpha() # bg is transparent
        self.rect = self.image.get_rect()
        self.rect.topleft = (np.random.randint(0, WINDOWWIDTH - self.rect.width), startPos) # (x, y) tuple
        self.rotateSpeed = np.random.randint(0, 6)
        self.rotation = 0

    def move(self):
        self.rect.top += self.speed
        self.rotation += self.rotateSpeed

    def draw(self):
        image = pygame.transform.rotate(self.image, self.rotation)
        return image, self.rect