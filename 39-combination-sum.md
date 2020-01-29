

- https://leetcode.com/problems/combination-sum/ backtracking/medium
  - 从C数组里,找出所有和为T的组合,每个数字可以用多次.比如C中只有一个2,但是你可以在solution里面用2次2.







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