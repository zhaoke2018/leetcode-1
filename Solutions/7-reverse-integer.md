- [Intro](#intro)
- [Topics](#topics)
- [Math](#math)

## Intro

- https://leetcode.com/problems/reverse-integer

Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


## Topics

- `Math`


## Math


- 解决溢出问题有两个思路
- [思路] 通过字符串转换加try catch的方式来解决.
  - 由于字符串转换的效率较低且使用较多库函数，所以解题方案不考虑该方法，而是通过数学计算来解决。
- [思路] 通过数学计算来解决。
  - 通过循环将数字x的每一位拆开，在计算新值时每一步都判断是否溢出。




- https://leetcode-cn.com/problems/reverse-integer/solution/hua-jie-suan-fa-7-zheng-shu-fan-zhuan-by-guanpengc/