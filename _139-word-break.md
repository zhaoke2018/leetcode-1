


- https://leetcode.com/problems/word-break/


```py
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

# 执行这个例子时, 超时
sol = Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])




```