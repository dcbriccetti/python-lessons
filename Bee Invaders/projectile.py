import pygame
from util import loadImage

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage('projectile.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        imgRect = self.image.get_rect()
        self.y -= 5
        if self.y < -imgRect.height / 2:
            self.kill()
        self.rect = imgRect.move(self.x, self.y)
