








- https://leetcode.com/problems/sort-colors/


## Count


直接统计三种颜色的数量, 然后重写原数组

```py
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = collections.Counter(nums)
        
        step = 0
        for i in range(count[0]):
            nums[step] = 0
            step += 1
        for i in range(count[1]):
            nums[step] = 1
            step += 1
        for i in range(count[2]):
            nums[step] = 2
            step += 1

```