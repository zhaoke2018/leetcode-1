- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/hamming-distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.



## Topics

- `Bit Manipulation`
- `Bit Manipulation - XOR`


## Bit


- 这不就是典型的 XOR 吗! 不能更典型了.
- `经验` binary 就可以直接遍历,不用转换为字符串!
- `经验` binary.count('1')可以直接统计,不用遍历!!!

```py
def hammingDistance(self, x, y):
    xor_res = x ^ y
    xor_res_str = str(bin(xor_res)) # XOR 后转换为二进制字符串,方便遍历

    # 事实上,以下这段可以直接用一个系统函数解决 👇
    # distance = xor_res_str.count('1')
    distance = 0
    for i in xor_res_str:
        if i == '1':
            distance += 1
            
    return distance
```