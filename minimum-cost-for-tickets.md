

- https://leetcode.com/problems/minimum-cost-for-tickets
  - 设dp[i]为第i天最低花费,那么 `minCost = min(dp[i-1] + cost[0], dp[i-7] + cost[1], dp[i-30] + cost[2])`
  - https://leetcode.com/problems/minimum-cost-for-tickets/solution/ 官方solution的解法好像不一样...

