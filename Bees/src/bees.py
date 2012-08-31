import pygame, random
from pygame.locals import *
from util import loadImage
from bee import Bee
from flower import Flower
from score import Score

def main():
    pygame.init()
    title = 'Bee, Get the Nectar!'
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screenRect = screen.get_rect()
    Bee.loadImages()
    Flower.loadImages()
    background = loadImage('clover-large.jpg')
    drawTitle = True
    if drawTitle:
        font = pygame.font.Font(None, 48)
        text = font.render(title, 1, Color('white'))
        textpos = text.get_rect(centerx=screenRect.width/2, centery=25)
        background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    bee = Bee(screenRect)
    flowers = pygame.sprite.Group()
    score = Score()

    drawingGroup = pygame.sprite.RenderUpdates()
    drawingGroup.add(bee)
    drawingGroup.add(score)

    pygame.display.set_caption(title)
    pygame.mouse.set_visible(0)

    clock = pygame.time.Clock()
    angles = ((45, 90, 135), (0, 0, 180), (315, 270, 225))

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
        
        bee.setAngle(angles[xdir+1][ydir+1])
        bee.rect = bee.rect.move((xdir * 8, ydir * 8)).clamp(screenRect)

        # Detect collisions
        for flower in pygame.sprite.spritecollide(bee, flowers, True):
            score.score += 1
            flower.kill()
            
        if random.randint(0, 50) == 0:
            flower = Flower(screenRect)
            drawingGroup.add(flower)
            flowers.add(flower)
            
        drawingGroup.clear(screen, background)
        drawingGroup.update()
        changedRects = drawingGroup.draw(screen)
        pygame.display.update(changedRects)

        # maintain frame rate
        clock.tick(40)
        
    pygame.quit()

if __name__ == '__main__': 
    main()
