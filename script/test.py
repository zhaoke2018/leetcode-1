from typing import List
import collections 

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp = [[0] * (n+1)] * (m+1) # shallow copy, 遗患无穷!
        dp = [[0] * (n+1) for _ in range(m+1)] # dp[i][j] 表示i个0,j个1最多可以构成多少个字符串 # m:0

        for ss in strs:
            # 统计 zero one 出现的次数
            counter = collections.Counter(ss)
            count_zero = counter['0']
            count_one = counter['1']
            
            for zz in range(m, count_zero-1, -1): # Backwards iteration
                for oo in range(n, count_one-1, -1):
            # for zz in range(count_zero, m+1): # Backwards iteration
            #     for oo in range(count_one, n+1):
                    dp[zz][oo] = max(dp[zz][oo], dp[zz - count_zero][oo - count_one] + 1)
        print('逆向遍历', dp)
        return dp[m][n]

sol = Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) 
# sol = Solution().findMaxForm(["11", "1", "0"], 1, 1) 
print(sol)