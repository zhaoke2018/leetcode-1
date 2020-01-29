
- 矩阵中数值为0的地方可以走,为1的地方不能走,问有多少种走法. 
  - https://leetcode.com/problems/unique-paths-ii/

```py
def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    
    # 既是初始化,也是一小段一维dp.
    dp = [[0 for i in xrange(col)] for j in xrange(row)]
    dp[0][0] = 1
    for i in xrange(1, row):
        dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0 # 必须有else部分,否则就报错!
    for j in xrange(1, col):
        dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
    
    for i in xrange(1, row):
        for j in xrange(1, col):
            if obstacleGrid[i][j] == 1: # 被1挡住的地方,dp清空即可.
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] # 一开始不知道如何初始化,然后陷在这里,不知道该如何处理i为0时的数组越界问题: i-1 为-1
                
    return dp[-1][-1]
```
