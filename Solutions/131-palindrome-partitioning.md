- [Intro](#intro)
- [Recursion](#recursion)
- [Recursion with unittest](#recursion-with-unittest)

## Intro

- https://leetcode.com/problems/palindrome-partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]











## Topics

- `Backtracking`


## Recursion



- Python 直接将字符串转置的复杂度是多少?


```py
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
```



## Recursion with unittest




```py
#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
- 一搜 "leetcode unittest",立马找出最直接的单测教程,😄
  - https://github.com/hongxiaolong/leetcode
- unittest那么多方法,如何画出一个API图呢? 👉 cheatsheet or dash
"""
import unittest
 
class Solution(object):
    def partition(self, s):
        print s
        if not s:
            return []
        self.result = []
        self.end = len(s)
        self.str = s

        self.is_palindrome = [[False for i in range(self.end)]
                              for j in range(self.end)]

        for i in range(self.end-1, -1, -1):
            for j in range(self.end):
                if i > j:
                    pass
                elif j-i < 2 and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                elif self.is_palindrome[i+1][j-1] and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                else:
                    self.is_palindrome[i][j] = False

        self.palindrome_partition(0, [])
        return self.result

    def palindrome_partition(self, start, sub_strs):
        if start == self.end:
            # It's confused the following sentence doesn't work.
            # self.result.append(sub_strs)
            self.result.append(sub_strs[:])
            return

      for i in range(start, self.end):
          if self.is_palindrome[start][i]:
              sub_strs.append(self.str[start:i+1])
              self.palindrome_partition(i+1, sub_strs)
              sub_strs.pop()      # Backtracking here

class TestListElements(unittest.TestCase):
  """
  Given a string s, partition s such that every substring of the partition is a palindrome.

  Return all possible palindrome partitioning of s.
  """
    def test(self):
        s = Solution()
        input = "aab"
        output = [
          ["aa","b"],
          ["a","a","b"]
        ]
        # self.assertEqual(s.partition(input), output) # 现在获取的结果是正确的,但是顺序不对,如何assert呢?
        self.assertItemsEqual(s.partition(input), output) # 直接对比数组,不用管顺序. python3.2 接口变成了 assertCountEqual


if __name__ == '__main__':
    unittest.main()
```




- 给定字符串s,将其拆成每一个substring都是回文,即使只有一个字母.返回所有拆分方式 https://leetcode.com/problems/palindrome-partitioning/ backtracking/hard


```py
#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
- 一搜 "leetcode unittest",立马找出最直接的单测教程,😄
  - https://github.com/hongxiaolong/leetcode
- unittest那么多方法,如何画出一个API图呢? 👉 cheatsheet or dash
"""
import unittest
 
class Solution(object):
    def partition(self, s):
        print s
        if not s:
            return []
        self.result = []
        self.end = len(s)
        self.str = s

        self.is_palindrome = [[False for i in range(self.end)]
                              for j in range(self.end)]

        for i in range(self.end-1, -1, -1):
            for j in range(self.end):
                if i > j:
                    pass
                elif j-i < 2 and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                elif self.is_palindrome[i+1][j-1] and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                else:
                    self.is_palindrome[i][j] = False

        self.palindrome_partition(0, [])
        return self.result

    def palindrome_partition(self, start, sub_strs):
        if start == self.end:
            # It's confused the following sentence doesn't work.
            # self.result.append(sub_strs)
            self.result.append(sub_strs[:])
            return

      for i in range(start, self.end):
          if self.is_palindrome[start][i]:
              sub_strs.append(self.str[start:i+1])
              self.palindrome_partition(i+1, sub_strs)
              sub_strs.pop()      # Backtracking here

class TestListElements(unittest.TestCase):
  """
  Given a string s, partition s such that every substring of the partition is a palindrome.

  Return all possible palindrome partitioning of s.
  """
    def test(self):
        s = Solution()
        input = "aab"
        output = [
          ["aa","b"],
          ["a","a","b"]
        ]
        # self.assertEqual(s.partition(input), output) # 现在获取的结果是正确的,但是顺序不对,如何assert呢?
        self.assertItemsEqual(s.partition(input), output) # 直接对比数组,不用管顺序. python3.2 接口变成了 assertCountEqual


if __name__ == '__main__':
    unittest.main()
```



