- [Intro](#intro)
- [Topics](#topics)
- [Recursion](#recursion)
- [DFS Emitter By John](#dfs-emitter-by-john)

## Intro

- https://leetcode.com/problems/combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]





## Topics

- `Backtracking`


## Recursion

用caikehe的 抽数法 也可以吧！


- 从1~n中,找出所有的k个数组合 https://leetcode.com/problems/combinations/


- Python 知识点



- [] Complexity
- 不知道



```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(arr, inter, index):
            if len(inter) == k:
                res.append(inter)
            for i in range(index, len(arr)):
                dfs(arr, inter+[arr[i]], 1+i) # 每次都从前往后找, 就不用去重了, 因此也就不用set转来转去了.
        
        res = []
        arr = [i+1 for i in range(n)]
        dfs(arr, [], 0)
        return res
```





## DFS Emitter By John



```py
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(arr, inter, index):
            if len(inter) == k:
                res.append(inter)
            for i in range(index, len(arr)):
                dfs(arr, inter+[arr[i]], 1+i) # 每次都从前往后找, 就不用去重了, 因此也就不用set转来转去了.
        
        res = []
        arr = [i+1 for i in range(n)]
        dfs(arr, [], 0)
        return res
        
sol = Solution().combine(4, 2)
print(sol)
```