- [Intro](#intro)
- [Topics](#topics)
- [Math](#math)

## Intro

- https://leetcode.com/problems/number-of-digit-one

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.



## Topics

- `Math`


## Math

- [思路] 考虑每一位上可能会出现多少个1, 比如 1234, 对于 十位, 个位上是4, 那么就会出现4次1 -- 11,12,13,14.
- [推理] 画个图就很清晰了 https://www.cnblogs.com/grandyang/p/4629032.html
- 本题主要考逻辑, 而不是代码编写.

```py
class Solution:
    def countDigitOne(self, n: int) -> int:
        ones, m = 0, 1 # m will be 1, 10, 100, 1000
        while m <= n:
            # 1xxx, 这个1将会出现xxx次
            ones += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones
```
