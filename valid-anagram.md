
- 检验两个字符串是否互为 anagram https://leetcode.com/problems/valid-anagram/


```py
def isAnagram(self, s: str, t: str) -> bool:
    cts, ctt = Counter(s), Counter(t)
    return cts == ctt
```
