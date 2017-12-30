# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:40:50 2017

@author: Houxudong
"""

import numpy as np
import pylab as pl
import random
from mpl_toolkits.mplot3d import Axes3D

class random_walk:

    def walk(self):
        self.i=[0]
        self.r_2ave=np.zeros(101)
        while self.i[-1]<1000:
            self.x=[0]
            self.y=[0]
            self.z=[0]
            self.t=[0]
            self.r_2=[0]
            while self.t[-1]<100:
                a=random.randrange(6)
                if a==0:
                    x_new=self.x[-1]+1
                    y_new=self.y[-1]
                    z_new=self.z[-1]
                elif a==1:
                    x_new=self.x[-1]-1
                    y_new=self.y[-1]
                    z_new=self.z[-1]
                elif a==2:
                    x_new=self.x[-1]
                    y_new=self.y[-1]+1
                    z_new=self.z[-1]
                elif a==3:
                    x_new=self.x[-1]
                    y_new=self.y[-1]-1
                    z_new=self.z[-1]
                elif a==4:
                    x_new=self.x[-1]
                    y_new=self.y[-1]
                    z_new=self.z[-1]+1
                else:
                    x_new=self.x[-1]
                    y_new=self.y[-1]
                    z_new=self.z[-1]-1
                t_new=self.t[-1]+1
                r_2_new=x_new**2+y_new**2+z_new**2
                self.x.append(x_new)
                self.y.append(y_new)
                self.z.append(z_new)
                self.r_2.append(r_2_new)
                self.t.append(t_new)   
            for l in range(101):
                self.r_2ave[l]=(self.r_2ave[l]*self.i[-1]+self.r_2[l])/(self.i[-1]+1)
            self.i.append(self.i[-1]+1)
        return self.r_2ave, self.t
    def plot(self):
        para = np.polyfit(self.t, self.r_2ave,1)
        poly = np.poly1d(para)
        y_fit = poly(self.t)
        pl.plot(self.t, y_fit, 'b')
        pl.scatter(self.t, self.r_2ave,color='k',s=3)
        pl.xlim(0,100)
        pl.ylim(0,110)
        pl.xlabel('step number(=time)')
        pl.ylabel('$r^2$')
        pl.title('Random walk: 3D(fixed length)')
        pl.show()               
A=random_walk()
A.walk()
A.plot()
fig=pl.figure()

a=fig.add_subplot(111,projection='3d')
a.scatter(A.x,A.y,A.z,color='b')
a.plot(A.x,A.y,A.z,'y')
a.set_xlabel('x')
a.set_ylabel('y')
a.set_zlabel('z')
a.set_title('Random walk: 3D(fixed length)')
pl.show()