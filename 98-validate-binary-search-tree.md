



- https://leetcode.com/problems/validate-binary-search-tree/






```py
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def traverse(root, min_=float('-inf'), max_=float('inf')):
            if not root:
                return True
            
            if root.val >= max_ or root.val <= min_: # 保证本代在限定范围内
                return False
            
            if not traverse(root.left, min_, root.val):
                return False
            if not traverse(root.right, root.val, max_):
                return False
            return True

        return traverse(root)
```






