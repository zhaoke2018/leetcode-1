from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n+1)] # dp[i] 从i后面切开 的最小切割次数
        # 因为 i 在 s[j:i] 中作为末尾的指针, 所以必须到 n+1
        
        memo_palin = self.memoPalindrome(s) # 缓存
        print(memo_palin)

        for i in range(1, n+1):
            if memo_palin[0][i]:
                print('整个字符串都是回文: 0-', i)
                dp[i] = 0
                continue
            for j in range(i):
                if memo_palin[j][i]: # abcd aba
                    print('部分回文: ', j, i)
                    dp[i] = min(dp[i], dp[j]+1) # 前面是回文
        
        print('dp', dp)
        return dp[-1]
    
    def memoPalindrome(self, s) -> List[List[int]]:
        memo_palin = [[False for _ in range(len(s))] for _ in range(len(s))]
        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or memo_palin[left + 1][right - 1]):
                    memo_palin[left][right] = True
        return memo_palin

sol = Solution().minCut('aabaa')
print(sol)