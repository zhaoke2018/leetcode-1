- [Intro](#intro)
- [Topics](#topics)
- [Sliding Window - Time Limit Exceeded](#sliding-window---time-limit-exceeded)
- [Sliding Window](#sliding-window)
- [Sliding Window - Optimized](#sliding-window---optimized)

## Intro

- https://leetcode.com/problems/minimum-window-substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.






## Topics

- `Hash Table`
- `Two Pointers`
- `String`
- `Sliding Window`

## Sliding Window - Time Limit Exceeded

- [思路] 很简单, 但是每次判断都需要建立 subcount, 所以会超时
- [改进] 保留 subcount, 每次仅对其进行更新操作.


```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def qualify(count, ss):
            subcount = collections.Counter(ss)
            for key in count.keys():
                if subcount[key] < count[key]:
                    return False
            return True

        l, r = 0, 0
        minwin = s
        count = collections.Counter(t)

        # 扩张到count全部满足为止, 然后收缩到刚好不满足为止
        while r<len(s):
            while not qualify(count, s[l:r]):
                r += 1
            while qualify(count, s[l:r]):
                l += 1
            if len(minwin) > r-l:
                minwin = s[l-1:r]
        return minwin
```


## Sliding Window


LeetCode 76 几个可以提炼的小技巧：
① extend right pointer：当 right 在 s 里面遇到 t 包含的字母时，就将 count - 1
② shrink left pointer：当 left 在当前 s 里面遇到 t 包含的字母时，就将 count + 1
③ 因为字母可以重复，所以需要 frequency map 来记录每个字母出现的次数
④ 在 shrink left pointer 的时候需要不断 update result，找到最小 distance（right - left）



- 扩张到所有字符都满足
- 收缩的目的是为了继续扩张，那么收缩到刚好缺一个字符即可。


```py
def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1    

        # Keep expanding the window once we are done contracting.
        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```

## Sliding Window - Optimized

```py
def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    
```
