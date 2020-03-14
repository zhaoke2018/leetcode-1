- [Intro](#intro)
- [Topics](#topics)
- [Recursion](#recursion)

## Intro

- https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7



## Topics

- `Array`
- `Tree`
- `Depth-first Search`


## Recursion


```py
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder: left root right
        # postorder: left right root
        if not inorder:
            return None
        root = TreeNode(postorder[-1])

        idx = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return root
```