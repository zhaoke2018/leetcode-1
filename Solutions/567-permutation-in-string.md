- [Intro](#intro)

## Intro

- https://leetcode.com/problems/permutation-in-string

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
 
Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

 
Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


- 检验 s1 的变种是否存在 s2 中 https://leetcode.com/problems/permutation-in-string/


```py
def checkInclusion(self, s1: str, s2: str) -> bool:
    sm = Counter(s1)
    bg = Counter(s2[:len(s1)-1])

    for i in range(len(s1), len(s2)):

```
- 检验 s1 的变种是否存在 s2 中 https://leetcode.com/problems/permutation-in-string/


```py
def checkInclusion(self, s1: str, s2: str) -> bool:
    sm = Counter(s1)
    bg = Counter(s2[:len(s1)-1])

    for i in range(len(s1), len(s2)):

```

## Topics

- `Two Pointers`
- `Sliding Window`


