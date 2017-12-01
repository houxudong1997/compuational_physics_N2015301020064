# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:01:38 2017

@author: Houxudong
"""
import math
import matplotlib.pyplot as plt
from matplotlib import animation

G=4*math.pi**2
MS=1
ME=3*10**(-6)
MJ=1.9*10**(-3)/2
Gs=G*MS

def threebody(me,mj,dt,T):
    Gj=G*mj
    Ge=G*me
    re=[[]for i in range(2)]
    rj=[[]for i in range(2)]
    rs=[[]for i in range(2)]
    ve=[[]for i in range(2)]
    vj=[[]for i in range(2)]
    vs=[[]for i in range(2)]
    re[0].append(1.00)
    re[1].append(0.00)
    rj[0].append(5.20)
    rj[1].append(0.00)
    rs[0].append(0.00)
    rs[1].append(0.00)
    ve[0].append(0.00)
    ve[1].append(2*math.pi)
    vj[0].append(0.00)
    vj[1].append(2*math.pi/math.sqrt(5.2))
    vs[0].append(0.00)
    vs[1].append(0.00)
    for i in range(int(T/dt)):
        de=math.sqrt((re[0][-1]-rs[0][-1])**2+(re[1][-1]-rs[1][-1])**2)
        dj=math.sqrt((rj[0][-1]-rs[0][-1])**2+(rj[1][-1]-rs[1][-1])**2)
        dej=math.sqrt((re[0][-1]-rj[0][-1])**2+(re[1][-1]-rj[1][-1])**2)
        for k in range(2):
            ve[k].append(ve[k][-1]+(Gs*(rs[k][-1]-re[k][-1])/de**3+Gj*(rj[k][-1]-re[k][-1])/dej**3)*dt)
            vj[k].append(vj[k][-1]+(Gs*(rs[k][-1]-rj[k][-1])/dj**3+Ge*(re[k][-1]-rj[k][-1])/dej**3)*dt)
            vs[k].append(vs[k][-1]+(Ge*(re[k][-1]-rs[k][-1])/de**3+Gj*(rj[k][-1]-rs[k][-1])/dj**3)*dt)
            re[k].append(re[k][-1]+ve[k][-1]*dt)
            rj[k].append(rj[k][-1]+vj[k][-1]*dt)
            rs[k].append(rs[k][-1]+vs[k][-1]*dt)
    return rs,re,rj

n=float(input('Set the mass of Jupiter /m_J ='))
me,mj = ME,MJ*n
rs,re,rj=threebody(me,mj,0.001,20)
plt.xlim(-2,100)
plt.ylim(-2,60)
plt.plot(rj[1],rj[0],label='Jupiter')
plt.plot(re[1],re[0],label='Earth')
plt.plot(rs[1],rs[0],label='Sun')
plt.title('Three-body Trajectory')
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.text(2.4,20,'Mass of Jupiter=%s$m_J$'%(mj/MJ))
plt.legend()

plt.show()



