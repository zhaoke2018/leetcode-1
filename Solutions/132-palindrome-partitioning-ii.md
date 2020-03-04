- [Intro](#intro)
- [Topics](#topics)
- [DP](#dp)
  - [Memo Palindrome](#memo-palindrome)
- [Recursion](#recursion)

## Intro

- https://leetcode.com/problems/palindrome-partitioning-ii

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


- 将字符串切割成回文子串,问最小切割次数是?
- https://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/
- 感觉跟rod cutting 有点像?








## Topics

- `Dynamic Programming`


## DP

- dp[i] 表示到 i 需要的最小cut, 且两边都是回文.
- 感觉有点像区间DP.
- faster than 26%
- 优化空间, 将回文判断部分使用 `palin[i][j]` 进行记忆下来.

```py
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n+1)] # dp[i] 从i后面切开 的最小切割次数
        # 因为 i 在 s[j:i] 中作为末尾的指针, 所以必须到 n+1
        
        for i in range(1, n+1):
            if self.isPal(s[:i]):
                dp[i] = 0
                continue
            for j in range(i):
                if self.isPal(s[j:i]): # abcd aba
                    dp[i] = min(dp[i], dp[j]+1) # 前面是回文
        
        return dp[-1]
    
    def isPal(self, s):
        return s == s[::-1]
```


### Memo Palindrome

- [TODO] 本段代码尚未调试成功

```py
from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n+1)] # dp[i] 从i后面切开 的最小切割次数
        # 因为 i 在 s[j:i] 中作为末尾的指针, 所以必须到 n+1
        
        memo_palin = self.memoPalindrome(s) # 缓存
        print(memo_palin)

        for i in range(1, n+1):
            if memo_palin[0][i]:
                print('整个字符串都是回文: 0-', i)
                dp[i] = 0
                continue
            for j in range(i):
                if memo_palin[j][i]: # abcd aba
                    print('部分回文: ', j, i)
                    dp[i] = min(dp[i], dp[j]+1) # 前面是回文
        
        print('dp', dp)
        return dp[-1]
    
    def memoPalindrome(self, s) -> List[List[int]]:
        memo_palin = [[False for _ in range(len(s))] for _ in range(len(s))]
        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or memo_palin[left + 1][right - 1]):
                    memo_palin[left][right] = True
        return memo_palin

sol = Solution().minCut('aabaa')
print(sol)
```



## Recursion

- 遍历所有的切割方式, 然后返回最小的一个. 但是会超时


```py
class Solution:
    def minCut(self, s: str) -> int:
        res = []
        self.dfs(s, [], res)
        
        return min(map(len, res))-1

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