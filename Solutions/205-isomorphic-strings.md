- [Intro](#intro)

## Intro

- https://leetcode.com/problems/isomorphic-strings

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

- 如果两个单词相同位置是相同字母, 就是 isomorphic https://leetcode.com/problems/isomorphic-strings/


- ref
  - https://v.qq.com/x/page/x0518u9b8i0.html XCodeCareerService出品

```py
# 这个想法很好,但是完全没有通用性吧...
def isIsomorphic(self, s: str, t: str) -> bool:
  """
  zip([1, 2, 3], [4, 5, 6]) 得到 [(1, 4), (2, 5), (3, 6)]
  """
  return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphic(self, s: str, t: str) -> bool:
    hashMap = new hashMap()
    for i in xrange(len(s)):
        if hashMap[s[i]] is none:
            hashMap[s[i]] = t[i]
        elif hashMap[s[i]] !== t[i]:
            return false
    return true
```



- 通常的follow-ups是3+个string,所以考虑通用解就可以了.
