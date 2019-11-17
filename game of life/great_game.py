import numpy as np
import pygame
import random
APPLE_COL=(255,0,0)
RABBIT_COL=(156,156,156)
BG_COL=(0,150,0)
SCREEN_SIZE=[500,500]
ATOM_SIZE=5
FPS=10

speed=1
stomach=2

#board = np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
board=[]
for x in range(0,SCREEN_SIZE[0],ATOM_SIZE):
    for y in range(0,SCREEN_SIZE[1],ATOM_SIZE):
        board.append([x,y])

def applegen(apple_board,amount,board):
    while amount>0:
        new_apple=random.choice(board)
        if new_apple not in apple_board:
            apple_board.append(new_apple)
            amount-=1
    return apple_board

def rabbitgen(amount,board):
    rabbit_board=[]
    while amount>0:
        new_rabbit=random.choice(board)
        if new_rabbit not in apple_board:
            if new_rabbit not in rabbit_board:
                rabbit_board.append([new_rabbit,speed,stomach])
                amount-=1
    return rabbit_board




apple_board=applegen([],100,board)
rabbit_board=rabbitgen(50,board)
print(rabbit_board)
pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    apple_board=applegen(apple_board,5,board)

    full_board=np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
    for apple in apple_board:
        full_board[int(apple[0]/ATOM_SIZE),int(apple[1]/ATOM_SIZE)]=1
    for rabbit in rabbit_board:
        full_board[int(rabbit[0][0]/ATOM_SIZE),int(rabbit[0][1]/ATOM_SIZE)]=2
    gameDisplay.fill(BG_COL)
    for element in full_board:
        if element==1:
            pygame.draw.rect(gameDisplay, APPLE_COL, (i[0],i[1],ATOM_SIZE,ATOM_SIZE))
        if element==2:
            pygame.draw.rect(gameDisplay, RABBIT_COL, (i[0][0],i[0][1],ATOM_SIZE,ATOM_SIZE))


    print(len(apple_board))
    pygame.display.update()
    clock.tick(FPS)
