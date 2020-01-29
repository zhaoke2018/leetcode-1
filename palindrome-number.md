
- https://leetcode.com/problems/palindrome-number/
  - 检测数字是否回文.
  - 两端对比法,比较慢.

```py
# Runtime: 272 ms, faster than 22.11% of Python online submissions for Palindrome Number.
class Solution(object):
    def isPalindrome(self, x):
        stri = str(x) # 使用了额外的空间!
        leng = len(stri)
        for i in xrange(leng / 2):
            if stri[i] != stri[leng-i-1]:
                return False
        return True
```
