

## Intro

- https://leetcode.com/problems/longest-substring-without-repeating-characters/


- substring 是连续起来的字符串; sub sequence 非连续.



## Sliding Window

- [思路] 使用 head + rail 进行 sliding window. 如果 s[head] 不重复, 就一直 expand, 如果重复了, 就 contract

```py
if s[head] is unique:
    keep expand
else:
    contract
```

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head, rear = 0, 0
        unique = {}

        while head < len(s)-1:
            if s[head] not in unique:
                unique[s[head]] = 1
                maxlen = max(maxlen, len(unique))
                head += 1
            else:
                # 当前 head 已经指到一个重复的元素了, 并且还没有加入 unique
                while s[head] in unique:
                    del unique[s[head]]
                    rear += 1
        return maxlen
```




## 






