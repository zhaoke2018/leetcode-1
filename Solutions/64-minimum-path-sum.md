- [Intro](#intro)

## Intro

- https://leetcode.com/problems/minimum-path-sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.






## 知识总结

解题思路
1. 确定dp关系(很经典) grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
1. 处理边角,因为i-1有溢出风险,于是循环的时候从1开始.




```py
from typing import List, Tuple, Dict, TextIO # 还是需要导入哦

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j] # tip: i=0时,数组会越界!那从1开始计算不就行了
        # print(grid)
        return grid[-1][-1]

xx = Solution()
pa = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
res = xx.minPathSum(pa)
print(res)
```

## xxx



- 给定一个矩形表格，每个格子有一个权值,求从左上到右下的权值和最小 
  - https://leetcode.com/problems/minimum-path-sum/

```py
def minPathSum(self, grid: List[List[int]]) -> int:
    # 本题不用新建dp数组了, 直接在原数组上操作就行了.
    row, col = len(grid), len(grid[0])

    # 初始化两条边
    for i in range(1, row):
        grid[i][0] += grid[i-1][0]
    for i in range(1, col):
        grid[0][i] += grid[0][i-1]
    
    # 计算剩余的边
    for i in range(1, row):
        for j in range(1, col):
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j] # 每个格子有两个来源,从里面选一个最小的继续往下走就行了.

    return grid[-1][-1]
```