- [Intro](#intro)

## Intro

- https://leetcode.com/problems/climbing-stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


- 每次要么跳一步, 要么跳两步, 求一共有多少爬梯方式 https://leetcode.com/problems/climbing-stairs/
  - `解析` 发现这种有多路选择的, 立马想到动态规划
  - 状态: dp[i] 为当前的爬梯方式数
    - dp[i] = dp[i-1] + dp[i-2]

```py
def climbStairs(self, n):
    dp = [i for i in xrange(n+1)] # 亮点: n最小值为1,为了方便返回值,数组也从1开始.
    for i in xrange(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] # dp[i]: 到达第i级的爬梯方式.要么爬一级过来的,要么爬两级.
    return dp[-1]
```



