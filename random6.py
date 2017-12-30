# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:23 2017

@author: Houxudong
"""


import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FormatStrFormatter 
from copy import deepcopy

class diffusion():
    def __init__(self,s):
        self.s=s
        
    def grid(self):
        self.x = np.linspace(-50,50,101)
        self.y = np.linspace(-50,50,101)
        self.x,self.y = np.meshgrid(self.x,self.y)
        self.d = np.zeros((101,101))
        self.d[50][50]=1
        self.d1 = deepcopy(self.d)
        return self.d1,self.d,self.x,self.y
        
    def diffusion(self):
        for t in range(self.s):
            for i in range(101):
                for j in range(101):
                    if i==0 or i==100 or j==0 or j==100:
                        pass
                    else:
                        self.d[i][j]=0.25*(self.d1[i+1][j] + self.d1[i-1][j] + self.d1[i][j+1] + self.d1[i][j-1])
            self.d1=deepcopy(self.d)

        for i in range(101):
                for j in range(101):
                    if i==0 or i==100 or j==0 or j==100:
                        pass
                    else:
                        if self.d[i][j]==0:
                            self.d[i][j]=0.25*(self.d1[i+1][j] + self.d1[i-1][j] + self.d1[i][j+1] + self.d1[i][j-1])

        return self.d



A=diffusion(1000)
A.grid()
A.diffusion()
fig = pl.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(A.x, A.y, A.d, rstride=1, cstride=1,cmap=cm.cool)
ax.zaxis.set_major_formatter(FormatStrFormatter('%.04f'))
fig.colorbar(surf, shrink=0.5)
ax.set_ylabel('y(m)')
ax.set_xlabel('x(m)')
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
ax.set_zlim(0,0.001)
ax.set_zlabel('Concentration')
ax.set_title('Diffusion : 3D ($t=1000\Delta t$)')
pl.show()