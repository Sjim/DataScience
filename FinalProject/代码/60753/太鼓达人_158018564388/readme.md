### 题目描述

七夕祭上，Vani 牵着 cl 的手，在明亮的灯光和欢乐的气氛中愉快地穿行。这时，在前面忽然出现了一台太鼓达人机台，而在机台前坐着的是刚刚被精英队伍成员 XLk、Poet_shy 和 lydrainbowcat 拯救出来的的 applepi。看到两人对太鼓达人产生了兴趣，applepi 果断闪人，于是 cl 拿起鼓棒准备挑战。然而即使是在普通难度下，cl 的路人本性也充分地暴露了出来。一曲终了，不但没有过关，就连鼓都不灵了。Vani 十分过意不去，决定帮助工作人员修鼓。

鼓的主要元件是M个围成一圈的传感器。每个传感器都有开和关两种工作状态，分别用1和0表示。显然，从不同的位置出发沿顺时针方向连续检查K个传感器可以得到M个长度为K的01串。Vani 知道这M个01串应该是互不相同的。而且鼓的设计很精密，M会取到可能的最大值。现在 Vani 已经了解到了K的值，他希望你求出M的值，并给出字典序最小的传感器排布方案。

### 输入描述

```
一个整数K。

数据范围：2≤K≤11
```
### 输出描述

```
一个整数M和一个二进制串，由一个空格分隔。表示可能的最大的M，以及字典序最小的排布方案，字符 0 表示关，1 表示开。你输出的串的第一个字和最后一个字是相邻的。
```

### 测试样例
#### 样例1:输入-输出-解释

```
3
```
```
8 00010111
```
```
得到的8个01串分别是000, 001, 010, 101, 011,111, 110和100。注意前后是相邻的。长度为3的二进制串总共只有8种，所以M =8 一定是可能的最大值。
```

### 题目来源  
`BZOJ`