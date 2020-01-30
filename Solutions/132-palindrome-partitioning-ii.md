- [Intro](#intro)

## Intro

- https://leetcode.com/problems/palindrome-partitioning-ii

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


- https://leetcode.com/problems/palindrome-partitioning-ii/
  - 将字符串切割成回文子串,问最小切割次数是?
  - https://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/
  - 感觉跟rod cutting 有点像?

```py
# st[i,j]表示区间(i,j)的回文最小切割次数
st[i][j] = st[i][mid] + st[mid][j]

# hw[i][j]: 区间是否为回文
hw[i][j] = hw[i+1][j-1] and hw[i] == hw[j]
```

 





## DP

- dp[i] 表示到 i 需要的最小cut, 且两边都是回文.
- 感觉有点像区间DP.

```py
class Solution:
    def minCut(self, s: str) -> int:
        dp[i] = min(dp[i-1], )
```



- https://leetcode.com/problems/palindrome-partitioning-ii/
  - 将字符串切割成回文子串,问最小切割次数是?
  - https://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/
  - 感觉跟rod cutting 有点像?

```py
# st[i,j]表示区间(i,j)的回文最小切割次数
st[i][j] = st[i][mid] + st[mid][j]

# hw[i][j]: 区间是否为回文
hw[i][j] = hw[i+1][j-1] and hw[i] == hw[j]
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