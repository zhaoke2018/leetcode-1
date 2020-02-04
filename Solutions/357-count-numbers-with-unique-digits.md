- [Intro](#intro)

## Intro

- https://leetcode.com/problems/count-numbers-with-unique-digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99





## Topics

- `Math`
- `Dynamic Programming`
- `Backtracking`


## Math


```py
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n: return 1

        res = 10
        count = 9
        for i in range(2, n+1):
            count *= (11-i)
            res += count
        return res
```



- https://www.cnblogs.com/grandyang/p/5582633.html







