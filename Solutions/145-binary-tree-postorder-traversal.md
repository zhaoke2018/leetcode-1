- [Intro](#intro)

## Intro

- https://leetcode.com/problems/binary-tree-postorder-traversal

Given a binary tree, return the postorder traversal of its nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?


- postorder traversal https://leetcode.com/problems/binary-tree-postorder-traversal/
  - 参考 https://www.youtube.com/watch?v=4zVdfkpcT6U





```py
def postorderTraversal_recursive(root):
    res = [], []
    while root:
        postorderTraversal_recursive(root.left)
        postorderTraversal_recursive(root.right)
        res.append(root.val)

def postorderTraversal_iterative(root):
    stack, res = [], []
    while root:
        stack.append(root)
```





