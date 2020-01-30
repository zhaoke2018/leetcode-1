- [Intro](#intro)

## Intro

- https://leetcode.com/problems/minimum-window-substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.





## xxx

TODO
- 已经做到一半了, 思想也掌握了, 赶紧完成吧.







LeetCode 76 几个可以提炼的小技巧：
① extend right pointer：当 right 在 s 里面遇到 t 包含的字母时，就将 count - 1
② shrink left pointer：当 left 在当前 s 里面遇到 t 包含的字母时，就将 count + 1
③ 因为字母可以重复，所以需要 frequency map 来记录每个字母出现的次数
④ 在 shrink left pointer 的时候需要不断 update result，找到最小 distance（right - left）
















- https://leetcode.com/problems/minimum-window-substring/

```py


```


```py


```
