# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:15:10 2017

@author: Administrator
"""
import math
import pygame
import random
from pygame.locals import *


pygame.init()
pygame.mixer.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100,100]
acc=[0,0]
arrows=[]
badtimer=150
badtimer1=0
badguys=[[640,100]]
healthvalue=194
i=1

healthlogo = pygame.image.load("resources/images/healthlogo.png")
bg1 = pygame.image.load("resources/images/bg1.png")
bg2 = pygame.image.load("resources/images/bg2.png")
bg3 = pygame.image.load("resources/images/bg3.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
arrow = pygame.image.load("resources/images/pao.png")
player = pygame.image.load("resources/images/mengqi.png")
grass = pygame.image.load("resources/images/grass.png")
castle1 = pygame.image.load("resources/images/c1.png")
castle2 = pygame.image.load("resources/images/c2.png")
castle3 = pygame.image.load("resources/images/c3.png")
castle4 = pygame.image.load("resources/images/c4.png")
badguyimg1 = pygame.image.load("resources/images/xiaobing.png")
badguyimg=badguyimg1
# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
bgm="resources/audio/Hello.ogg"

pygame.mixer.music.load(bgm)
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


while 1:
    if i==1:
        
        screen.fill(0)
        screen.blit(bg1, (0,0))
        pygame.font.init()
        font = pygame.font.Font(None, 48)
        text = font.render("START", True, (0,0,0))
        screen.blit(text, (400,350))        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_dx,mouse_dy=pygame.mouse.get_pos()
                if mouse_dx >= 400 and mouse_dx <= 500 and mouse_dy >= 350 and mouse_dy <= 380:
                    i=2
                    
    if i==2:
        # 4 - keep looping through
        running = 1
        exitcode = 0
        while running:
    
            screen.fill(0)
            screen.blit(bg2, (0,0))
            screen.blit(castle1,(20,30))
            screen.blit(castle2,(20,135))
            screen.blit(castle3,(20,240))
            screen.blit(castle4,(20,345))
            screen.blit(healthlogo,(200,0))
    # 6.1 - Set player position and rotation
            position = pygame.mouse.get_pos()
            angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
            playerrot = pygame.transform.rotate(player, 360-angle*57.29)
            playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
            screen.blit(playerrot, playerpos1)
    # 6.2 - Draw arrows
            for bullet in arrows:
                index=0
                velx=math.cos(bullet[0])*6
                vely=math.sin(bullet[0])*6
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                    arrows.pop(index)
                index+=1
                for projectile in arrows:
                    arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
                    screen.blit(arrow1, (projectile[1], projectile[2]))
    # 6.3 - Draw badgers
            if badtimer==0:
                badguys.append([640, random.randint(50,430)])
                badtimer=150-(badtimer1*2)
                if badtimer1>=35:
                    badtimer1=35
                else:
                    badtimer1+=5
            index=0
            for badguy in badguys:
                if badguy[0]<-64:
                    badguys.pop(index)
                badguy[0]-=1
        # 6.3.1 - Attack castle
                badrect=pygame.Rect(badguyimg.get_rect())
                badrect.top=badguy[1]
                badrect.left=badguy[0]
                if badrect.left<64:
                    hit.play()
                    healthvalue -= random.randint(5,20)
                    badguys.pop(index)
        #6.3.2 - Check for collisions
                index1=0
                for bullet in arrows:
                    bullrect=pygame.Rect(arrow.get_rect())
                    bullrect.left=bullet[1]
                    bullrect.top=bullet[2]
                    if badrect.colliderect(bullrect):
                        enemy.play()
                        acc[0]+=1
                        badguys.pop(index)
                        arrows.pop(index1)
                    index1+=1
        # 6.3.3 - Next bad guy
                index+=1
            for badguy in badguys:
                screen.blit(badguyimg, badguy)
    
    # 6.4 - Draw clock
#    font = pygame.font.Font(None, 24)
 #   survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
#    textRect = survivedtext.get_rect()
#    textRect.topright=[635,5]
#    screen.blit(survivedtext, textRect)
    # 6.5 - Draw health bar
            screen.blit(healthbar, (5,5))
            for health1 in range(healthvalue):
                screen.blit(health, (health1+8,8))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:            
                    pygame.quit() 
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key==K_w:
                        keys[0]=True
                    elif event.key==K_a:
                        keys[1]=True
                    elif event.key==K_s:
                        keys[2]=True
                    elif event.key==K_d:
                        keys[3]=True
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_w:
                        keys[0]=False
                    elif event.key==pygame.K_a:
                        keys[1]=False
                    elif event.key==pygame.K_s:
                        keys[2]=False
                    elif event.key==pygame.K_d:
                        keys[3]=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    shoot.play()
                    position=pygame.mouse.get_pos()
                    acc[1]+=1
                    arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
            if keys[0]:
                playerpos[1]-=2
            elif keys[2]:
                playerpos[1]+=2
            if keys[1]:
                playerpos[0]-=2
            elif keys[3]:
                playerpos[0]+=2
            badtimer-=1
    #10 - Win/Lose check
            if pygame.time.get_ticks()>=9000:
                running=0
                exitcode=1
            if healthvalue<=0:
                running=0
                exitcode=0
            if acc[1]!=0:
                accuracy=acc[0]*1.0/acc[1]*100
            else:
                accuracy=0
# 11 - Win/lose display        
        if exitcode==0:
            pygame.font.init()
            font = pygame.font.Font(None, 24)

            screen.blit(gameover, (0,0))
            
        else:
            
            pygame.font.init()
            font = pygame.font.Font(None, 48)
            
            text1 = font.render("Next level", True, (255,255,0))

            screen.blit(youwin, (0,0))
            screen.blit(text1, (400,400))
        while i==2:         
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_dx,mouse_dy=pygame.mouse.get_pos()
                    if mouse_dx >= 400 and mouse_dx <= 550 and mouse_dy >= 400 and mouse_dy <= 430:
                        i=3
            pygame.display.flip()                       
            
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        
    if i==3:
        screen.fill(0)
        screen.blit(bg3, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)        
        
        





