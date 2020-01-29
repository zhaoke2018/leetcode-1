
- 将字符串解码成数字,有多少种方式?其中*可以匹配任意数字 https://leetcode.com/problems/decode-ways-ii
  - 为什么上一题都是加法, 而这里确是除法, 究竟是什么区别
    - 为什么同样是分支,之前那个不是 *2 呢?


```py
def numDecodings(S):
    MOD = 10**9 + 7 
    e0, e1, e2 = 1, 0, 0
    for c in S:
        if c == '*':
            f0 = 9*e0 + 9*e1 + 6*e2
            f1 = e0
            f2 = e0
        else:
            f0 = (c > '0') * e0 + e1 + (c < = '6') * e2
            f1 = (c == '1') * e0
            f2 = (c == '2') * e0
        e0, e1, e2 = f0 % MOD, f1, f2
    return e0
```




