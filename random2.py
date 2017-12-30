# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 20:00:45 2017

@author: Houxudong 
"""

import random
import turtle
wn=turtle.Screen()
wn.bgcolor('white')
tess=turtle.Turtle()
tess.color('black')
tess.pensize(1)
for d in range (101):
    x=random.randrange(0,51)
    det = random.random()
    tess.speed(5)
    tess.forward(x)
    tess.left(det*360)
    tess.stamp()
wn.exitonclick()