- [Intro](#intro)
- [Full Inorder By John](#full-inorder-by-john)

## Intro

- https://leetcode.com/problems/increasing-order-search-tree

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.





- [分析] 将一个 二叉树 转换成只有 右节点 的树. 结构重组. 眼尖的朋友一眼就能看出, 转换后的结果 == inorder 遍历结果.
- [Full_Inorder思路] 使用 in-order 遍历出一个数组, 然后将 遍历结果 连接成树即可.
- [Half_Inorder思路] 也可以一边 in-order 遍历, 一边重组, 处理起来稍微麻烦一点点
- 考点: python-generator, inorder-traversal.


## Topics

- `Tree`
- `Depth-first Search`


## Full Inorder By John

```py
# Python的yield 可以让这一切更优雅
def increasingBST(self, root):
    def inorder(node):
        if node:
            yield from inorder(node.left) # 记得是递归噢!
            yield node.val # 使用 yield 来一个个吐出
            yield from inorder(node.right)

    ans = cur = TreeNode(None)

    for v in inorder(root): # inorder() 返回一个 generator, 是可以遍历的!
        cur.right = TreeNode(v)
        cur = cur.right

    return ans.right
```



return ans.right
```



