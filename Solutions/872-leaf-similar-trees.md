- [Intro](#intro)
- [Recursion By John](#recursion-by-john)

## Intro

- https://leetcode.com/problems/leaf-similar-trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
 
Note:

Both of the given trees will have between 1 and 100 nodes.


## Topics

- `Tree`
- `Depth-first Search`


## Recursion By John


- [思路] DFS遍历整个树, 如果某个节点没有子节点, 就可以加入结果序列. 最后比较两个树的结果序列即可.
- [注意] 题目要求从左至右组成序列, 因此必须使用从左至右的DFS. BFS会变成层次排序, 不符合题意.

```py
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root): # 返回一个 generator
            if node:
                if not root.left and not root.right: # 如果没有子节点, 就可以收集这个
                    yield root.val
                yield from dfs(root.left)
                yield from dfs(root.right)
        return list(dfs(root1)) == list(dfs(root2)) # generator 可以 list 化.
```

