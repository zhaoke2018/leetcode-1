- [Intro](#intro)

## Intro

- https://leetcode.com/problems/max-area-of-island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.




## Intro

- https://leetcode.com/problems/max-area-of-island/


总结
- [代码技巧] `if then 递归()`, 不如改成 `递归 then if`, 这样可以省去多个 if.
- [审题误区] 很多二维坐标的题根本不是 N*N !
- [审题误区] 有些题说明了 non-empty, 就不用考虑 None 了.



## Topics

- `Array`
- `Depth-first Search`


## DFS by John


```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def expand(i, j):
            if not (0<=i<N and 0<=j<M) or visited[i][j] or not grid[i][j]:
                return 0
            visited[i][j] = 1
            print('当前expand坐标', i, j)
            # 将无数个if改成下一个递归首判断
            return 1+expand(i+1, j) + expand(i-1, j) + expand(i, j-1) + expand(i, j+1)
                
        N = len(grid)
        M = len(grid[0])
        maxi = 0
        visited = [[0 for i in range(M)] for j in range(N)]
        
        for i in range(N):
            for j in range(M):
                this_island = expand(i, j)
                if this_island:
                    print('this island', this_island)
                maxi = max(maxi, this_island)
        return maxi
```











