import pygame
from util import loadImage
from random import randint

class Monster(pygame.sprite.Sprite):

    def __init__(self, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.screen_rect = screen_rect
        self.image = loadImage('monster.png')
        self.rect = self.image.get_rect()
        self.x = 10
        self.y = randint(0, screen_rect.centery)
        self.pixels_per_movement = randint(1, 5)

    def update(self):
        imgRect = self.image.get_rect()
        self.x += self.pixels_per_movement
        self.rect = imgRect.move(self.x, self.y)
        if self.x > self.screen_rect.right:
            self.kill()
