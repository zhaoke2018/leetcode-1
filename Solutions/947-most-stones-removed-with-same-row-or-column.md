- [Intro](#intro)

## Intro

- https://leetcode.com/problems/most-stones-removed-with-same-row-or-column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?
 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5


Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3


Example 3:

Input: stones = [[0,0]]
Output: 0

 
Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000










## Intro


- 输入一系列石头的坐标, 如果某石头的同行or同列有石头, 那么它就可以被移除, 问最多可以移除多少石头? https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


## BFS by Wangchen

- https://buptwc.com/2018/11/25/Leetcode-947-Most-Stones-Removed-with-Same-Row-or-Column/


```py
class Solution(object):
    def removeStones(self, stones):
        stones = list(map(tuple, stones))
        s = set(stones)
        d = collections.defaultdict(list)
        for i,j in s:
            d[i].append(j)
            d[j].append(i)
        
        def dfs(i,j):
            for y in d[i]:
                if (i,y) not in s: continue
                s.remove((i,y))
                dfs(i,y)
            for x in d[j]:
                if (x,j) not in s: continue
                s.remove((x,j))
                dfs(x,j)
        
        n = len(s)
        res = 0
        for i,j in stones:
            if (i,j) not in s: continue
            s.remove((i,j))
            dfs(i,j)
            # n表示遍历之前集合s的长度
            # n-len(s)则表明这次dfs遍历的石头总数
            res += n - len(s) - 1
            n = len(s)
        return res

```











