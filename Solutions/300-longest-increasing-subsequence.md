- [Intro](#intro)

## Intro

- https://leetcode.com/problems/longest-increasing-subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note: 

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

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