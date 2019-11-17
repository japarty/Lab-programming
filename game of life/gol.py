import numpy as np
import pygame
LIFE_COLOR=(255,0,0)
DEAD_COLOR=(0,0,0)
SCREEN_SIZE=[500,500]
ATOM_SIZE=10
FPS=3
#board = np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
board = np.random.randint(2, size=(int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
board[21,20]=1
board[22,21]=1
board[20,22]=1
board[21,22]=1
board[22,22]=1


def somsiadsum(board):
    sum_board=np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if i==0 and j==0: sum_board[i,j] = board[i,j+1]+board[i+1,j]+board[i+1,j+1]
            elif i==0 and j==board.shape[1]-1: sum_board[i,j] = board[i,j-1]+board[i+1,j-1]+board[i,j]
            elif i==board.shape[1]-1 and j==0: sum_board[i,j] = board[i-1,j]+board[i-1,j+1]+board[i,j+1]
            elif i==board.shape[0]-1 and j==board.shape[1]-1: sum_board[i,j] = board[i-1,j-1]+board[i-1,j]+board[i,j-1]
            elif i==0 and j!=0 and j!=board.shape[1]-1: sum_board[i,j] = board[i,j-1]+board[i,j+1]+board[1,j-1]+board[1,j]+board[1,j+1]
            elif i==board.shape[0]-1 and j!=0 and j!=board.shape[1]-1: sum_board[i,j] = board[i,j-1]+board[i-1,j-1]+board[i-1,j]+board[i-1,j+1]+board[i,j+1]
            elif i!=0 and i!=board.shape[0]-1 and j==0: sum_board[i,j] = board[i-1,j]+board[i-1,j+1]+board[i,j+1]+board[i+1,j+1]+board[i+1,j]
            elif i!=0 and i!=board.shape[0]-1 and j==board.shape[1]-1: sum_board[i,j] = board[i-1,j]+board[i-1,j-1]+board[i,j-1]+board[i+1,j-1]+board[i+1,j]
            else:
                sum_board[i,j] = board[i-1,j-1]+board[i-1,j]+board[i-1,j+1]+board[i,j-1]+board[i,j+1]+board[i+1,j-1]+board[i+1,j]+board[i+1,j+1]
    return sum_board

def nowyboard(board,sum_board):
    new_board=np.zeros((int(SCREEN_SIZE[0]/ATOM_SIZE),int(SCREEN_SIZE[1]/ATOM_SIZE)))
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i,j]==0 and sum_board[i,j]==3:
                new_board[i,j]=1
            elif board[i,j]==1:
                if sum_board[i,j]==2 or sum_board[i,j]==3:
                    new_board[i,j]=1
    return new_board


print(somsiadsum(board))


pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    gameDisplay.fill(DEAD_COLOR)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i,j]==1:
                pygame.draw.rect(gameDisplay, LIFE_COLOR, (i*ATOM_SIZE,j*ATOM_SIZE,ATOM_SIZE,ATOM_SIZE))
            else:
                pygame.draw.rect(gameDisplay, DEAD_COLOR, (i*ATOM_SIZE,j*ATOM_SIZE,ATOM_SIZE,ATOM_SIZE))
    sum_board=somsiadsum(board)
    board=nowyboard(board,sum_board)

    pygame.display.update()
    clock.tick(FPS)
