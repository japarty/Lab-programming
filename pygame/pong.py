import pygame
import random

BALL_SIZE=10
color=(200,120,255)
GREEN=[0,255,0]
PALETKA_SIZE=70

SCREEN_SIZE=500

ball_position=[SCREEN_SIZE/2,SCREEN_SIZE/2]

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

flag_w=0
flag_s=0
flag_up=0
flag_down=0
x=ball_position[0]
y=ball_position[0]
qwe=[[0,2],[4,6]]
direction=["left","up"]
speed=2
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_w:
                flag_w=1
            if event.key == pygame.K_s:
                flag_s=1
            if event.key == pygame.K_UP:
                flag_up=1
            if event.key == pygame.K_DOWN:
                flag_down=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_w:
                flag_w=0
            if event.key == pygame.K_s:
                flag_s=0
            if event.key == pygame.K_UP:
                flag_up=0
            if event.key == pygame.K_DOWN:
                flag_down=0
    if flag_w==1 and x>1: x-=5
    if flag_s==1 and x<SCREEN_SIZE-PALETKA_SIZE: x+=5
    if flag_up==1 and y>1: y-=5
    if flag_down==1 and y<SCREEN_SIZE-PALETKA_SIZE: y+=5
    if direction[0]=="left":
        ball_position[0]+=speed
        if direction[1]=="up":
            ball_position[1]-=speed
        elif direction[1]=="down":
            ball_position[1]+=speed
    elif direction[0]=="right":
        ball_position[0]-=speed
        if direction[1]=="up":
            ball_position[1]-=speed
        elif direction[1]=="down":
            ball_position[1]+=speed
    if ball_position[1]==0: direction[1]="down"
    elif ball_position[1]==SCREEN_SIZE-BALL_SIZE: direction[1]="up"
    if ball_position[0]==20 and ball_position[1]+BALL_SIZE/2<=x+PALETKA_SIZE and ball_position[1]+BALL_SIZE/2>=x: direction[0]="left"
    if ball_position[0]==SCREEN_SIZE-30 and ball_position[1]+BALL_SIZE/2<=y+PALETKA_SIZE and ball_position[1]+BALL_SIZE/2>=y: direction[0]="right"
    gameDisplay.fill(color)
    pygame.draw.rect(gameDisplay, GREEN,(ball_position[0],ball_position[1],BALL_SIZE,BALL_SIZE))
    pygame.draw.rect(gameDisplay, (255,0,0),(10,x,10,PALETKA_SIZE))
    pygame.draw.rect(gameDisplay, (0,0,255),(SCREEN_SIZE-20,y,10,PALETKA_SIZE))

    pygame.display.update()
    clock.tick(30)
