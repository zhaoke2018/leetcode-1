- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/single-number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4



## Topics

- `Hash Table` 统计一下就出来了.
- `Bit Manipulation` 比较精巧, 推广性不大
  - https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
- `Math` 对于只有一个例外的, 相乘再相减



## Bit







- 异或, 使所有成对的数字都湮灭.
- `n^0=n` 初始化为0, 可以保证第一个数字是他本身.
- [WHY] 不太懂为什么可以一锅炖, 需要继续研究一下.


```py
def singleNumber(self, nums):
    res = 0
    for i in nums:
        res = res ^ i # 0 ^ n = n
    return res
```