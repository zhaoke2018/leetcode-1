- [Intro](#intro)

## Intro

- https://leetcode.com/problems/permutations

Given a collection of distinct integers, return all possible permutations.
Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]





## Topics

- `Backtracking`


## Recursion

- 求 全排列 https://leetcode.com/problems/permutations/
  - 大概就是不断加元素, 如果数量够了, 就是一个新组合.
  - 思路: 每次从 nums 中取出一个数, 放到 new_order 中, 当 nums 取空了, 那 new_order 就是我们要找的 permutation 了.
- follow-up: 给定的数组中有重复数字, 因此会涉及到一个去重, 但是思路完全一样 https://leetcode.com/problems/permutations-ii/


- [] 如何想到这个思路?
- 既然重新排列, 那么就要有一个打乱的过程.


- [] 复杂度如何?


- Python 知识点
1. list 可以直接用 + 拼接


```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, new_order, res):
            if not nums:
                res.append(new_order) # 如果 nums 空了, 那么 new_order 就满了, 可以存了
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], new_order+[nums[i]], res)
        
        res = []
        dfs(nums, [], res) # 计算 res
        return res
```







- 求 全排列 https://leetcode.com/problems/permutations/
  - 大概就是不断加元素, 如果数量够了, 就是一个新组合.
  - 思路: 每次从 nums 中取出一个数, 放到 new_order 中, 当 nums 取空了, 那 new_order 就是我们要找的 permutation 了.
- follow-up: 给定的数组中有重复数字, 因此会涉及到一个去重, 但是思路完全一样 https://leetcode.com/problems/permutations-ii/


- [] 如何想到这个思路?
- 既然重新排列, 那么就要有一个打乱的过程.


- [] 复杂度如何?


- Python 知识点
1. list 可以直接用 + 拼接


```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, new_order, res):
            if not nums:
                res.append(new_order) # 如果 nums 空了, 那么 new_order 就满了, 可以存了
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], new_order+[nums[i]], res)
        
        res = []
        dfs(nums, [], res) # 计算 res
        return res
```

