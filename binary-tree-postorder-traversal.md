

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





