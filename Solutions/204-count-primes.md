- [Intro](#intro)

## Intro

- https://leetcode.com/problems/count-primes

Count the number of prime numbers less than a non-negative number, n.
Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.





## Topics

- `Hash Table`
- `Math`


## Math
- https://leetcode.com/problems/count-primes/ easy/math
  - 试除法: 循环一遍,能够被整除的就排除,可以不断缩小除数/被除数的范围来优化.
  - 筛选法: 2到sqrt(n),把这些倍数筛掉,剩下的就是素数了.
  - 数学法: 如果要求前N个素数的话,就需要用素数分布定理来判断除数的范围了.
  - https://program-think.blogspot.com/2011/12/prime-algorithm-1.html 求质数算法的 N 种境界


```py
def countPrimes(self, n):
    count = 0
    primeList = []
    for i in xrange(2, n):
        if self.isPrime_iterate(i, primeList):
            count += 1
            primeList.append(i)
    return count

# 只考虑2357是不够的.只有当n不能被[2,n-1]的时候,才是素数.
# [缩小被除数范围] 由于因数是一大一小成对出现的,所以被除数考虑[2, sqrt(n)]就可以了.
# [缩小除数范围] 除数为偶数的肯定不用考虑,因为他们能被2整除,肯定不是素数.
# [进一步缩小被除数范围] 当我们求101是否为素数时,只需要考虑[2, 10], 但是9并不需要被除,因为它的因数已经被考虑了.因此我们可以将被除数进一步缩小到“已经求出的素数”,即将之前算出的素数都保存起来,以空间换时间.
def isPrime_iterate(self, n, primeList):
    sqrtn = sqrt(n)
    for j in primeList:
        if j < sqrtn and (n % 2 == 0 or n % j == 0) and n != j:
            return False
    return True

def isPrime_filter(self, n):
    return True
```




- https://leetcode.com/problems/ugly-number/ math
- https://leetcode.com/problems/ugly-number-ii/ math/dp/heap
- https://leetcode.com/problems/super-ugly-number/ math/heap








- https://leetcode.com/problems/count-primes/ easy/math
  - 试除法: 循环一遍,能够被整除的就排除,可以不断缩小除数/被除数的范围来优化.
  - 筛选法: 2到sqrt(n),把这些倍数筛掉,剩下的就是素数了.
  - 数学法: 如果要求前N个素数的话,就需要用素数分布定理来判断除数的范围了.
  - https://program-think.blogspot.com/2011/12/prime-algorithm-1.html 求质数算法的 N 种境界


```py
def countPrimes(self, n):
    count = 0
    primeList = []
    for i in xrange(2, n):
        if self.isPrime_iterate(i, primeList):
            count += 1
            primeList.append(i)
    return count

# 只考虑2357是不够的.只有当n不能被[2,n-1]的时候,才是素数.
# [缩小被除数范围] 由于因数是一大一小成对出现的,所以被除数考虑[2, sqrt(n)]就可以了.
# [缩小除数范围] 除数为偶数的肯定不用考虑,因为他们能被2整除,肯定不是素数.
# [进一步缩小被除数范围] 当我们求101是否为素数时,只需要考虑[2, 10], 但是9并不需要被除,因为它的因数已经被考虑了.因此我们可以将被除数进一步缩小到“已经求出的素数”,即将之前算出的素数都保存起来,以空间换时间.
def isPrime_iterate(self, n, primeList):
    sqrtn = sqrt(n)
    for j in primeList:
        if j < sqrtn and (n % 2 == 0 or n % j == 0) and n != j:
            return False
    return True

def isPrime_filter(self, n):
    return True
```




- https://leetcode.com/problems/ugly-number/ math
- https://leetcode.com/problems/ugly-number-ii/ math/dp/heap
- https://leetcode.com/problems/super-ugly-number/ math/heap







