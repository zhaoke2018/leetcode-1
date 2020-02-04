- [Intro](#intro)
- [Iteration By John](#iteration-by-john)

## Intro

- https://leetcode.com/problems/binary-tree-inorder-traversal

Given a binary tree, return the inorder traversal of its nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?



## Topics

- `Hash Table`
- `Stack`
- `Tree`


## Iteration By John

```py
def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    order = []
    cur = root
    
    while cur or len(stack):
        while cur != None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        order.append(cur.val)
        cur = cur.right
    
    return order
```


