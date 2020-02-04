- [Intro](#intro)

## Intro

- https://leetcode.com/problems/path-sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.




## Topics

- `Tree`
- `Depth-first Search`


## Iteration

```py
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 开始从 root 遍历
        while current:
            if current.left:
                currentSum += current.left.val
                if currentSum == sum:
                    return True

        

        return False
```






## 知识总结

- Python 的 class 关键词是小写的!



```py
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 开始从 root 遍历
        while current.left or current.right:
            
        

        return False
```