- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/power-of-four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example 1:

Input: 16
Output: true


Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?

## Topics

- `Bit Manipulation`


## Bit

- [方法] 通过列举数字, 看出规律 https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
  - 但是这句判断的话, 还是很精妙

```py
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num != 0 and num & (num-1) == 0 and num & 1431655765 == num
```