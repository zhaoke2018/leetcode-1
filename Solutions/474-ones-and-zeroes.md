- [Intro](#intro)
- [Topics](#topics)
- [Dynamic Programming - Knapsack - 二维费用问题](#dynamic-programming---knapsack---%e4%ba%8c%e7%bb%b4%e8%b4%b9%e7%94%a8%e9%97%ae%e9%a2%98)

## Intro

- https://leetcode.com/problems/ones-and-zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.
Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.
Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

 
Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

 
Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

 






## Topics

- `Dynamic Programming - Knapsack - 二维费用问题`


## Dynamic Programming - Knapsack - 二维费用问题

- 给你m个0,n个1,还有一个字符串数组.看你能拼出多少个array里面的字符串,返回总数.(这些0和1都只能用一次) 

- 转化:物品ith的二维费用问题 (并不是限定使用次数的多重背包问题)









