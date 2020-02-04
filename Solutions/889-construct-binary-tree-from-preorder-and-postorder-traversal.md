- [Intro](#intro)

## Intro

- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers.
 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

 
Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.








## Intro

- pre + post = BST https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
- [注意] pre 和 post 里面的 left 和 right 顺序不一样! 这是解题的关键.

- 比如
       1
      /  \
     2    3
    / \   / \
   4   5 6   7

- pre: [1] + [2, 4, 5] + [3, 6, 7]
- post: [4, 5, 2] + [6, 7, 3] + [1]

- 所以
- root = pre[0]
- left = pre[1, post.indexOf(pre[1])+1]



## Topics

- `Tree`


## Recursion By Leetcode

- 递归结构巧妙, 值得多品品.

```py
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre: return None

        root = TreeNode(pre[0])
        if len(pre) == 1: return root # 对于叶子节点, 直接返回

        L = post.index(pre[1]) + 1
        # 每次递归, 都会生成一个当前的root
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L]) # pre 始终要传入 pre
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1]) # pre 始终要传入 pre

        return root
```













