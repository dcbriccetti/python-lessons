import math
import pygame
from pygame.locals import *
from imageutil import loadImage

def main():
    pygame.init()
    title = 'Invisible Maze'
    screen = pygame.display.set_mode((500, 500), 0)
    screenRect = screen.get_rect()
    pygame.display.flip()

    player = loadImage('player.png')
    playerRect = player.get_rect()
    playerRect.y = screenRect.height - playerRect.height
    obstacles = (ob(100, 400), ob(200, 220), ob(350, 230), ob(450, 100),
        ob(460, 350))
    exitRect = Rect(490, 200, 10, 100)

    pygame.display.set_caption(title)
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()

    # game loop
    loop = True
    hit = False
    playerVisible = True
    while loop:
        # get input
        for event in pygame.event.get():
            if event.type == QUIT \
                or (event.type == KEYDOWN and event.key == K_ESCAPE):
                loop = False

        keystate = pygame.key.get_pressed()
        xdir = keystate[K_RIGHT] - keystate[K_LEFT]
        ydir = keystate[K_DOWN] - keystate[K_UP]
        if xdir or ydir:
            playerVisible = False
        if not hit:
            playerRect = playerRect.move((xdir * 2, ydir * 2)).clamp(screenRect)

        screen.fill((0,0,0))
        screen.fill((0,255,0), exitRect)
        
        for obstacle in obstacles:
            screen.fill(colorFromDistance(playerRect.center, obstacle.center),
                obstacle)
            if playerRect.colliderect(obstacle):
                hit = True
                playerVisible = True
        if playerVisible:
            screen.blit(player, playerRect)
        pygame.display.flip()

        # maintain frame rate
        clock.tick(40)

    pygame.quit()

def ob(x, y):
    return Rect(x, y, 30, 30)

def colorFromDistance(loc1, loc2):
    dx = loc2[0] - loc1[0]
    dy = loc2[1] - loc1[1]
    dist = min(127, math.sqrt(dx * dx + dy * dy))
    return (255-dist*2, 0, 0)

if __name__ == '__main__':
    main()
