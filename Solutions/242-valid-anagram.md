- [Intro](#intro)

## Intro

- https://leetcode.com/problems/valid-anagram

Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

- 检验两个字符串是否互为 anagram https://leetcode.com/problems/valid-anagram/


```py
def isAnagram(self, s: str, t: str) -> bool:
    cts, ctt = Counter(s), Counter(t)
    return cts == ctt
```
