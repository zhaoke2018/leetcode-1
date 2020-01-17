



## Intro

- https://leetcode.com/problems/max-area-of-island/


总结
- [代码技巧] `if then 递归()`, 不如改成 `递归 then if`, 这样可以省去多个 if.
- [审题误区] 很多二维坐标的题根本不是 N*N !
- [审题误区] 有些题说明了 non-empty, 就不用考虑 None 了.


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











