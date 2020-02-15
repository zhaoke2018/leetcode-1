- [Intro](#intro)
- [Topics](#topics)
- [Monotonous](#monotonous)
- [Brute Force](#brute-force)

## Intro

- https://leetcode.com/problems/next-greater-element-i


You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2. 


The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:

All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.



## Topics

- `Stack - Monotonous`

## Monotonous

- Labuladong https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/


```py
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈的思路如何理解?
```




## Brute Force

- faster than 5%, 太可怜了!
- Time O(N^2)


```py
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for key in nums1:
            index = -1
            for jj in range(len(nums2)):
                # 找到下标
                if key == nums2[jj]:
                    index = jj
                
                # 找到下标之后, 开始找更大的数
                if index != -1 and nums2[jj] > nums2[index]:
                    res.append(nums2[jj])
                    break
                
                # 找到最后也没找到
                if jj == len(nums2)-1 and nums2[jj] <= nums2[index]:
                    res.append(-1)
                
        return res
```