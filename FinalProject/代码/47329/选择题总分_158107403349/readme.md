### 题目描述

一个班级的学生写了一份只有选择题的测试。这个班有 n 个学生。测试有 m 个问题，每个问题都有 5 个可能的答案 (A, B, C, D或E)，每个问题都有一个正确的答案。问题 i 的正确答案值 ai 分，不正确的答案得零分。

学生们记得他们在考试中给出的答案，但是他们不知道正确的答案是什么。他们非常乐观，所以他们想知道班上所有学生的最大可能总分是多少。

### 输入描述

```
第一行包含整数 n 和 m (1≤n,m≤1000) 为班级人数和考试题目数。
下面 n 行中的每一行都包含字符串 si，描述第 i 个学生的答案。第 j 个字符表示第 j 个问题的学生答案(A、B、C、D或E)
最后一行包含 m 个整数 a1,a2，…，am (1≤ai≤1000) 为每个问题正确答案的分数。
```

### 输出描述

```
一个整数表示学生总分的最大可能
```

### 测试样例

#### 样例1: 输入-输出

```
2 4
ABCD
ABCE
1 2 3 4
```

```
16
```

#### 样例2: 输入-输出

```
3 3
ABC
BCD
CDE
5 4 12
```

```
21
```

### 题目来源

CodeForces
