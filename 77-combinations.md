

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