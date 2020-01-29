


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