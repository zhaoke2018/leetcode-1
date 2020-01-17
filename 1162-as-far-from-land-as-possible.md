


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

