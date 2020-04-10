- [Intro](#intro)
- [Topics](#topics)
- [Array](#array)
- [模拟加法](#%e6%a8%a1%e6%8b%9f%e5%8a%a0%e6%b3%95)

## Intro

- https://leetcode.com/problems/plus-one

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


## Topics

- `Array`


## Array

- Python join 只能处理字符串, 所以这里需要先把 int 转换成 str



```py
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_int = int("".join([str(i) for i in digits])) + 1
        return [int(i) for i in str(digits_int)]
```


- [与本题无关] reversed 返回的结果为什么是个对象.
  - reversed 之后是个数组, 需要join 才能变成字符串

```py
ss = "apple"
ss = ''.join(reversed(ss))
```


## 模拟加法

```py
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] <= 9:
                return digits # normal situation, return
            digits[i] = 0
        # 如果一直进位到比原数组还要长
        res = [0 for i in range(len(digits)+1)]
        res[0] = 1
        return res
```

