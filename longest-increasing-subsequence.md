
- 给定一个数组,求最长递增子序列,不需要连续 https://leetcode.com/problems/longest-increasing-subsequence/
  - 五种解法!!! http://www.cnblogs.com/grandyang/p/4938187.html
  - Google 只关心最优解

```py
def LCS(s1, s2):
    m, n = len(s1), len(s2)
    arr = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    return arr[m][n]
```