




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


