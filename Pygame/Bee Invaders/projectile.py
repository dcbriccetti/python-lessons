from pygame.sprite import Sprite
from util import loadImage

class Projectile(Sprite):

    def __init__(self, x, y):
        super().__init__()
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
