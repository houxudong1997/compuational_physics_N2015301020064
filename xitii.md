# Chapter 2:Realistic Motion
## Exercise2.6
***
### Background
Use the Euler method to calculate cannon shell trajectories ignoring both air drag and the effect of air density(actually, ignoring the 
former automatically rules out the latter). 
### Analysis
首先用牛顿第二定律可知：<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;x}{\mathrm{d}&space;t}=&space;v_{x}" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;x}{\mathrm{d}&space;t}=&space;v_{x}" title="\frac{\mathrm{d} x}{\mathrm{d} t}= v_{x}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v_{x}}{\mathrm{d}&space;t}=&space;0" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;v_{x}}{\mathrm{d}&space;t}=&space;0" title="\frac{\mathrm{d} v_{x}}{\mathrm{d} t}= 0" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;y}{\mathrm{d}&space;t}=&space;v_{y}" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;y}{\mathrm{d}&space;t}=&space;v_{y}" title="\frac{\mathrm{d} y}{\mathrm{d} t}= v_{y}" /></a>；
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v_{y}}{\mathrm{d}&space;t}=&space;-g" target="_blank"><img src="http://latex.codecogs.com/png.latex?\frac{\mathrm{d}&space;v_{y}}{\mathrm{d}&space;t}=&space;-g" title="\frac{\mathrm{d} v_{y}}{\mathrm{d} t}= -g" /></a>
