#最大流的Ford-Fulkerson方法

## 残留网络 Residual networks
* *残留网络*的概念，流网络G和流f，残留网络G_f由残留容量的边组成。
c_f(u,v) = c(u,v) - f(u,v)。说的是网络中剩余的容量和边所构成的网络，称为残留网络 Residual networks。
那些流等于容量的边，由于残留容量为0，故不再残留网络中。
* *残留网络*G_f也可能包含不在原网络G中的边！？
 
# 流网络的切 cut
流网络 G=(V,E)的切是指对顶点集合的一个划分 (S,T)，S+T=V。f是G上的流，那么切的流
![切的流](http://chart.apis.google.com/chart?cht=tx&chl=f(S%2CT)%20%3D%20%5Csum_%7Bu%20%5Cin%20S%7D%20%5Csum_%7Bv%20%5Cin%20T%7D%20f(u%2Cv)%20-%20%20%5Csum_%7Bu%20%5Cin%20S%7D%20%5Csum_%7Bv%20%5Cin%20T%7D%20f(v%2Cu))


这里利用到了[Google tex 公式API](http://chart.apis.google.com/chart?cht=tx&chl=\Pi)