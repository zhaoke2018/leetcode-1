- [Intro](#intro)

## Intro

- https://leetcode.com/problems/as-far-from-land-as-possible

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
If no land or water exists in the grid, return -1.
 
Example 1:


Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:


Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

 
Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1




- https://leetcode.com/problems/as-far-from-land-as-possible/


```py
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def expand(i, j, step):
            if i+1 < N and grid[i+1][j] == 0:
                grid[i+1][j] = step
                Q.append((i+1, j))
            if i-1 >= 0 and grid[i-1][j] == 0:
                grid[i-1][j] = step
                Q.append((i-1, j))
            if j+1 < N and grid[i][j+1] == 0:
                grid[i][j+1] = step
                Q.append((i, j+1))
            if j-1 >= 0 and grid[i][j-1] == 0:
                grid[i][j-1] = step
                Q.append((i, j-1))
        
        # 有了队列, 就可以不用全盘遍历了, 比递归优越
        
        Q = collections.deque([])
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    Q.append((i, j))
        
        step = 0
        
        while Q:
            level = len(Q)
            step += 1
            for k in range(level):
                q = Q.popleft()
                expand(q[0], q[1], step)
                
        return step-1 if step != 1 else -1 # 因为最后一个节点也会执行一次 入队出队, 因此要减去这个.
```



## Topics

- `Breadth-first Search`
- `Graph`


