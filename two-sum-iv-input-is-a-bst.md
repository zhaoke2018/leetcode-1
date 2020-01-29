
- https://leetcode.com/problems/two-sum-iv-input-is-a-bst/ tree/easy
  - input一个binary search tree和一个val,若树中有两个元素加起来==val,则返回true,否则返回false.
  - [Hash] 跟最普通的 2 sum 一样, 区别在于, 遍历的是BST, 而不是一个数组.

```py
def findTarget(self, root: TreeNode, k: int) -> bool:
    cache = set()
    qu = [root] # 使用 queue 实现 BFS
    while qu: # 遍历所有数据
        cv = qu.pop()
        if k-cv.val in cache:
            return True
        else:
            cache.add(cv.val)
            
            if cv.left: qu.append(cv.left)
            if cv.right: qu.append(cv.right)
    return False
```
