"""
Created on Fri Dec  1 17:36:56 2017

@author: Houxudong
"""
import math
import matplotlib.pyplot as plt
from matplotlib import animation

n=float(input('Set the mass of Jupiter /m_J ='))
ME,MJ=me,n*mj
G=4*math.pi**2
ms=1
me=3*10**(-6)
mj=1.9*10**(-3)/2
Gs=G*ms

def threebody(ME,MJ,dt,T):
    Gj=G*MJ
    Ge=G*ME
    re=[[]for i in range(2)]
    rj=[[]for i in range(2)]
    ve=[[]for i in range(2)]
    vj=[[]for i in range(2)]
    re[0].append(1.00)
    re[1].append(0.00)
    rj[0].append(5.20)
    rj[1].append(0.00)
    ve[0].append(0.)
    ve[1].append(2*math.pi)
    vj[0].append(0.)
    vj[1].append(2*math.pi/math.sqrt(5.2))    
    for i in range(int(T/dt)):
        de=math.sqrt(re[0][-1]**2+re[1][-1]**2)
        dj=math.sqrt(rj[0][-1]**2+rj[1][-1]**2)
        dej=math.sqrt((re[0][-1]-rj[0][-1])**2+(re[1][-1]-rj[1][-1])**2)
        ve[0].append(ve[0][-1]+(-G*re[0][-1]/de**3+Gj*(rj[0][-1]-re[0][-1])/dej**3)*dt)
        ve[1].append(ve[1][-1]+(-G*re[1][-1]/de**3+Gj*(rj[1][-1]-re[1][-1])/dej**3)*dt)
        vj[0].append(vj[0][-1]+(-Gs*rj[0][-1]/dj**3+Ge*(re[0][-1]-rj[0][-1])/dej**3)*dt)
        vj[1].append(vj[1][-1]+(-Gs*rj[1][-1]/dj**3+Ge*(re[1][-1]-rj[1][-1])/dej**3)*dt)
        re[0].append(re[0][-1]+ve[0][-1]*dt)
        re[1].append(re[1][-1]+ve[1][-1]*dt)
        rj[0].append(rj[0][-1]+vj[0][-1]*dt)
        rj[1].append(rj[1][-1]+vj[1][-1]*dt)
    return re,rj

re,rj=threebody(ME,MJ,0.001,20)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.plot(rj[0],rj[1],label='Jupiter', color='b',linewidth='1')
plt.plot(re[0],re[1],label='Earth' ,color='r',linewidth='1')
plt.legend()
plt.title(r'Three-body Trajectory')
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.text(-5.8,5.1,r'Mass of Jupiter=%s$m_J$'%(MJ/mj))
plt.show()



