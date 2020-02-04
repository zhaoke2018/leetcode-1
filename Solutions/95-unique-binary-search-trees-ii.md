- [Intro](#intro)

## Intro

- https://leetcode.com/problems/unique-binary-search-trees-ii

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3



- https://leetcode.com/problems/unique-binary-search-trees-ii/


```py
def numTrees(self, n: int) -> int:
    pass
```



## Topics

- `Dynamic Programming`
- `Tree`


## Recursion
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

