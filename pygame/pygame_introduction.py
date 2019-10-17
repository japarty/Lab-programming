import pygame

BLACK=(200,120,255)
SCREEN_SIZE=800

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
graphics_list={"jump":[],"walk":[],"climb":[],"idle":[]}
graphics_list["walk"].append(pygame.image.load("Poses/player_walk1.png"))
graphics_list["walk"].append(pygame.image.load("Poses/player_walk2.png"))
graphics_list["climb"].append(pygame.image.load("Poses/player_climb1.png"))
graphics_list["climb"].append(pygame.image.load("Poses/player_climb2.png"))
graphics_list["idle"].append(pygame.image.load("Poses/player_idle.png"))
graphics_list["idle"].append(pygame.image.load("Poses/player_idle.png"))
indx=0
x=10
y=10
flag_w=0
flag_a=0
flag_s=0
flag_d=0
movement_type="idle"
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_w:
                flag_w=1
                movement_type="climb"
            if event.key == pygame.K_a:
                flag_a=1
                movement_type="walk"
            if event.key == pygame.K_s:
                flag_s=1
                movement_type="climb"
            if event.key == pygame.K_d:
                flag_d=1
                movement_type="walk"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                flag_w=0
                if flag_w==0 and flag_a==0 and flag_s==0 and flag_d==0: movement_type="idle"
            if event.key == pygame.K_a:
                flag_a=0
                if flag_w==0 and flag_a==0 and flag_s==0 and flag_d==0: movement_type="idle"
            if event.key == pygame.K_s:
                flag_s=0
                if flag_w==0 and flag_a==0 and flag_s==0 and flag_d==0: movement_type="idle"
            if event.key == pygame.K_d:
                flag_d=0
                if flag_w==0 and flag_a==0 and flag_s==0 and flag_d==0: movement_type="idle"
    if flag_w==1 and y>=0: y-=5
    if flag_a==1 and x>=0: x-=5
    if flag_s==1 and y<SCREEN_SIZE-110: y+=5
    if flag_d==1 and x<SCREEN_SIZE-70: x+=5
    gameDisplay.fill(BLACK)
    gameDisplay.blit(graphics_list[movement_type][indx],(x,y))
    if indx==0: indx=1
    else: indx=0
    pygame.display.update()
    clock.tick(10)
