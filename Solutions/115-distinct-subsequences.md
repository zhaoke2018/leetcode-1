- [Intro](#intro)

## Intro

- https://leetcode.com/problems/distinct-subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^






- https://leetcode.com/problems/distinct-subsequences
  - 给定2个字符串a, b，求b在a中出现的次数。要求可以是不连续的，但是b在a中的顺序必须和b以前的一致。 
  - Here is an example: S = "rabbbit", T = "rabbit" 
  - Return 3.
  - 类似于数字分解的题目。dp[i][j]表示：b的前j个字符在a的前i个字符中出现的次数。
  - 如果S[i]==T[j]，那么dp[i][j] = dp[i-1][j-1] + dp[i-1][j]。
  - 意思是：如果当前S[i]==T[j]，那么当前这个字母即可以保留也可以抛弃，所以变换方法等于保留这个字母的变换方法加上不用这个字母的变换方法。
  - 如果S[i]!=T[i]，那么dp[i][j] = dp[i-1][j]，
  - 意思是如果当前字符不等，那么就只能抛弃当前这个字符
  - 递归公式中用到的dp[0][0] = 1，dp[i][0] = 0（把任意一个字符串变换为一个空串只有一个方法