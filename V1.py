# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:55:19 2017

@author: Houxudong
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from functools import reduce

delta=0.01
deltaV,times=10,0

V=[[0.]*(int(1+1/delta))for i in range(int(1+1/delta))]
for i in range(1+int(round(0.3/delta))):
    V[int(round(0.3/delta))][i]=-1.

def updateV(V_old):
    V_new=[[0.]*len(V_old)for i in range(len(V_old))]
    for i in range(1,len(V_old)-1):
        for j in range(1,len(V_old)-1):
            V_new[i][j]=(V_old[i-1][j]+V_old[i+1][j]+V_old[i][j-1]+V_old[i][j+1])/4
    for j in range(1,len(V_old)-1):
        V_new[0][j]=(V_old[0][j-1]+V_old[0][j+1])/4
    for k in range(1,len(V_old)-1):
        V_new[k][0]=(V_old[k-1][0]+V_old[k+1][0]+2*V_old[k][1])/4
    V_new[0][0]=V_old[0][1]/2
    for l in range(1+int(round(0.3/delta))):
        V_new[int(round(0.3/delta))][l]=-1.
    return V_new

while deltaV > len(V)**2*10**(-5):
    V1=updateV(V)
    V=updateV(V1)
    v=[]
    for i in range(len(V)):
        v.append(reduce(lambda x,y:x+y,(map(lambda a,b:abs(a-b),V1[i],V[i]))))
    deltaV=reduce(lambda x,y:x+y,v)
    times=times+1

N=len(V)
V1=np.transpose(V)
V3=[[0.]*(N-1) for i in range(N)]
for i in range(N):
    for j in range(N-1):
        V3[i][j]=-V1[N-1-i][N-1-j]

for i in range(N):
    V3[i].extend(V1[N-1-i])

V_whole=V3
for i in range(N-1):
    V_whole=V_whole+[V3[N-2-i]]
del V1,V3


fig = plt.figure()
ax = Axes3D(fig)
x=np.linspace(-1,1,len(V_whole))
X,Y= np.meshgrid(x,x)
ax.plot_surface(X,Y,V_whole, rstride=1, cstride=1, cmap='cool')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Electric Potential/V')
ax.set_title(r'Electric Potential Distribution Near Two Metal Plates,$\Delta=$%s'%delta)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1.2,1.2)
ax.contourf(X, Y, V_whole, zdir='z', offset=-1.2, cmap=plt.cm.cool)
plt.show()

