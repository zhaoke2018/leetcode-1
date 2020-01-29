
- 起跳花费为cost[i].先cost后跳.每次可以跳1-2级.求最小总花费 https://leetcode.com/problems/min-cost-climbing-stairs/
  - `解析`: 既然求最小花费, 那么肯定是多路选其一了, 每次起跳两种方式不就是多路吗? 每次选择最小的不就是花费最小吗?
  - 像这种有两种选择的, 很显然就是dp, 并且一个 min/max 就搞定了.
  - 状态: dp[i] 当前的最小花费
    - dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
  - 边界条件: 为什么计算的长度要+1? 最后一级也要跨越.所以自然要n+1.



```py
def minCostClimbingStairs(cost):
    # dp[i]: 到i级的最小成本
    for i in range(len(cost) + 1):
        dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
```
