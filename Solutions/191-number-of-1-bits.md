- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/number-of-1-bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
 
Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 
Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

 
Follow up:
If this function is called many times, how would you optimize it?


## Topics

- `Bit Manipulation`


## Bit



```py
# 循环法 逐步与1做and操作
# 大致思想就是这样了,但是目前还有bug,应该是python不熟的原因
def hammingWeight(n):
    mask = 1
    count = 0
    for i in xrange(32):
        if n & mask != 0:
            count += 1
        mask <<= 1 # 左移并不只是<<噢!
    return count

# 位运算法 10000 & 10000-1 = 0,这样就清除了后5位,依次清除就可以得到所有1了.
# accepted 但是 faster than 8%
def hammingWeight_bitwise(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count
```





