### 题目描述

小奇所在的国家一共由n个城市和m条连接这些城市的双向道路组成。

小奇非常喜欢骑自行车，它常常骑着自行车从一个城市，沿着某些双向道路到达另一个城市。

现在，这个国家要关闭其所有的道路以便翻修，但为了保证必要的交通运输，第i条道路会在第i天暂时开放。

小奇为了了解本次翻修对它旅行的影响，因此想知道，如果它第l天在一个城市s，在第r天或之前是否能到达城市t。（小奇不需要第l天就立即离开s，也不需要恰好在第r天到达城市t。）

为了更全面地评估这个影响，小奇会有许多的询问，但它一下子算不过来，就只好找你帮忙了。

### 输入描述


第一行三个正整数n,m,q,分别表示城市数、道路数、询问数。

接下来有m行,其中第i行有两个正整数u<sub>i</sub>,v<sub>i</sub>(u<sub>i</sub>≠v<sub>i</sub>),表示有一条连接u<sub>i</sub>,v<sub>i</sub>两座城市的双向道路,并且这条道路在第i天暂时开放,不保证整张图连通,不保证有且仅有一条道路连接u<sub>i</sub> , v<sub>i</sub>两座城市。

接下来q行,每行四个正整数l<sub>i</sub>,r<sub>i</sub>,s<sub>i</sub>,t<sub>i</sub>,表示一个询问。

### 输出描述

```
q行，第i行表示第i个询问的答案，可行输出Yes，不可行输出No。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 4 6
1 2
2 3
3 4
3 5
1 3 1 4
1 3 2 4
1 4 4 5
1 4 4 1
2 3 1 4
2 2 2 3
```
```
Yes
Yes
Yes
No
No
Yes
```