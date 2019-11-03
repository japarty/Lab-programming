import pygame
import random

BALL_SIZE=10
BG_COLOR=(200,120,255)
PALETKA_COLOR=(0,255,0)
BALL_COLOR=(255,0,0)
BLOCK_COLOR=(0,0,255)
PALETKA_SIZE=[70,10]
BLOCK_SIZE=[50,20]
SCREEN_SIZE=[500,400]
FPS=60
speed=2

blocks=[]

for i in range(3):
    x=25
    y=10+(20+BLOCK_SIZE[1])*i
    for q in range(6):
        blocks.append([x,y])
        x+=BLOCK_SIZE[0]+25
paletka_position=[SCREEN_SIZE[0]/2-PALETKA_SIZE[0]/2,SCREEN_SIZE[1]-50]
ball_position=[paletka_position[0]+PALETKA_SIZE[0]/2-BALL_SIZE/2,paletka_position[1]-BALL_SIZE]
print(len(blocks))
print(blocks)
pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
clock = pygame.time.Clock()

flag_left=0
flag_right=0
flag_up=0
ball_on_paletka=1
start=["left","right"]
direction=[start[random.randint(0,1)],"up"]
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_LEFT:
                flag_left=1
            if event.key == pygame.K_RIGHT:
                flag_right=1
            if event.key == pygame.K_UP:
                flag_up=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_LEFT:
                flag_left=0
            if event.key == pygame.K_RIGHT:
                flag_right=0
            if event.key == pygame.K_UP:
                flag_up=0
    if flag_left==1 and paletka_position[0]>1: paletka_position[0]-=5
    if flag_right==1 and paletka_position[0]<SCREEN_SIZE[0]-PALETKA_SIZE[0]: paletka_position[0]+=5
    if flag_up==1: ball_on_paletka=0

    if ball_position[0]<=0: direction[0]="right"
    if ball_position[0]>=SCREEN_SIZE[0]-BALL_SIZE: direction[0]="left"

    if ball_on_paletka==1: ball_position=[paletka_position[0]+PALETKA_SIZE[0]/2-BALL_SIZE/2,paletka_position[1]-BALL_SIZE]
    else:
        if direction[0]=="left":
            ball_position[0]-=speed
            if direction[1]=="up":
                ball_position[1]-=speed
            elif direction[1]=="down":
                ball_position[1]+=speed
        elif direction[0]=="right":
            ball_position[0]+=speed
            if direction[1]=="up":
                ball_position[1]-=speed
            elif direction[1]=="down":
                ball_position[1]+=speed
        if ball_position[1]<=0: direction[1]="down"
        if ball_position[1]==paletka_position[1]-BALL_SIZE:
            if ball_position[0]>=paletka_position[0] and ball_position[0]<=paletka_position[0]+PALETKA_SIZE[0]-BALL_SIZE:
                direction[1]="up"
        if ball_position[1]>=SCREEN_SIZE[1]-BALL_SIZE: exit()

    gameDisplay.fill(BG_COLOR)
    pygame.draw.rect(gameDisplay, PALETKA_COLOR,(paletka_position[0],paletka_position[1],PALETKA_SIZE[0],PALETKA_SIZE[1]))
    pygame.draw.rect(gameDisplay, BALL_COLOR,(ball_position[0],ball_position[1],BALL_SIZE,BALL_SIZE))
    for i in range(len(blocks)):
        if blocks[i]!=0:
            pygame.draw.rect(gameDisplay, BLOCK_COLOR,(blocks[i][0],blocks[i][1],BLOCK_SIZE[0],BLOCK_SIZE[1]))
            if ball_position[0]>blocks[i][0] and ball_position[0]<blocks[i][0]+BLOCK_SIZE[0]:
                if ball_position[1]==blocks[i][1]:
                    direction[1]="up"
                    blocks[i]=0
                    print("hit")
                elif ball_position[1]==blocks[i][1]+BLOCK_SIZE[1]:
                    direction[1]="down"
                    blocks[i]=0
                    print("hit")
            elif ball_position[1]>blocks[i][1] and ball_position[1]<blocks[i][1]+BLOCK_SIZE[1]:
                if ball_position[0]==blocks[i][0]:
                    direction[0]="left"
                    blocks[i]=0
                    print("hit")
                elif ball_position[0]==blocks[i][0]+BLOCK_SIZE[0]:
                    direction[0]="right"
                    blocks[i]=0
                    print("hit")



    pygame.display.update()
    clock.tick(FPS)
