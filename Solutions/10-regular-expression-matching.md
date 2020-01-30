- [Intro](#intro)

## Intro

- https://leetcode.com/problems/regular-expression-matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false







## Backtracking By Leetcode

匹配情况
- * 重复次数: [0,∞)
- 

```py
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text # 技巧!

        # 对于每个字符, 要么一毛一样, 要么通配
        first_match           = bool(text) and pattern[0] in {text[0], '.'}

        pattern_next_kleene   = len(pattern) >= 2 and pattern[1] == '*'

        pattern_skip_next     = self.isMatch(text, pattern[2:])
        text_next             = self.isMatch(text[1:], pattern)
        done_this_check_next_pair = first_match and self.isMatch(text[1:], pattern[1:])
        
        if pattern_next_kleene:
            return (pattern_skip_next or (first_match and text_next))
        else:
            return check_next_pair
```







## DP By Leetcode



```py
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
```










