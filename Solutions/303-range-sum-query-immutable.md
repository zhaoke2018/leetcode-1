- [Intro](#intro)

## Intro

- https://leetcode.com/problems/range-sum-query-immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

You may assume that the array does not change.
There are many calls to sumRange function.




## DP

- https://leetcode.com/problems/range-sum-query-immutable/ easy
  - 求区间和.由于需要多次调用区间和函数,所以必须把计算结果缓存好,然后每次只需要调用结果就行.
  - dp[i]表示[0,i]区间的和,则区间[i,j]调用函数直接返回dp[j]-dp[i]即可.
- https://leetcode.com/problems/range-sum-query-immutable/ easy
  - 求区间和.由于需要多次调用区间和函数,所以必须把计算结果缓存好,然后每次只需要调用结果就行.
  - dp[i]表示[0,i]区间的和,则区间[i,j]调用函数直接返回dp[j]-dp[i]即可.