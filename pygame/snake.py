import pygame
import random
from collections import deque

square_size=10
fill_color=(0,0,0)
snake_color=(0,255,0)
apple_color=(161,40,48)


SCREEN_SIZE=200
points=0
snakes_elements=[SCREEN_SIZE/2,SCREEN_SIZE/2]
apple_position=[random.randint(0,(SCREEN_SIZE-square_size)/10)*10,random.randint(0,(SCREEN_SIZE-square_size)/10)*10]
snake_elements=[[SCREEN_SIZE/2,SCREEN_SIZE/2]]

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

flag_w=0
flag_s=0
flag_a=0
flag_d=0
speed=10
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_w:
                flag_w=1
                flag_s=0
                flag_a=0
                flag_d=0
            if event.key == pygame.K_s:
                flag_w=0
                flag_s=1
                flag_a=0
                flag_d=0
            if event.key == pygame.K_a:
                flag_w=0
                flag_s=0
                flag_a=1
                flag_d=0
            if event.key == pygame.K_d:
                flag_w=0
                flag_s=0
                flag_a=0
                flag_d=1
    if snake_elements[0][0]==apple_position[0] and snake_elements[0][1]==apple_position[1]:
        while apple_position in snake_elements:
            apple_position=[random.randint(0,(SCREEN_SIZE-square_size)/10)*10,random.randint(0,(SCREEN_SIZE-square_size)/10)*10]
        points+=1
        if flag_w==1:
            if snake_elements[0][1]>0:
                snake_elements.insert(0,[snake_elements[0][0],snake_elements[0][1]-speed])
            else: exit()
        elif flag_s==1:
            if snake_elements[0][1]<SCREEN_SIZE-square_size:
                snake_elements.insert(0,[snake_elements[0][0],snake_elements[0][1]+speed])
            else: exit()
        elif flag_a==1:
            if snake_elements[0][0]>0:
                snake_elements.insert(0,[snake_elements[0][0]-speed,snake_elements[0][1]])
            else: exit()
        elif flag_d==1:
            if snake_elements[0][0]<SCREEN_SIZE-square_size:
                snake_elements.insert(0,[snake_elements[0][0]+speed,snake_elements[0][1]])
            else: exit()
    elif flag_w==1:
        if snake_elements[0][1]>0:
            snake_elements.insert(0,[snake_elements[0][0],snake_elements[0][1]-speed])
            snake_elements.pop(-1)
        else: exit()
    elif flag_s==1:
        if snake_elements[0][1]<SCREEN_SIZE-square_size:
            snake_elements.insert(0,[snake_elements[0][0],snake_elements[0][1]+speed])
            snake_elements.pop(-1)
        else: exit()
    elif flag_a==1:
        if snake_elements[0][0]>0:
            snake_elements.insert(0,[snake_elements[0][0]-speed,snake_elements[0][1]])
            snake_elements.pop(-1)
        else: exit()
    elif flag_d==1:
        if snake_elements[0][0]<SCREEN_SIZE-square_size:
            snake_elements.insert(0,[snake_elements[0][0]+speed,snake_elements[0][1]])
            snake_elements.pop(-1)
        else: exit()


    gameDisplay.fill(fill_color)
    for i in snake_elements:
        pygame.draw.rect(gameDisplay, snake_color,(i[0],i[1],square_size,square_size))
    pygame.draw.rect(gameDisplay, apple_color,(apple_position[0],apple_position[1],square_size,square_size))
    if snake_elements[0] in snake_elements[1:]:
        exit()
    print(apple_position[0],apple_position[1])
    print(int(snake_elements[0][0]),int(snake_elements[0][1]))
    print(points)
    pygame.display.update()
    clock.tick(5)
