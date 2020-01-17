
- 这道题虽然有个 two pointers 的标签, 但是一个 pointer 就可以完成, 而且效率应该不比 two pointers 低.

TODO
- Two Pointers 的解法好在哪里?


```py
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i=0
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
            i += 1
        print(nums)
        return len(nums)

sol = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(sol)
```