# 课后习题1.2
* Queation:The position of an object moving horizontally with a constant velocity, v, is described by the equation:
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dx}{dt}=v" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v" title="\frac{dx}{dt}=v" /></a> (1.9)
Assuming that the velocity is a constant, say v=40m/s, use the Euler method to solve (1.9) for x as a function of time.
Compare your result with the exact solution.
* 运用欧拉方法求常微分方程（1.9）的近似解，x(n+1)-x(n)=vh，v=40m/s是常量，不妨取t=0时x=0, h为时间间隔，取h=0.1s，求出相应的x(1)~x(10)的值，
并且绘制出x-t曲线。曲线如下图所示。
![图像](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/%E5%9B%BE%E5%83%8F.png)
* 近似解与实际解之间不存在误差。
* [代码](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/Euler%20mothed.py)
