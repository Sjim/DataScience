### 题目描述
给定数字N，请打印所有数字，这些数字是N的二进制表示形式的按位子集。数字N的按位子集将是0满足以下条件的i： N＆i == i
### 输入描述
输入的第一行包含一个整数T，表示测试用例的数量。对于每个测试用例，都有一个整数N表示数字。
### 输出描述
对于每个测试用例，输出是满足上述条件的以空格分隔的整数。
### 输入范例
```
2
5
9
```
### 输出范例
```
5 4 1 0
9 8 1 0
```
对于第一个测试用例： 

0＆5 = 0 

1＆5 = 1 

2＆5 = 0 

3＆5 = 1 

4＆5 = 4 

5＆5 = 5
### 题目来源
geeksforgeeks.org
