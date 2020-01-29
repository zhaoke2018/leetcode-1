
- https://leetcode.com/problems/unique-binary-search-trees-ii/
- 
- [Iteration] Recursion

```py
# wrong answer 待修改
def generateTrees(self, n):
  def stepTree(start, end):
    trees = []
    for i in xrange(start, end + 1):
      atree = TreeNode(i) # 以i为root
      # 其余的值,经过判断,找到自己的位置
      for left in stepTree(start, i - 1):
        for right in stepTree(i + 1, end):
          atree.left = left
          atree.right = right
          trees.append(tree)
    return trees
  return stepTree(1, n) if n else []
```

- [DP]


```py
# BST节点大小: 左 < 中 < 右
def generateTrees(self, n):
  return res
```

