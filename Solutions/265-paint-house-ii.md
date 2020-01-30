- [Intro](#intro)

## Intro

- https://leetcode.com/problems/paint-house-ii



## DP

- 用k种油漆涂房子, 每栋房子&每种油漆的花费各不一样, 要求相邻的房子颜色不一, 求最少花费
  - https://www.lintcode.com/problem/paint-house-ii/description
  - https://leetcode.com/problems/paint-house-ii/


- [DP思路] 跟 paint house i 一样, 只需要循环遍历即可. 仍然是二维数组, 两层循环.



- 按理说, 这样处理应该可以, 也通过了几个 case, 但是没有完全提交成功

```py
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0

        # 将每栋房子的3种涂色方案都记录下来, 最后比较最小的
        dp = costs # 状态划分: 前i栋房子的最小花费, 房子i的颜色为j
        plen = len(costs[0])
        for i in range(1, len(costs)):
            for j in range(plen):
                p1 = (j + 1) % plen
                p2 = (j + 2) % plen
                if plen > 2:
                    if j != p1 and j != p2: # 保证与前者不是同一种颜色
                        dp[i][j] += min(dp[i - 1][p1], dp[i - 1][p2]) # 前一个房子有两种颜色方案, 选花费小的
                elif plen == 2:
                    dp[i][j] += dp[i - 1][p1] # 前一个房子有两种颜色方案, 选花费小的

        return min(dp[-1])
```