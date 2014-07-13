# Chapter 2 Concept learning and the general-to-specific ordering
概念学习，指从训练集中的输入输出学习一个布尔值函数。

## Inductive lerning 归纳
归纳学习假设，任何在一个充分大的训练集中近似成立的假设
在没有观测的样例中也会近似成立！

假设空间H中的关系 more general 和 more specific 是一个部分序关系
### Find-S 算法

```
初始化 h 为假设空间H中的最特殊的假设
for each 训练集中的正例 x
	for each 属性约束 ai in h
		if x 满足 ai
			do nothing
		else
			将ai替换成x满足的下一个更一般的假设
输出 h
```

### Candidate-Elimination 算法

一个假设h在训练集D中是一致的consistent，当且仅当h(x)=c(x)，
对D中一切(x,c(x))成立。即假设对所有训练集都成立。
Consistent(h,D) = (\forall <x,c(x)> \in D) h(x) = c(x)

### version space 
VS_H,D = {h \in H | Consistent(h, D)}
即在训练集D中一致成立的假设的集合。