

```py
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, con):
            if sum(nums) == target:
                res.add(tuple(sorted(nums)))
            for num in candidates:
                if con - num >= 0:
                    dfs(nums+[num], con-num)
        
        res = set()
        dfs([], target)
        return list(res)

sol = Solution().combinationSum([2,3,6,7], 7)
print(sol)
```