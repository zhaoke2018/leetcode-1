- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/add-binary

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


## Topics

- `Math`
- `String`


## Bit


```py
def addBinary(a: str, b: str) -> str:
    sum = []
    carry = 0
    length = max(len(a), len(b))
    reverse_a = reversed(a)
    reverse_b = reversed(b)

    for i in range(length):
        sum[i] = reverse_a[i] ^ reverse_b[i]
        if carry:
            # TODO 这里需要两个 carry 才行啊, 一个用来代表之前产生的进位, 一个用来代表当前两位产生的进位
            carry = reverse_a[i] & reverse_b[i]

    # TODO reverse sum and join.('')
    return reversed(sum.join(''))
```




