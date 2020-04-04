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

- 这里的 1 和 0 相当于两个背包, 他们的个数相当于背包的容量.

- [WHY] 背包问题使用 bottom-up 可以二维变一维.
- [WHY] 为什么要逆序遍历
  - 如果正序反倒会出错, 这也太奇葩了.
- 等等, 这个逆序不就是 bottom-up 吗?
  - https://leetcode.com/problems/ones-and-zeroes/discuss/121876/C++-DP-Knapsack-Approach
  


```py
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp = [[0] * (n+1)] * (m+1) # shallow copy, 遗患无穷!
        dp = [[0] * (n+1) for _ in range(m+1)] # dp[i][j] 表示i个0,j个1最多可以构成多少个字符串 # m:0

        for ss in strs:
            # 统计每个字符串中, zero one 出现的次数
            counter = collections.Counter(ss)
            count_zero = counter['0']
            count_one = counter['1']
            
            # 从最大空间 到最小空间
            for zz in range(m, count_zero-1, -1): # Backwards iteration
                for oo in range(n, count_one-1, -1):
            # for zz in range(count_zero, m+1): # Backwards iteration
            #     for oo in range(count_one, n+1):
                    dp[zz][oo] = max(dp[zz][oo], dp[zz - count_zero][oo - count_one] + 1)

        return dp[m][n]
```




