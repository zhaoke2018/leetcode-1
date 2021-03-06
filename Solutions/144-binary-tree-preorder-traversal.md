- [Intro](#intro)
- [Topics](#topics)
- [Iteration](#iteration)
- [Recursion - Pythonic](#recursion---pythonic)
- [Recursion - Regular](#recursion---regular)
- [Morris Traversal](#morris-traversal)

## Intro

- https://leetcode.com/problems/binary-tree-preorder-traversal

Given a binary tree, return the preorder traversal of its nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?






## Topics

- `Stack`
- `Tree`
- `Iteration`
- `Recursion - Pythonic`
- `Recursion - Regular`
- `Morris Traversal`


## Iteration

```py
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return
        order = []
        que = deque([root])

        while len(que):
            current = que.popleft() # 出栈
            order.append(current.val)
            
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        return order
```


## Recursion - Pythonic

- faster than 66.87% 
- Pythonic 写法, 虽然很简单, 但是对于其他语言不具备普适性


```py
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```


## Recursion - Regular

- faster than 66.87% 
- 普通写法需要有一个辅助函数.

```py
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        def preder(node):
            if not node:
                res.append(node.val)
                preder(node.left)
                preder(node.right)

        res = []
        preder(root)
        return res
```


## Morris Traversal