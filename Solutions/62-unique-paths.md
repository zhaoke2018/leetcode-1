- [Intro](#intro)

## Intro

- https://leetcode.com/problems/unique-paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?
Note: m and n will be at most 100.
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28




## Topics

- `Array`
- `Dynamic Programming`


## DP
- 在一个mxn的矩阵中,要从左上角走到右下角,只能往下或者往右移动,一共有多少个unique path. 
  - https://leetcode.com/problems/unique-paths/
  - 每个状态无非拆成从左边来 or 从上面来.

```py
def uniquePaths(self, m, n):
    dp = [[1 for i in xrange(n)] for i in xrange(m)] # 二维数组的i是行数,是纵坐标,然而python的这个初始化有点颠倒,所以就先n再m

    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
```

- follow-up 用一维数组记录dp.
  - 应该跟一维dp可以优化为两个变量的思想类似吧.
  - 其实是因为ij不参与计算,只作遍历,所以可以压缩为一维.

```py
def uniquePath_1d():
    for i in xrange(m):
        for j in xrange(n):
            dp[j] += dp[j-1] # 因为ij不参与计算,只承担遍历功能,所以可以这样压缩.
```

- 在一个mxn的矩阵中,要从左上角走到右下角,只能往下或者往右移动,一共有多少个unique path. 
  - https://leetcode.com/problems/unique-paths/
  - 每个状态无非拆成从左边来 or 从上面来.

```py
def uniquePaths(self, m, n):
    dp = [[1 for i in xrange(n)] for i in xrange(m)] # 二维数组的i是行数,是纵坐标,然而python的这个初始化有点颠倒,所以就先n再m

    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
```

- follow-up 用一维数组记录dp.
  - 应该跟一维dp可以优化为两个变量的思想类似吧.
  - 其实是因为ij不参与计算,只作遍历,所以可以压缩为一维.

```py
def uniquePath_1d():
    for i in xrange(m):
        for j in xrange(n):
            dp[j] += dp[j-1] # 因为ij不参与计算,只承担遍历功能,所以可以这样压缩.
```
