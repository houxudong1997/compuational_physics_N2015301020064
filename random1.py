# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:24:12 2017

@author: Houxudong 
"""

import random
import turtle


wn=turtle.Screen()
turtle.screensize(2000,2000)
wn.title("Random walk: 2D")
wn.bgcolor('white')
tess=turtle.Turtle()
tess.shape('classic')
tess.color('black')
tess.pensize(1)
for i in range (200):
    x=30
    det=random.randrange(4)
    if det==0:
        tess.forward(x)
        tess.left(90)
        tess.speed(5)
        tess.stamp()
    elif det==1:
        tess.forward(x)
        tess.left(180)
        tess.speed(5)
        tess.stamp()
    elif det==2:
        tess.forward(x)
        tess.left(270)
        tess.speed(5)
        tess.stamp()
    elif det==3:
        tess.forward(x)
        tess.left(360)
        tess.speed(5)
        tess.stamp()        
wn.exitonclick()