- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/single-number-ii

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99


## Topics

- `Bit Manipulation`


## Bit



```py
def singleNumberII_bitwise(self, nums: List[int]) -> int:
    res = 0
    for i in nums:
        res = res & nums ^ nums
    return res
```




```py
# Math version
def singleNumberII_math(self, nums):
    res = set(nums)
    res = sum(res)*3 - sum(nums) # 这样一来,就把所有出现3次的数字都减掉了
    res = res/2 # python3中的除法是精确除, 返回的是浮点数!!!
    return res
```

