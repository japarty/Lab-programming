import numpy as np
import pygame
RABBIT_COL=(255,0,0)
BG_COL=(0,150,0)
SCREEN_SIZE=[500,500]
ATOM_SIZE=5
FPS=3
#board = np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
board = np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))


print(board)

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    gameDisplay.fill(BG_COL)
    pygame.display.update()
    clock.tick(FPS)
