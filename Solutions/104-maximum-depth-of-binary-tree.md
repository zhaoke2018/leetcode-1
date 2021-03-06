- [Intro](#intro)
- [Topics](#topics)
- [Recursion](#recursion)

## Intro

- https://leetcode.com/problems/maximum-depth-of-binary-tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.



## Topics

- `Tree`
- `Depth-first Search`


## Recursion

- 要记得在 children 里面取max.
- 需要判断的节点, 只有三种情况.
```py
if not root:
    # bye bye
else:
    if not children:
        # 深度计算到这里就可以了
    else:
        # 继续遍历
```



```py
def maxDepth(self, root: TreeNode) -> int:
    def depth(root, currDepth):
        if not root:
            return currDepth
        if not root.left and not root.right: # 如果只有根, 没有子节点, 那就 当前深度+1 完成
            return currDepth + 1
        elif root.left or root.right:
            return max(depth(root.left, currDepth + 1), depth(root.right, currDepth + 1)) # 如果有子节点, 那就看谁更深
    
    return depth(root, 0)
```