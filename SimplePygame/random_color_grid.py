import pygame
from random import randint
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()
side_length = 50
frame_rate = 5
bg_color = Color('black')

loop = True

def draw_grid():
    def rc():
        return randint(0, 255)

    for x in range(0, screen.get_width(), spacing):
        for y in range(0, screen.get_height(), spacing):
            pygame.draw.rect(screen, Color(rc(), rc(), rc()),
                             Rect(x + margin, y + margin + 20, side_length, side_length))

def draw_info_text():
    font_surface = font.render('Size: %d; FPS: Desired: %d, Avg. Actual: %.2f; Time Used (ms): %d' % (
        side_length, frame_rate, clock.get_fps(), clock.get_rawtime()), True, Color('white'), bg_color)
    screen.blit(font_surface, (margin, 5))

def process_input():
    global loop, side_length, frame_rate

    event = pygame.event.poll()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        loop = False

    changed = False
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    shift = mods & KMOD_SHIFT

    if keys[K_UP]:
        side_length += 10 if shift else 1
        changed = True
    elif keys[K_DOWN]:
        side_length -= 10 if shift else 1
        changed = True
    if keys[K_RIGHT]:
        frame_rate += 10 if shift else 1
    elif keys[K_LEFT]:
        frame_rate -= 10 if shift else 1
    if frame_rate < 1:
        frame_rate = 1
    if side_length < 1:
        side_length = 1
    return changed

while loop:
    changed = process_input()

    screen.fill(bg_color)
    margin = max(side_length / 10, 1)
    spacing = side_length + margin

    draw_grid()
    draw_info_text()
    pygame.display.flip()

    clock.tick(60 if changed else frame_rate)

pygame.quit()
