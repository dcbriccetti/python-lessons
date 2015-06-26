import pygame
from util import loadImages

class Bee(pygame.sprite.Sprite):
    images = []

    @staticmethod
    def loadImages():
        Bee.images = loadImages('bee1.png', 'bee2.png', 'bee3.png')

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagesRotated = Bee.images
        self.image = self.images[0]
        imgRect = self.image.get_rect()
        self.rect = imgRect.move(x, y)
        self.animIdx = 0
        self.update_freq = 5
        self.update_place = 0
        
    def update(self):
        self.update_place += 1
        if self.update_place >= self.update_freq:
            self.animIdx = (self.animIdx + 1) % len(self.images)
            self.image = self.imagesRotated[self.animIdx]
            self.update_place = 0

    def setAngle(self, angle):
        self.imagesRotated = []
        for image in Bee.images:
            self.imagesRotated.append(pygame.transform.rotate(image, angle))