'''
Demonstration of jumping.
Dave Briccetti, Young Programmers Podcast: http://young-programmers.blogspot.com/
'''

import pygame
from pygame.locals import *

MAN_SCREEN_MARGIN = 5       # pixels
JUMPING_DURATION = 500      # milliseconds
HORZ_MOVE_INCREMENT = 4     # pixels
TIME_AT_PEAK = JUMPING_DURATION / 2
JUMP_HEIGHT = 200           # pixels

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 300), 0)
pygame.display.set_caption('Jumping Man')
#man = pygame.image.load('red-man.png').convert_alpha()

def floorY():
    ''' The Y coordinate of the floor, where the man is placed '''
    return 0#screen.get_height() - man.get_height() - MAN_SCREEN_MARGIN

def jumpHeightAtTime(elapsedTime):
    ''' The height of the jump at the given elapsed time (milliseconds) '''
    return 0#((-1.0/TIME_AT_PEAK**2)* \
        #((elapsedTime-TIME_AT_PEAK)**2)+1)*JUMP_HEIGHT

#manX = screen.get_width() / 2
manY = floorY()
jumping = False
jumpingHorz = 0

loop = False
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    keys = pygame.key.get_pressed()

    def horzMoveAmt():
        ''' Amount of horizontal movement based on left/right arrow keys '''
        return (keys[K_RIGHT] - keys[K_LEFT]) * HORZ_MOVE_INCREMENT

    if not jumping:
        manX += horzMoveAmt()
        if keys[K_SPACE]:
            jumping = True
            jumpingHorz = horzMoveAmt()
            jumpingStart = pygame.time.get_ticks()

    if jumping:
        t = pygame.time.get_ticks() - jumpingStart
        if t > JUMPING_DURATION:
            jumping = False
            jumpHeight = 0
        else:
            jumpHeight = jumpHeightAtTime(t)

        manY = floorY() - jumpHeight
        manX += jumpingHorz

    screen.fill((180,120,120))
    screen.blit(man, (manX, manY))
    pygame.display.flip()
    clock.tick(50)
