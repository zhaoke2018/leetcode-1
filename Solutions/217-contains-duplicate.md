- [Intro](#intro)

## Intro

- https://leetcode.com/problems/contains-duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true



## Intro

- https://leetcode.com/problems/contains-duplicate/



## 知识总结

- 实在是太简单了,没什么可总结的.
- [思路]


由于使用cache
空间复杂度 O(n)
时间复杂度 O(n)



```py

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = dict()
        for i in nums:
            if i in cache:
                return True
            else:
                cache[i] = 1
        return False
```