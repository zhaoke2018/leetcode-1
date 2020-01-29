




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