#Import thu vien 
import pygame
import sys
import random
pygame.init()
clock=pygame.time.Clock()
#tieu de va icon
pygame.display.set_caption('Robot_running')
icon=pygame.image.load(r'assets\icon.png')
pygame.display.set_icon(icon)
#Cua so game 
screen=pygame.display.set_mode((600,300))
#Load hinh anh
bg=pygame.image.load(r'assets\background.jpg')
ps4=pygame.image.load(r'assets\maychoigame.png')
logo=pygame.image.load(r'assets\ueh.png')
robot_1 = pygame.transform.scale2x(pygame.image.load(r'assets\robot1.png'))
robot_2 = pygame.transform.scale2x(pygame.image.load(r'assets\robot2.png'))
robot_3 = pygame.transform.scale2x(pygame.image.load(r'assets\robot3.png'))
robot_4 = pygame.transform.scale2x(pygame.image.load(r'assets\robot4.png'))
robot_list=[robot_1,robot_2,robot_3,robot_4]
robot_index = 0
robot = robot_list[robot_index]
#load am thanh
sound1=pygame.mixer.Sound(r'sound\score.wav')
sound2=pygame.mixer.Sound(r'sound\gameover.wav')
#tao timer cho robot
robotrun = pygame.USEREVENT
pygame.time.set_timer(robotrun,150)
#khoi tao
score, hscore=0,0
bg_x,bg_y=0,0
ps4_x,ps4_y=550,235
lg_x,lg_y=0,0
robot_x,robot_y=0,200
x_def=5
y_def=7 #toc do roi robot
jump=False 
gameplay=True
#ham hieu ung robot
def robot_animation():
    new_robot = robot_list[robot_index]
    new_robot_hcn = screen.blit(robot,(robot_x,robot_y))
    return new_robot,new_robot_hcn
#ham check va cham
def checkvc():
    if robot_hcn.colliderect(ps4_hcn):
        pygame.mixer.Sound.play(sound2)
        return False
    return True
#dua diem vao game
game_font=pygame.font.Font('04B_19.TTF',15)
game_font1= pygame.font.Font('Tropisky.ttf',80)
def score_view():
    if gameplay:
        score_txt=game_font.render(f'score: {int(score)}',True,(0,0,0))
        screen.blit(score_txt,(460,20))
        hscore_txt=game_font.render(f'High score: {int(hscore)}',True,(0,0,0))
        screen.blit(hscore_txt,(460,40))
    else:
        score_txt=game_font.render(f'score: {int(score)}',True,(0,0,0))
        screen.blit(score_txt,(460,20))
        hscore_txt=game_font.render(f'High score: {int(hscore)}',True,(0,0,0))
        screen.blit(hscore_txt,(460,40))
        over_txt=game_font1.render(f'GAME OVER',True,(255,0,0))
        screen.blit(over_txt,(200,120))
#vong lap xu li game
running=True
while running:
    #chinh FPS
    if 5>score>=0:
        clock.tick(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and gameplay:
                if robot_y==200:
                    jump=True 
            if event.key==pygame.K_SPACE and gameplay==False:
                gameplay=True
        if event.type == robotrun:
            if robot_index < 2:
                robot_index += 1
            else:
                robot_index = 0
            robot, robot_hcn = robot_animation()
    if gameplay:
        #bg
        bg_hcn=screen.blit(bg,(bg_x,bg_y))
        bg2_hcn=screen.blit(bg,(bg_x+600,bg_y))
        bg_x-=x_def
        if bg_x==-600: bg_x=0
        elif 10>score>=5:clock.tick(55)
        elif 25>score>=10:clock.tick(60)
        elif 30>score>=25:clock.tick(65)
        elif 35>score>=30:clock.tick(70)
        elif 40>score>=35:clock.tick(75)
        elif 45>score>=40:clock.tick(80)
        elif 50>score>=45:clock.tick(85)
        elif 55>score>=50:clock.tick(90)
        elif 60>score>=55:clock.tick(95)
        elif score>=60:clock.tick(100)
        #logo ueh
        lg_hcn=screen.blit(logo,(lg_x,lg_y))
        #chuong ngai vat
        ps4_hcn=screen.blit(ps4,(ps4_x,ps4_y))
        ps4_x-=x_def
        if ps4_x==-20:
            ps4_x=550
            score+=1#
            pygame.mixer.Sound.play(sound1)#
        #robot
        robot_hcn=screen.blit(robot,(robot_x,robot_y))
        if robot_y>=80 and jump:
            robot_y-=y_def
        else:
            jump=False
        if robot_y<200 and jump==False:
            robot_y+=y_def
        if hscore<score: hscore=score
        gameplay=checkvc()
        score_view()
    else:
        #reset game
        bg_x,bg_y=0,0
        ps4_x,ps4_y=550,235
        robot_x,robot_y=0,200
        bg_hcn=screen.blit(bg,(bg_x,bg_y))
        lg_hcn=screen.blit(logo,(lg_x,lg_y))
        ps4_hcn=screen.blit(ps4,(ps4_x,ps4_y))
        robot_hcn=screen.blit(robot,(robot_x,robot_y))
        score=0
        score_view()
    pygame.display.update()