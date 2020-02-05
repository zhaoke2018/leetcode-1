from typing import List

from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return

      
        # Define basic values {
        order = []
        que = deque([root])
        # }


        # print(len(que))
        while len(que):
            current = que.popleft() # 出栈
            order.append(current.val)
            
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        return order

# sol = Solution().longestPalindrome('babad')
# sol = Solution().longestPalindrome('cbbd')
sol = Solution().solve([1,2,3]) 
print(sol)