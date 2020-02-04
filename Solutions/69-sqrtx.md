- [Intro](#intro)
- [Math](#math)

## Intro

- https://leetcode.com/problems/sqrtx

Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.









## Topics

- `Math`
- `Binary Search`


## Math

- https://leetcode.com/problems/sqrtx/
  - 保留精度就不算是follow-up了,直接当作基本要求吧!
  - 牛顿迭代法解释 http://www.matrix67.com/blog/archives/361



```py
# 最土的方法,遍历
# 从小到大遍历,总能找到
def sqrt(x):
    for i in xrange(1, x/2+2):
        if i*i == x:
            return i
        elif i*i > x:
            return i-1

# 最普适的高效方法,二分法
def sqrt_binary(x):
    pass

# 最好的特异方法,牛顿迭代法
# y=x^2 无非就是一个幂函数,本题的目的就是求函数的横坐标x而已.而牛顿迭代法就是用切线不断逼近.
def sqrt_newton(x):
    pass
```


