# 棒球运动
## 课后习题2.21
姓名：侯旭东
学号：2015301020064
班级：15级材料物理班
### 题目分析
按照之前的设定，棒球被击出后会受到空气阻力及重力影响，即<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}Vy&space;}{\mathrm{d}&space;t}=&space;-g" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}Vy&space;}{\mathrm{d}&space;t}=&space;-g" title="\frac{\mathrm{d}Vy }{\mathrm{d} t}= -g" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v_{x}}{\mathrm{d}&space;t}=-\frac{B_{2}}{m}vv_{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;v_{x}}{\mathrm{d}&space;t}=-\frac{B_{2}}{m}vv_{x}" title="\frac{\mathrm{d} v_{x}}{\mathrm{d} t}=-\frac{B_{2}}{m}vv_{x}" /></a>；
另外，据题意，需另加自旋带来的侧向力，即<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v_{z}}{\mathrm{d}&space;t}=-\frac{S_{0}}{m}wv_{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;v_{z}}{\mathrm{d}&space;t}=-\frac{S_{0}}{m}wv_{x}" title="\frac{\mathrm{d} v_{z}}{\mathrm{d} t}=-\frac{S_{0}}{m}wv_{x}" /></a>；
此外，<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;x}{\mathrm{d}&space;t}=v_{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;x}{\mathrm{d}&space;t}=v_{x}" title="\frac{\mathrm{d} x}{\mathrm{d} t}=v_{x}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;y}{\mathrm{d}&space;t}=v_{y}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;y}{\mathrm{d}&space;t}=v_{y}" title="\frac{\mathrm{d} y}{\mathrm{d} t}=v_{y}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;z}{\mathrm{d}&space;t}=v_{z}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;z}{\mathrm{d}&space;t}=v_{z}" title="\frac{\mathrm{d} z}{\mathrm{d} t}=v_{z}" /></a>。
### 系数分析
上述式子中，<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{B_{2}}{m}=0.0039&plus;\frac{0.0058}{1&plus;exp[\frac{(v-v_{d})}{\Delta&space;}]}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{B_{2}}{m}=0.0039&plus;\frac{0.0058}{1&plus;exp[\frac{(v-v_{d})}{\Delta&space;}]}" title="\frac{B_{2}}{m}=0.0039+\frac{0.0058}{1+exp[\frac{(v-v_{d})}{\Delta }]}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=v_{d}=35m/s" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{d}=35m/s" title="v_{d}=35m/s" /></a>，
<a href="http://www.codecogs.com/eqnedit.php?latex=\Delta&space;=&space;5m/s" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Delta&space;=&space;5m/s" title="\Delta = 5m/s" /></a>，
即<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{B_{2}}{m}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{B_{2}}{m}" title="\frac{B_{2}}{m}" /></a>值确定。
并有<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{S_{0}}{m}\approx&space;0.00041" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{S_{0}}{m}\approx&space;0.00041" title="\frac{S_{0}}{m}\approx 0.00041" /></a>当
<a href="http://www.codecogs.com/eqnedit.php?latex=m=&space;149g" target="_blank"><img src="http://latex.codecogs.com/gif.latex?m=&space;149g" title="m= 149g" /></a>
z时，即<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{S_{0}}{m}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{S_{0}}{m}" title="\frac{S_{0}}{m}" /></a>
值确定。题目给出转速2000rpm。
### 思路
由于侧旋带来力使轨迹横向偏移，则抛球手在保证一定抛射角a1的同时，需要横向的角度偏差a2，使得球准确击中或者说落于9m远处平行点处，假定抛出球的速度为80mph，换算为178m/s
，编程分别画出x-y，x-z轨迹图，可以清楚地看到球的运动轨迹情况。
### [代码](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/Baseball.py)


### 调试
需多次耐心调试改变a1,a2的值，使得抛出的球准确击中9m远处的平行点。
### 图
![图](https://github.com/houxudong1997/compuational_physics_N2015301020064/blob/master/TIM%E5%9B%BE%E7%89%8720171020151233.png?raw=true)
### 结果分析
调试可以出现我们理想的效果，即向上角度为0.079度，侧偏角度为0.06度时，球击中目标。即转速为2000rpm时找准角度是可行的。理性分析两者（角度）应该存在共轭，即角度值
不唯一。可以看到角度都为很小角度，考虑到抛出速度极快且路程极短，角度极小也就可以理解了。
