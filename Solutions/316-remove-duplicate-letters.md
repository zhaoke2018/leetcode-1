- [Intro](#intro)

## Intro

- https://leetcode.com/problems/remove-duplicate-letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
Example 1:

Input: "bcabc"
Output: "abc"

Example 2:

Input: "cbacdcbc"
Output: "acdb"



## xx

- https://leetcode.com/problems/remove-duplicate-letters/


```py
def removeDuplicateLetters(self, s):
    for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    return ''

def removeDuplicateLetters(self, s):
    table = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    
    # 循环验证table,一旦匹配上就标记为之后不能再来.
    for i in s.reversed():
        if i in table:
            table[i] = True
    
    # 最终倒置一下即可
    return res.reversed()
```



- https://leetcode.com/problems/remove-duplicate-letters/


```py
def removeDuplicateLetters(self, s):
    for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    return ''

def removeDuplicateLetters(self, s):
    table = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    
    # 循环验证table,一旦匹配上就标记为之后不能再来.
    for i in s.reversed():
        if i in table:
            table[i] = True
    
    # 最终倒置一下即可
    return res.reversed()
```

