- [Intro](#intro)

## Intro

- https://leetcode.com/problems/word-break-ii

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
- [基本信息](#%e5%9f%ba%e6%9c%ac%e4%bf%a1%e6%81%af)
- [Backtracking by me](#backtracking-by-me)
- [xxx](#xxx)



## 基本信息

- https://leetcode.com/problems/word-break-ii/

- [Backtracking] 截取前i个元素, 然后看是否在 dict 里, 如果找到了, 就继续递归, 如果i=full length 的时候都没找到, 那就 return False.
- [DP] 这个暂时还没思路



## Backtracking by me



```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def bt(ress, stage): # ress 表示剩余的字符串
            # print("刚开始", ress, stage)
            if not ress: # 当发射器空了之后, 就阶段性结束
                res.append(stage)

            for i in range(len(ress)+1): # 为了 ress[:i] 能取到所有值
                if ress[:i] in wordDict:
                    # print(ress[:i], stage)
                    bt(ress[i:], stage+[ress[:i]])
        
        if not s:
            return
        res = []
        bt(s, [])
        return map(lambda li: ' '.join(li), res)

# 执行这个例子时, Time Limit Exceeded
sol = Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
```


## xxx



- follow-up 返回所有的拆分组合. https://leetcode.com/problems/word-break-ii/

```py
# 超时! 需要加入 memo 功能!
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wdset = set(wordDict)
        def checkReg(s):
            for i in range(1, len(s)):
                if s[:i] in wdset and s[i:] in wdset:
                    return True
                elif s[:i] in wdset and checkReg(s[i:]):
                    return True
            return False
        
        if s in wdset:
            return True
        return checkReg(s)
```

