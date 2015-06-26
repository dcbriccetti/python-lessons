import pygame
from pygame.locals import *
from time import sleep

sqlen = 50

class Board(object):
    def __init__(self):
        self.squares = [[None for r in range(8)] for c in range(8)]
        for c in range(8):
            self.squares[1][c] = Pawn(0)
            self.squares[6][c] = Pawn(1)
        
    def draw(self, screen):
        self._drawBackground(screen)
        
        for r in range(8):
            for c in range(8):
                square = self.squares[r][c]
                if square:
                    square.draw(screen, r, c)
                    
        pygame.display.flip()
        
    def _drawBackground(self, screen):
        gray = 80, 80, 80
        white = 240, 240, 240
        for r in range(8):
            for c in range(8):
                screen.fill(gray if (r + c) % 2 else white,
                    Rect(r * sqlen, c * sqlen, sqlen, sqlen))

class Chessman(object):
    def __init__(self, color):
        self.color = color
        
    def draw(self, screen, row, col):
        self._blitCentered(self.images[self.color], sqlen * col, sqlen * row)
        
    def _blitCentered(self, surface, x, y):
        rect = surface.get_rect()
        screen.blit(surface, (x + (sqlen - rect.width) / 2,
            y + (sqlen - rect.height) / 2))
    
class Pawn(Chessman):
    images = [pygame.image.load(n) for n in ("whitepawn.png", "blackpawn.png")]
        
pygame.init()
board_len = sqlen * 8
screen = pygame.display.set_mode((board_len, board_len), 0)
pygame.display.set_caption("Chess?")
board = Board()
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False
    board.draw(screen)
    sleep(.1)
pygame.quit()
