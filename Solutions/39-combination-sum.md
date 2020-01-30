- [Intro](#intro)

## Intro

- https://leetcode.com/problems/combination-sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]




## Recursion

- 从C数组里,找出所有和为T的组合,每个数字可以用多次.比如C中只有一个2,但是你可以在solution里面用2次2.



```py
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, con):
            if sum(nums) == target:
                res.add(tuple(sorted(nums)))
            for num in candidates:
                if con - num >= 0:
                    dfs(nums+[num], con-num)
        
        res = set()
        dfs([], target)
        return list(res)

sol = Solution().combinationSum([2,3,6,7], 7)
print(sol)
```