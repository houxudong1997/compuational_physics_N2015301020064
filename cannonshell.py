# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:00:38 2017

@author: Houxudong
"""

import matplotlib.pyplot as plt
import numpy as np


distance = [0]
v = 700
g = 9.8
a = 0
v= float(v)
a= float(a)
dt = 1
vy -= g * dt
plt.figure(figsize=(8,6))
plt.xlim(0,60000)
plt.ylim(0,40000)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("cannon shell")

while a <= 90:
    i=0
    list1 = [0]
    list2 = [0]
    ra = a * 3.14 / 180
    vx = v * np.cos(ra)
    vy = v * np.sin(ra)
    while list2[i] >= 0:
        x = list1[i] + vx * dt
        list1.append(x)
        y = list2[i] + vy * dt
        list2.append(y)
        vy -= g * dt
        i += 1
    distance.append(x)
    
    X=np.array(list1)
    Y=np.array(list2)
    plt.plot(X,Y,color="red", linewidth=2.5, linestyle="-")
    
    a+=1

plt.show()
j=0
print("角度  距离")
while j<=90:
    print(j,distance[j])
    
    j+=1