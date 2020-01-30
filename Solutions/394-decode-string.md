- [Intro](#intro)

## Intro

- https://leetcode.com/problems/decode-string

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

 


## Basic

- https://leetcode.com/problems/decode-string/description/




## Regex

- sub() 与 捕获的组合用法很常用，对照文档理解下 https://leetcode.com/problems/decode-string/discuss/87536/3-lines-Python-2-lines-Ruby-regular-expression
- 正则匹配远比我想象的简单，注意这里 捕获 的 写法！



```py
# Time Limit Exceeded
class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-zA-Z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s

# Accepted
class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = re.sub(r'(\d+)\[([^\[^\]]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
            # \[([^\[^\]]*)\] 表示匹配所有大小写
        return s
```



## Stack

stack很适合，但是好难看懂，白天笔纸模拟一下



```py
class Solution:
    def decodeString(self, s: str) -> str:
        def visit(ss):
            temp_stack
            if isdigit(ss[0]):
        


```


## DFS

DFS代码待看



- 第一层，找到本层所有 数字+[] 的组合；
- 如果遇到层内还有其他的，就BFS递归

- 至于如何找，直接找[]组合即可，遇到数字就找下一个]。