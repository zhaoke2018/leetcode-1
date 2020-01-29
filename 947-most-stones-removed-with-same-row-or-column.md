





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











