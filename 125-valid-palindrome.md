

## Intro

- 忽视大小写与空格与标点(只考虑数字和字母),检测字符串是否回文 https://leetcode.com/problems/valid-palindrome/ twoPointers/easy
- [分析] Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
  - [要求1] 回文验证
  - [要求2] 过滤掉非字母, 过滤大小写.




## Two Pointers

```py
import re
def isPalindrome(self, s):
    s = s.lower()
    s = re.sub(r'[^\w]|\s', '', s) # 正则去掉所有 ^\w 与 \s
    print s

    leng = len(s)
    for i in xrange(leng / 2):
        if s[i] != s[leng-i-1]:
            print s[i], s[leng-i-1]
            return False
    return True
```
