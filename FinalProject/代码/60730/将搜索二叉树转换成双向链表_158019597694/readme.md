### 题目描述

对二叉树的节点来说，有本身的值域，有指向左孩子节点和右孩子节点的两个指针；对双向链表的节点来说，有本身的值域，有指向上一个节点和下一个节点的指针。在结构上，两种结构有相似性，现在有一棵搜索二叉树，请将其转换成一个有序的双向链表。


### 输入描述

```
第一行一个数字 n 表示二叉树的总结点数。
以下 n 行每行三个整数 fa lch rch，表示节点 fa 的左儿子节点为 lch，右儿子节点为 rch。(若 lch 为 0 则表示 fa 没有左儿子，rch同理)

第一行的 fa 为根节点。

ps:节点的标号就是节点的值。
```
### 输出描述

```
在给定的函数中返回双向链表的头指针。
```

### 测试样例
#### 样例1:输入-输出-解释

```
9
6 4 7
4 2 5
2 1 3
5 0 0
1 0 0
3 0 0
7 0 9
9 8 0
8 0 0
```
```
1 2 3 4 5 6 7 8 9
```
```
无
```

### 题目来源  
`nowcoder.com`