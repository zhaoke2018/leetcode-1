- [Intro](#intro)
- [Topics](#topics)
- [Hash](#hash)

## Intro

- https://leetcode.com/problems/group-anagrams

Given an array of strings, group anagrams together.
Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.



## Topics

- `Hash Table`
- `String`


## Hash


```py
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    cache = dict()
    
    for i in strs:
        unify = ''.join(sorted(i)) # 对字符串排序. 排序后, 所有的 anagram 都长得一样了
        if unify in cache:
            cache[unify].append(i)
        else:
            cache[unify] = [i]
    return [value for value in cache.values()]
```

