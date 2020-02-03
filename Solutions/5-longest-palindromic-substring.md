- [Intro](#intro)
- [Interval DP](#interval-dp)
- [Expand String](#expand-string)

## Intro

- https://leetcode.com/problems/longest-palindromic-substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"



## Interval DP

- [区间DP思路] 这是一道典型的区间 DP 的题. 用二维数组的两个坐标来表示区间而已, 没什么奇特的. 本题的状态转移关系也很明显.

- faster than 18.47% 


```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        dp = [[True if i==j else False for i in range(slen)] for j in range(slen)] # dp[i][j] = True, 表示 区间[i,j]是一个回文数
        start = end = 0

        for ii in range(0, slen, 1): # substr end
            for jj in range(ii-1, -1, -1): # substr start
                is_end_palin = s[ii] == s[jj]
                if ii-jj == 1: # 处理 "aa" 的情况
                    dp[ii][jj] = is_end_palin
                elif is_end_palin and dp[ii-1][jj+1]: # 处理 "aba" 的情况
                    dp[ii][jj] = True
                
                if dp[ii][jj] and ii - jj > end - start: # 更新最长的下标
                    start, end = jj, ii
        return s[start: end+1]

```



## Expand String

- [Expand思路] 本方法利用的是 Palindrome 两边对称的特性. 容易想到, 也容易实现, 但是普适性不强.
- 

性能参数
- faster than 71.73%
- Time Complexity:  O(n^2)
- Space Complexity: O(1)


```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substri = ''
        for i in range(len(s)):
            odd_ss = self.expand_str(s, i, i)
            even_ss = self.expand_str(s, i, i+1) # 对于 even number, 多比较一次就行了
            ss = odd_ss if len(odd_ss) > len(even_ss) else even_ss

            if len(ss) > len(longest_substri):
                longest_substri = ss
        return longest_substri
    
    def expand_str(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: # 这只能处理 odd number 的扩展
            left -= 1
            right += 1
        return s[left+1:right]


# sol = Solution().longestPalindrome('babad')
# sol = Solution().longestPalindrome('cbbd')
sol = Solution().longestPalindrome('a') 
print(sol)
```