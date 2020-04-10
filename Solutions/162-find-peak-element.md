- [Intro](#intro)
- [Topics](#topics)
- [Linear](#linear)

## Intro

- https://leetcode.com/problems/find-peak-element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.


## Topics

- `Array`
- `Binary Search`


## Linear

```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: # 技巧, 只需要判断一侧即可!!!
                return i
        return len(nums) - 1
```