- [Intro](#intro)
- [Topics](#topics)
- [Trie](#trie)

## Intro

- https://leetcode.com/problems/longest-word-in-dictionary

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.  If there is more than one possible answer, return the longest word with the smallest lexicographical order.  If there is no answer, return the empty string.

Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].


## Topics

- `Hash Table`
- `Trie`


## Trie

- 好像用 dict 就能实现 trie.

```js
{'g': {'o': {'l': {'d': {}}, 'a': {'l': {}}}}, 's': {'o': {'l': {'e': {}}}}}
//// gold, goal, sole
{'g': {
  'o': {
    'l': {
      'd': {}
      }, 
      'a': {'l': {}}
  }
}, 's': {'o': {'l': {'e': {}}}}}
```


```py
class Solution:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
```