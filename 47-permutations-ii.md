

```py
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, new_order, res):
            if not nums:
                res.add(tuple(new_order)) # 如果 nums 空了, 那么 new_order 就满了, 可以存了
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], new_order+[nums[i]], res)
        
        res = set()
        dfs(nums, [], res) # 计算 res
            
        return list(res)
```