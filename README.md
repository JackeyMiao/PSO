# PSO

The basic form of Particle Swarm Optimization with Python

## Dependency

- numpy
- math
- fastprogress
- matplotlib.pyplot
- mpl_toolkits.mplot3d

## Task

Find the maximum of the following function
$$
f(x)=\sum_{i=1}^n(-x_i)·sin(\sqrt{|x_i|})\\
-500\le x_i \le500\\
n=2
$$
The 3D model is displayed as followed

<img src="http://typora-jackeymiao.oss-cn-beijing.aliyuncs.com/img/model.png" alt="model" style="zoom: 33%;" />

## Methodology

$$
X_i=(x_{i1},x_{i2},...,x_{in})\\
V_i=(v_{i1},v_{i2},...,v_{in})\\
P_i=(p_{i1},p_{i2},...,p_{in})
$$

where $X_i$，$Y_i$，$P_i$ is respectively the position, the velocity, the optimal position so far of the particle.

Set f(X) as the objective function of minimum, so that the minimum position of the particle i can be defined as the following formula.
$$
P_i(t+1)=P_i(t)\qquad if\quad f(x_i(t+1))\geq f(P_i(t))\\
P_i(t+1)=X_i(t+1)\qquad if\quad f(x_i(t+1))\lt f(P_i(t))
$$
Let the number of particles be $s$, so that the best position for all particles is $P_g(t)$, which is called the global best position.
$$
P_g=min\{f(P_0(t)),f(P_1(t)),...,f(P_s(t))\}
$$
So that the Evolution Equation can be described as
$$
v_{ij}(t+1)=v_{ij}(t)+c_1r_{1j}(t)(P_{ij}(t)-x_{ij}(t))+c_2r_{2j}(t)(P_{gj}(t)-x_{ij}(t))\\
x_{ij}(t+1)=x_{ij}(t)+v_{ij}(t+1)
$$
where the subscript $j$ represents the j st dimension of the particle, the subscript $i$ represents the particle $i$, the subscript $t$ represents the t st generation.

The constant $c_1$，$c_2$ is sampled from [0,2]，and $r_1$~$U(0,1)$， $r_2$~$U(0,1)$ are two independent random function.

## Result

![scatter](http://typora-jackeymiao.oss-cn-beijing.aliyuncs.com/img/scatter.png)
