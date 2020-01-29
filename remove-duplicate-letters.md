

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

