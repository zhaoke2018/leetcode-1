from typing import List
import collections 

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m+1)] * (n+1) # dp[i][j] 表示i个0,j个1最多可以构成多少个字符串 # m:0

        for ss in strs:
            # 统计 zero one 出现的次数
            counter = collections.Counter(ss)
            count_zero = counter['0']
            count_one = counter['1']
            
            for ii in range(m, count_zero-1, -1):
                for jj in range(n, count_one-1, -1):
                    print('越界了吗?', ii-count_zero, jj-count_one)
                    dp[ii][jj] = max(dp[ii][jj], dp[ii - count_zero][jj - count_one] + 1)
        return dp[m][n]


# sol = Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) 
sol = Solution().findMaxForm(["11", "01", "10"], 1, 1) 
print(sol)