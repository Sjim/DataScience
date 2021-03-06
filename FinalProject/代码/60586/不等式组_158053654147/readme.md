### 题目描述

旺汪与旺喵最近在做一些不等式的练习。这些不等式都是形如ax+b>c 的一元不等式。当然，解这些不等式对旺汪来说太简单了，所以旺喵想挑战旺汪。旺喵给出一组一元不等式，并给出一个数值 。旺汪需要回答的是x=k 时成立的不等式的数量。聪明的旺汪每次都很快就给出了答案。你的任务是快速的验证旺汪的答案是不是正确的。

### 输入描述

```
输入第一行为一个正整数 ，代表接下来有N行。
接下来每一行可能有3种形式：

1、Add a b c, 表明要往不等式组添加一条不等式ax+b>c。

2、Del i, 代表删除第i条添加的不等式（最先添加的是第1条）。

3、Query k, 代表一个询问，即当x=k 时，在当前不等式组内成立的不等式的数量。
注意一开始不等式组为空，a,b,c,i,k 均为整数，且保证所有操作均合法，不会出现要求删除尚未添加的不等式的情况。
```
### 输出描述

```
对于每一个询问“Query k”，输出一行，为一个整数，代表询问的答案。
```

### 测试样例
#### 样例1:输入-输出-解释

```
9
Add 1 1 1
Add -2 4 3
Query 0
Del 1
Query 0
Del 2
Query 0
Add 8 9 100
Query 10
```
```
1
1
0
0
```
```
第1条添加到不等式组的不等式为x+1>1 ，第2条为-2x+4>3 ，所以第1个询问的时候只有第2条不等式可以成立，故输出1。

然后删除第1条不等式，再询问的时候依然是只有第2条不等式可以成立，故输出1。

再删除第2条不等式后，因为不等式组里面没有不等式了，所以没有不等式可以被满足，故输出0。

继续加入第3条不等式8x+9>100 ，当x=k=10时有8×10+9=89<100，故也没有不等式可以被满足，依然输出0。
```

### 题目来源  
`luogu.com.cn`