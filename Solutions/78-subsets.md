- [Intro](#intro)
- [Topics](#topics)
- [Append](#append)

## Intro

- https://leetcode.com/problems/subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


## Topics

- `Array`
- `Backtracking`
- `Bit Manipulation`
- `Multiple Methods`



## Append

```py
def subsets(self, nums):
    res = [[]]
    for i in nums:
        res += [item+[i] for item in res]
    return res
```