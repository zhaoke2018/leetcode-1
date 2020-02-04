- [Intro](#intro)

## Intro

- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7









## Intro




https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.

- Inorder 可以将内容一分为二
- preorder 可以找到 root




## Topics

- `Array`
- `Tree`
- `Depth-first Search`


## Recursion by John

- 利用 inorder 获取 root
- 15分钟就提交成功! 大学的时候觉得很难, 现在写起来出奇地简单!


```py
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        gen = preorder[0]
        gendix = inorder.index(gen)
        root = TreeNode(gen)
        
        inorder_left = inorder[:gendix]
        inorder_right = inorder[gendix+1:]
        root.left = self.buildTree(preorder[1:len(inorder_left)+1], inorder_left)
        root.right = self.buildTree(preorder[len(inorder_left)+1:], inorder_right)
        return root
```
















