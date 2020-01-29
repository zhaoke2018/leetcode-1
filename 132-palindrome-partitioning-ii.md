


- https://leetcode.com/problems/palindrome-partitioning-ii/





## DP

- dp[i] 表示到 i 需要的最小cut, 且两边都是回文.
- 感觉有点像区间DP.

```py
class Solution:
    def minCut(self, s: str) -> int:
        dp[i] = min(dp[i-1], )
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