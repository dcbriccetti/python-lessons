import pygame
from util import loadImage

class MonsterDropping(pygame.sprite.Sprite):

    def __init__(self, x, y, pixels_per_movement):
        pygame.sprite.Sprite.__init__(self)
        self.pixels_per_movement = pixels_per_movement
        self.image = loadImage('monster-dropping.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        imgRect = self.image.get_rect()
        self.y += 5
        self.x += self.pixels_per_movement
        if self.y < 0:
            self.kill()
        self.rect = imgRect.move(self.x, self.y)
