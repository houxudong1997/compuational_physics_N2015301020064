# Chapter 2:Realistic Motion
## Exercise2.6
### 题目
Use the Euler method to calculate cannon shell trajectories ignoring both air drag and the effect of air density(actually, ignoring the 
former automatically rules out the latter). 
### 分析
1、首先用牛顿第二定律可知x，y各方向位移和速度随时间的变化关系：<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;x}{\mathrm{d}&space;t}=&space;v_{x}" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;x}{\mathrm{d}&space;t}=&space;v_{x}" title="\frac{\mathrm{d} x}{\mathrm{d} t}= v_{x}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v_{x}}{\mathrm{d}&space;t}=&space;0" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;v_{x}}{\mathrm{d}&space;t}=&space;0" title="\frac{\mathrm{d} v_{x}}{\mathrm{d} t}= 0" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;y}{\mathrm{d}&space;t}=&space;v_{y}" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;y}{\mathrm{d}&space;t}=&space;v_{y}" title="\frac{\mathrm{d} y}{\mathrm{d} t}= v_{y}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v_{y}}{\mathrm{d}&space;t}=&space;-g" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;v_{y}}{\mathrm{d}&space;t}=&space;-g" title="\frac{\mathrm{d} v_{y}}{\mathrm{d} t}= -g" /></a>。

2、利用欧拉法：<a href="http://www.codecogs.com/eqnedit.php?latex=x_{i&plus;1}=&space;x_{i}&plus;v_{x,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/png.latex?x_{i&plus;1}=&space;x_{i}&plus;v_{x,i}\Delta&space;t" title="x_{i+1}= x_{i}+v_{x,i}\Delta t" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=v_{x,i&plus;1}=v_{x,i}" target="_blank"><img src="http://latex.codecogs.com/png.latex?v_{x,i&plus;1}=v_{x,i}" title="v_{x,i+1}=v_{x,i}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}=&space;y_{i}&plus;v_{y,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/png.latex?y_{i&plus;1}=&space;y_{i}&plus;v_{y,i}\Delta&space;t" title="y_{i+1}= y_{i}+v_{y,i}\Delta t" /></a>；

3、忽略了空气阻力等的影响，当<a href="http://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}<&space;0" target="_blank"><img src="http://latex.codecogs.com/png.latex?y_{i&plus;1}<&space;0" title="y_{i+1}< 0" /></a>而<a href="http://www.codecogs.com/eqnedit.php?latex=y_{i}=&space;0" target="_blank"><img src="http://latex.codecogs.com/png.latex?y_{i}=&space;0" title="y_{i}= 0" /></a>时炮弹落地，此时x为炮弹射程。

### 编程
模拟地面情况，<a href="http://www.codecogs.com/eqnedit.php?latex=g=&space;9.8" target="_blank"><img src="http://latex.codecogs.com/png.latex?g=&space;9.8" title="g= 9.8" /></a>，设炮弹出射速度为700，忽略空气阻力的理想情况下，为了比较各个角度出射的射程大小，改变出射角度做多组图像。[编程代码](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/cannonshell.py)

### 作图
分别以角度变化间隔为5度和1度做整合图如图：
![da=5](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/cannonshell1.png?raw=true)
![da=1](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/cannonshell.png?raw=true)
