### 题目描述

HansBug在一本英语书里面找到了一个单词表，包含N个单词（每个单词内包含大小写字母）。现在他想要找出某一段连续的单词内字典序最大的单词。

如果遇到相同的字符串，输出后面的。

### 输入描述

```
第一行包含两个正整数N、M，分别表示单词个数和询问个数。

接下来N行每行包含一个字符串，仅包含大小写字母，长度不超过15，表示一个单词。

再接下来M行每行包含两个整数x、y，表示求从第x到第y个单词中字典序最大的单词。
```
### 输出描述

```
输出包含M行，每行为一个字符串，分别依次对应前面M个询问的结果。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 5
absi
hansbug
lzn
kkk
yyy
1 5
1 1
1 2
2 3
4 4
```
```
yyy
absi
hansbug
lzn
kkk
```
```
第一次操作：在{absi,hansbug,lzn,kkk,yyy}中找出字典序最大的，故为yyy

第二次操作：在{absi}中找出字典序最大的，故为absi

第三次操作：在{absi,hansbug}中找出字典序最大的，故为hansbug

第四次操作：在{hansbug,lzn}中找出字典序最大的，故为lzn

第五次操作：在{kkk}中找出字典序最大的，故为kkk
```

### 题目来源  
`luogu.com.cn`