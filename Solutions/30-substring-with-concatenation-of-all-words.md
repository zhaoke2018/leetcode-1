- [Intro](#intro)

## Intro

- https://leetcode.com/problems/substring-with-concatenation-of-all-words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
 
Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []





## Topics

- `Hash Table`
- `Two Pointers`
- `String`


## Hash By John


分析:
- 将所有 substring 的组合都保存下来, 然后使用 find string 的方法来做

- 使用 hashing?
  - All substring has the same length? which means we can compare the first chars first then confirm later.





```py
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # find substring's index that is concatenation of words
        res = []
        return res

res = Solution().findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"])
print(res)
```

