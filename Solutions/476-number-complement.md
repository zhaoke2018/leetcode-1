- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/number-complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.



## Topics

- `Bit Manipulation`


## Bit

- 取反很简单,与 1111 异或就可以了.
- `经验` 本题的关键是, 如何获取到跟 num 长度一样的 1.

```py
def findComplement(self, num):
    # 得到与num同长度的1111...
    counter = 1
    while counter <= num:
        counter = counter << 1

    # 减一之后正好变成全一,然后异或就 flip 了
    flipy =  counter - 1 ^ num
    return flipy
``` 
