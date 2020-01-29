


- https://leetcode.com/problems/minimum-falling-path-sum/
  - 设dp[i][j]为每一步的最小和,则 `minSum = dp[i][j] + min(A[i+1][j-1], A[i+1][j], A[i+1][j+1])`

