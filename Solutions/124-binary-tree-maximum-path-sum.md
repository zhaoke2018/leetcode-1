- [Intro](#intro)

## Intro

- https://leetcode.com/problems/binary-tree-maximum-path-sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42









## Topics

- `Tree`
- `Depth-first Search`


## DFS by John



- 二叉树版 maximum path sum https://leetcode.com/problems/binary-tree-maximum-path-sum/
  - 拿起树,就是一顿DFS/BFS.
  - 路径基本都是一个^状,所以必然是sub_root到左右子树的遍历.所以本题实际上就是两条 maximum subarray 加起来而已咯
  - Recursion 都是理解起来简单,但是要想出来就很难.


```py
def maxPathSum(self, root):
    globalMax = -sys.maxint
    globalMax = self.subMax(root, globalMax)[0] # 非常不简洁,待改进
    return globalMax

def subMax(self, node, globalMax):
    if not node:
        return [globalMax,0]
    left = max(self.subMax(node.left, globalMax)[1], 0)
    right = max(self.subMax(node.right, globalMax)[1], 0)
    print left, right
    globalMax = max(globalMax, left + right + node.val) # 计算左右结果之和
    subMax = max(left, right) + node.val # 单条结果
    return [globalMax, subMax]
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




































- 二叉树版 maximum path sum https://leetcode.com/problems/binary-tree-maximum-path-sum/
  - 拿起树,就是一顿DFS/BFS.
  - 路径基本都是一个^状,所以必然是sub_root到左右子树的遍历.所以本题实际上就是两条 maximum subarray 加起来而已咯
  - Recursion 都是理解起来简单,但是要想出来就很难.


```py
def maxPathSum(self, root):
    globalMax = -sys.maxint
    globalMax = self.subMax(root, globalMax)[0] # 非常不简洁,待改进
    return globalMax

def subMax(self, node, globalMax):
    if not node:
        return [globalMax,0]
    left = max(self.subMax(node.left, globalMax)[1], 0)
    right = max(self.subMax(node.right, globalMax)[1], 0)
    print left, right
    globalMax = max(globalMax, left + right + node.val) # 计算左右结果之和
    subMax = max(left, right) + node.val # 单条结果
    return [globalMax, subMax]
```




