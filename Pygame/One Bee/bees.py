import pygame
from pygame.locals import *
from bee import Bee

pygame.init()
screen = pygame.display.set_mode((700, 394), 0)
screen_rect = screen.get_rect()
background = screen.copy()
for y in range(screen_rect.height):
    color_val = 255 - 255 * y / screen_rect.height
    pygame.draw.line(background, (0, color_val, 0), (0, y), (screen_rect.width, y))
Bee.loadImages()

screen.blit(background, (0, 0))
pygame.display.flip()

bee = Bee(screen_rect)

drawing_group = pygame.sprite.RenderUpdates()
drawing_group.add(bee)

pygame.display.set_caption('One Bee')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()
angles = (( 45,   0,  -45),
          ( 90,   0,  -90),
          (135, 180, -135))

# game loop
loop = True
while loop:
    # get input
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    keystate = pygame.key.get_pressed()
    xdir = keystate[K_RIGHT] - keystate[K_LEFT]   # -1, 0, or 1
    ydir = keystate[K_DOWN]  - keystate[K_UP]

    bee.setAngle(angles[ydir+1][xdir+1])
    bee.rect = bee.rect.move((xdir * 8, ydir * 8)).clamp(screen_rect)

    drawing_group.clear(screen, background)
    drawing_group.update()
    changed_rects = drawing_group.draw(screen)
    pygame.display.update(changed_rects)

    # maintain frame rate
    clock.tick(40)

pygame.quit()
