### 题目描述

DZY 有一个哈希表，有 0~p-1 共 p 个存储位置。他现在使用 h(x) = x mod p 作为哈希函数往这个哈希表中插入 n 个元素。但是这个哈希表的每个存储位置只能放一个元素，但存储位置存在元素时，在往里面插入元素就会发生冲突，请写一个程序帮助 DZY 在冲突发生时告知他冲突发生在第几次插入操作，如果没有冲突，则输出 -1。

### 输入描述

```
第一行为哈希表的存储位置数 p 和需要插入的元素数 n 个 (2 ≤ p, n ≤ 300)
接下来 n 行，每行为一个整数，表示要插入的元素 (0 ≤ xi ≤ 10^9)
```

### 输出描述

```
若有冲突发生，输出第一次冲突发生时，在执行的插入操作序数，否则输出 -1
```

### 测试样例

#### 样例1: 输入-输出

```
10 5
0
21
53
41
53
```

```
4
```

#### 样例2: 输入-输出

```
5 5
0
1
2
3
4
```

```
-1
```

### 题目来源

CodeForces
