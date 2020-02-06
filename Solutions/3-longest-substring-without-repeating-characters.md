- [Intro](#intro)
- [Topics](#topics)
- [Sliding Window](#sliding-window)

## Intro

- https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 


Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.






## Topics

- `Hash Table`
- `Two Pointers`
- `String`
- `Sliding Window`
- substring 是连续起来的字符串; sub sequence 非连续.


## Sliding Window

- [思路] 使用 head + rail 进行 sliding window. 如果 s[head] 不重复, 就一直 expand, 如果重复了, 就 contract


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




