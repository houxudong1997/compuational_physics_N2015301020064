# Chapter 2:Realistic Motion
## Exercise2.6
***
### Background
Use the Euler method to calculate cannon shell trajectories ignoring both air drag and the effect of air density(actually, ignoring the former automatically rules out the latter). 
### Analysis
1. To solve the problem as required,we should first use the Newton's second law,which can be written as`$\displaystyle\frac{d^2x}{dt^2}=0$` and `$\displaystyle\frac{d^2y}{dt^2}= -g$`,where x and y are the horizontal and vertical coordinates of the projectile, and g is the acceleration due to gravity.
2. Then write each of these second-order equations as two first-order differential equations:`$\displaystyle\frac{dx}{dt}=v_x$`;`$\displaystyle\frac{dv_x}{dt}=0$`;`$\displaystyle\frac{dy}{dt}=v_y$`;`$\displaystyle\frac{dv_y}{dt}= -g$`,where `$v_x$` and `$v_y$`are the x and y components of the velocity.
3. Now using the Euler method:
`$x_{i+1}$`=`$x_i$`+`$v_{x,i}$` `$\Delta$`t;</br>`$v_{x,i+1}$`=`$v_{x,i}$` ; </br>`$y_{x,i}$`=`$y_i$`+`$v_{y,i}$` `$\Delta$`t ;</br> `$v_{y,i+1}$`=`$v_{y,i}$`-g`$\Delta$`t.

1. If we ignore both air drag and the effect of air density,the cannon shell stops when `$y_{i+1}$`<0. If we let r=-`$y_n$`/`$y_{n+1}$` then a linear interpolation gives:(`$x_l$`=`$x_n$`+r`$x_{n+1}$`)/r+1, and`$y_l$`=0.
### solution
From the analysis above, we can draw a figure  [specific code](https://github.com/witness97/computationalphysics_N2015301020062/blob/master/cannon%20shell.py). 
</br>![image](http://note.youdao.com/yws/public/resource/a3f15923a7a49ff3fdf830862a72164f/xmlnote/WEBRESOURCE4812d956a957dbca75e3600335faa20a/211)
</br>![image](http://note.youdao.com/yws/public/resource/a3f15923a7a49ff3fdf830862a72164f/xmlnote/WEBRESOURCE0bfb520910cfe1458e4579a6aa003412/215)
</br>![image](http://note.youdao.com/yws/public/resource/a3f15923a7a49ff3fdf830862a72164f/xmlnote/WEBRESOURCE47f38591ddfb911710234f8b76409c6c/221)
All the figures above have a start velocity of 700m/s, but they have different angels of 30,45 and 75.
### Conclution
1. As the figure showing above,we can find that when we ignoring both air drag and the effect of air density,the cannon shell can get the longest distance when it has a start angel of 45.
2. Compara to the Figure 2.4, we can find that the cannon shell can have a longer distance and flying time without both air drag and the effect of air density.
