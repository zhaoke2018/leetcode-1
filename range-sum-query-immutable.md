
- https://leetcode.com/problems/range-sum-query-immutable/ easy
  - 求区间和.由于需要多次调用区间和函数,所以必须把计算结果缓存好,然后每次只需要调用结果就行.
  - dp[i]表示[0,i]区间的和,则区间[i,j]调用函数直接返回dp[j]-dp[i]即可.