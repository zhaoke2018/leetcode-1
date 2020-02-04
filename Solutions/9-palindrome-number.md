- [Intro](#intro)

## Intro

- https://leetcode.com/problems/palindrome-number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?



## Topics

- `Math`


## two pointers

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
