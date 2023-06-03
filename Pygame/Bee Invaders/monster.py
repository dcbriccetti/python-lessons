import pygame
from util import loadImage
from monster_dropping import MonsterDropping
from random import randint

class Monster(pygame.sprite.Sprite):

    def __init__(self, screen_rect, drawing_group):
        pygame.sprite.Sprite.__init__(self)
        self.screen_rect = screen_rect
        self.drawing_group = drawing_group
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
        elif randint(1, 100) == 1:
            dropping = MonsterDropping(
                self.x + imgRect.width / 2 - 15,
                self.y + imgRect.height * 3 / 4, self.pixels_per_movement)
            self.drawing_group.add(dropping)
