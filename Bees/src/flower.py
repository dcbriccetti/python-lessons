import random, pygame
from util import loadImage

class Flower(pygame.sprite.Sprite):
    
    @staticmethod
    def loadImages():
        Flower.image = loadImage('flower.png')
        
    def __init__(self, screenRect):
        pygame.sprite.Sprite.__init__(self)
        self.image = Flower.image
        imgRect = self.image.get_rect()
        self.rect = imgRect.move(random.randint(0, screenRect.width), 
            random.randint(0, screenRect.height)).clamp(screenRect)
