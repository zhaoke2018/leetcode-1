



## Intro

- 找到一个二叉树里面「和最大」的路径 https://leetcode.com/problems/binary-tree-maximum-path-sum/



## DFS by John


```py

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        



```





## by wangyou1

- [经验] 按顺序 print 是 debug 神器


```py
class Solution(object):
    
    def maxPathSum(self, root):
        
        def side_max(root):
            if not root:
                return 0
            left_max = side_max(root.left)
            left_max = left_max if left_max > 0 else 0
            right_max = side_max(root.right)
            right_max = right_max if right_max > 0 else 0
            
            root_sum = root.val + left_max + right_max
            self.root_max = max(self.root_max, root_sum)
            
            return max(left_max, right_max) + root.val
        
        self.root_max = float('-inf') # int_min
        side_max(root)
        return self.root_max
```

[-10,9,20,null,null,15,7]

-10
/\
9 20
  /\
 15 7


- inspired by https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39884/Python-solution-beats-97
  - maxi = max(left) + max(right) + root.val

```py
class Solution(object):
    current_max = float('-inf') # int_min

    def maxPathSum(self, root):
        self.helper(root)
        return self.current_max

    def helper(self, root):
        if root is None:
            return
        left = self.helper(root.left)
        right = self.helper(root.right)
        left = 0 if left is None else (left if left > 0 else 0)
        right = 0 if right is None else (right if right > 0 else 0)
        self.current_max = max(left+right+root.val, self.current_max)
        return max(left, right) + root.val
```


































