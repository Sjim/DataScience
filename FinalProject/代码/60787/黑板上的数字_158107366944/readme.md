### 题目描述

有两个玩家在玩一个游戏，游戏开始时在黑板上写有n个数字。 每一轮由一个人选择一个数字，并将它从黑板上擦去。 这个游戏直到黑板上只剩下一个数字时结束也就是说会有 n - 1 轮游戏进行。第一个玩家进行第一轮操作，第二个玩家进行之后的一轮操作。

先手玩家希望最后黑板上留下来的数字越小越好；而作为后手希望最后黑板上留下来的数字越大越好。

如果两个人都采取最优的策略， n - 1 轮后黑板上留下来的数字是多少。

### 输入描述

```
第一行包含一个整数 n（1 ≤ n ≤ 1000) 黑板上初始的数字个数。
第二行包含 n 个整数 (1 ≤ ai ≤ 10^6)
```

### 输出描述

```
输出最后会留在黑板上的数字
```

### 测试样例

#### 样例1: 输入-输出

```
3
2 1 3
```

```
2
```

#### 样例2: 输入-输出

```
3
2 2 2
```

```
2
```

### 题目来源

CodeForces
