

```py
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, mid, res):
            if not nums:
                res.append(mid) # 如果 nums 空了, 那么 mid 就满了, 可以存了
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], mid+[nums[i]], res)
        
        res = []
        dfs(nums, [], res) # 计算 res
        return res

sol = Solution().permute([1, 2, 3])
print(sol)
```