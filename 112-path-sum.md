


```py
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 开始从 root 遍历
        while current:
            if current.left:
                currentSum += current.left.val
                if currentSum == sum:
                    return True

        

        return False
```






## 知识总结

- Python 的 class 关键词是小写的!



```py
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 开始从 root 遍历
        while current.left or current.right:
            
        

        return False
```