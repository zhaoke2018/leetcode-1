



- 用三种油漆涂房子, 每栋房子&每种油漆的花费各不一样, 要求相邻的房子颜色不一, 求最少花费 https://leetcode.com/problems/paint-house/
  - `cost[house][paint]` 表示刷某个 house 为某种 paint 的费用.
  - Lintcode也有类似的题 https://www.lintcode.com/problem/paint-house/description


- [思路] 对于所有的 house 以及所有的 paint, 将总花费都记录下来, 最后对比.


```py
# 伪代码
def minCost(self, costs):
    if not costs or not costs[0]: return 0

    # 将每栋房子的3种涂色方案都记录下来, 最后比较最小的
    dp = costs # 状态划分: 前i栋房子的最小花费, 房子i的颜色为j

    for i in range(1, len(costs)):
        for j in range(3):
            dp[i][j] += min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) # 前一个房子有两种颜色方案, 选花费小的

    return min(dp[-1][0], dp[-1][1], dp[-1][2])

# 伪代码 这样写逻辑更清晰
for i in range(len(costs)):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]) # 前一个房子有两种颜色方案, 选花费小的
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]) 
    dp[i][2] += min(dp[i - 1][1], dp[i - 1][0]) 
```

