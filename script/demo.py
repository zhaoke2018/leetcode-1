from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None: # python3 2d list typing!!!
        """
        Do not return anything, modify board in-place instead.
        """
        

# sol = Solution().longestPalindrome('babad')
# sol = Solution().longestPalindrome('cbbd')
sol = Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]) 
print(sol)