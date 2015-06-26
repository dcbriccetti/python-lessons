import pygame
from pygame.locals import Color

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.color = Color('white')
        self.lastscore = -1
        self.score = 0
        self.update()
        self.rect = self.image.get_rect().move(10, 20)

    def update(self):
        if self.score != self.lastscore:
            self.lastscore = self.score
            msg = "Score: %d" % self.score
            self.image = self.font.render(msg, 0, self.color)

