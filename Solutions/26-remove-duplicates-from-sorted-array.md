- [Intro](#intro)

## Intro

- https://leetcode.com/problems/remove-duplicates-from-sorted-array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}



## xxx


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

## two pointers

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


