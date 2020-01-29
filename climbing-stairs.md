
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



