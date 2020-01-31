- [Intro](#intro)

## Intro

- https://leetcode.com/problems/word-break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

- [Intro](#intro)
- [DP](#dp)
  - [还可以用 Trie 辅助?](#%e8%bf%98%e5%8f%af%e4%bb%a5%e7%94%a8-trie-%e8%be%85%e5%8a%a9)
- [记忆化搜索](#%e8%ae%b0%e5%bf%86%e5%8c%96%e6%90%9c%e7%b4%a2)



## Intro

- 输入一个string和一个dict,检测string是否可以拆分成substrings,使得substrings都是dict的成员. https://leetcode.com/problems/word-break/
- [DP思路] 状态划分: dp[i] 表示 s[:i-1] 可分. 不过这里面可以利用之前的内容. 这就是DP.
  - dp 数组的长度比s串的长度大1，是因为我们要 handle 空串的情况
  - “玩子数组或者子字符串且求极值的题，基本就是 DP 没差了” by https://www.cnblogs.com/grandyang/p/4257740.html







## DP

- Only faster than 5%! 怎么办?

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for i in range(len(s)+1)]
        dp[0] = True
        
        for i in range(len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: # 这里的 dp[j] 体现了 DP 的思想
                    dp[i] = True
                    break
        return dp[-1]
```

- 我也是，怎么这么慢！？明明都是DP，差距怎么这么大？-克
```Java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] == true && wordDict.contains(s.substring(j, i))) dp[i]=true;
            }
        }
        return dp[s.length()];
        
    }
}
```

### 还可以用 Trie 辅助?


## 记忆化搜索

- faster than 88%

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        return self.reccur(s,set(wordDict),memo)

    def reccur(self,s,wordDict,memo):
        if s in memo: return memo[s]
        if s=='': return True

        # dividing
        for i in range(1,len(s)+1):
            if s[:i] in wordDict and self.reccur(s[i:],wordDict,memo): # 表示 整个s 都可分
                memo[s]=True
                return True
        memo[s]=False
        return False
```


