

- 二叉树版 maximum path sum https://leetcode.com/problems/binary-tree-maximum-path-sum/
  - 拿起树,就是一顿DFS/BFS.
  - 路径基本都是一个^状,所以必然是sub_root到左右子树的遍历.所以本题实际上就是两条 maximum subarray 加起来而已咯
  - Recursion 都是理解起来简单,但是要想出来就很难.


```py
def maxPathSum(self, root):
    globalMax = -sys.maxint
    globalMax = self.subMax(root, globalMax)[0] # 非常不简洁,待改进
    return globalMax

def subMax(self, node, globalMax):
    if not node:
        return [globalMax,0]
    left = max(self.subMax(node.left, globalMax)[1], 0)
    right = max(self.subMax(node.right, globalMax)[1], 0)
    print left, right
    globalMax = max(globalMax, left + right + node.val) # 计算左右结果之和
    subMax = max(left, right) + node.val # 单条结果
    return [globalMax, subMax]
```




