
- Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters
  - expand until see duplicate, contract until duplicate gone.


```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        head, rear = 0, 0
        maxLength = 0
        while head < len(s):
            
            if s[head] not in unique: # [Expand phase] 只要不重复,就可以一直扩张!
                unique[s[head]] = 1
                head += 1
                maxLength = max(maxLength, len(unique))
                print('expand + ', s[rear: head])

            else: # [Contract phase] 收缩,直到重复解除
                while s[head] in unique:
                # while unique[s[head]] > 0: # 这样就会error: KeyError, 为什么呢?
                    del unique[s[rear]]
                    rear += 1
                    print('contract - ', s[rear: head])

        return maxLength

ret = Solution().lengthOfLongestSubstring('zyxabcdxefgde')
```

