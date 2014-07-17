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

auto_bees = pygame.sprite.Group()

player_bee = Bee(screen_rect)
player_bee.rect = player_bee.rect.move((50, 50))
auto_bee = Bee(screen_rect)
auto_bees.add(auto_bee)
imgRect = player_bee.image.get_rect()
player_bee.rect = imgRect.move(50, screen_rect.centery - imgRect.centery)

drawing_group = pygame.sprite.RenderUpdates()
drawing_group.add(player_bee, auto_bee)

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

    player_bee.setAngle(angles[ydir+1][xdir+1])
    player_bee.rect = player_bee.rect.move((xdir * 8, ydir * 8)).clamp(screen_rect)

    # Detect collisions
    for bee in pygame.sprite.spritecollide(player_bee, auto_bees, True):
        bee.kill()

    drawing_group.clear(screen, background)
    drawing_group.update()
    changed_rects = drawing_group.draw(screen)
    pygame.display.update(changed_rects)

    # maintain frame rate
    clock.tick(40)

pygame.quit()
