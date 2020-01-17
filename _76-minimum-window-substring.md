



https://leetcode.com/problems/minimum-window-substring/



TODO
- 已经做到一半了, 思想也掌握了, 赶紧完成吧.







LeetCode 76 几个可以提炼的小技巧：
① extend right pointer：当 right 在 s 里面遇到 t 包含的字母时，就将 count - 1
② shrink left pointer：当 left 在当前 s 里面遇到 t 包含的字母时，就将 count + 1
③ 因为字母可以重复，所以需要 frequency map 来记录每个字母出现的次数
④ 在 shrink left pointer 的时候需要不断 update result，找到最小 distance（right - left）














