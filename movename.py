# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:15:46 2017

@author: Administrator
"""
import time
import pygame
from pygame.locals import *
width, height = 640, 250
screen=pygame.display.set_mode((width, height))

namepos=[0,100]
name = pygame.image.load("resources/images/name.png")
while 1:
    while namepos[0]<640:
        screen.fill([255,255,255])
        screen.blit(name, namepos)
        pygame.display.flip()
        namepos[0]+=5
        time.sleep(0.1)
    namepos[0]=0