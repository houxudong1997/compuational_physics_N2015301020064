import math
import time
import pygame
import matplotlib.pyplot as plt
import numpy as np

from pygame.locals import *
 

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
shellpos=[94,400]
v = 6.8
g = 0.098
a=45
v= float(v)
a= float(a)
dt = 1

keys = [False, False,False]

cannon = pygame.image.load("resources/images/cannon.png")
background = pygame.image.load("resources/images/background.png")
shell = pygame.image.load("resources/images/shell.png")
target = pygame.image.load("resources/images/target.png") 

while 1:
    
    screen.fill(0)
   
    screen.blit(background, (0,0))
    screen.blit(cannon, (10,400))
    screen.blit(target, (560,400))
   

    pygame.display.flip()
    i=0
    list1 = [0]
    list2 = [0]
    ra = a * 3.14 / 180
    vx = v * np.cos(ra)
    vy = v * np.sin(ra)

    for event in pygame.event.get():
       
        
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_s:
                keys[1]=True
            elif event.key==K_a:
                keys[2]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_s:
                keys[1]=False  
            elif event.key==pygame.K_a:
                keys[2]=False
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
                        
    if keys[0]:
        a+=3
    elif keys[1]:
        a-=3
    if keys[2]:
        
        while list2[i] >= 0:
            x = list1[i] + vx * dt
            list1.append(x)
            y = list2[i] + vy * dt
            list2.append(y)
            vy -= g * dt
            i += 1
            time.sleep(0.04)
            shellpos=[94+x,400-y]
            screen.blit(background, (0,0))
            screen.blit(cannon, (10,400))
            screen.blit(target, (560,400))            
            screen.blit(shell, shellpos) 
            pygame.display.flip()
            


