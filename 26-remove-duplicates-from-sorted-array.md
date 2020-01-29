
- 去掉 sorted array 中的重复元素 https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- [Two_Pointers] slow节点控制所有需要的元素, fast节点去筛选unique元素.


```py
# 这样会超时!
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        fast = slow = 0
        count = 1
        for i in range(len(nums)):
            slow = fast = i # 一开始都是0

            # fast 去找一个新元素
            while fast<len(nums) and nums[slow] >= nums[fast]: # slow 守着重复的元素, fast 去找下一个
                fast += 1
            print('new ele index', fast)
            # while loop finished, found new unique

            # 找到了, 把新元素拿过来
            if fast<len(nums) and nums[fast] > nums[slow]:
                nums[slow+1], nums[fast] = nums[fast], nums[slow+1]
                slow += 1
                count += 1

            if fast == len(nums):
                break
        return count
```



