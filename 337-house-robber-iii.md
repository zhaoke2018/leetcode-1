


## Intro

- 房子阵型为 binary tree, 相邻的房子不能抢, 求最大收益 https://leetcode.com/problems/house-robber-iii/
- 考点: 递归的写法!!







## By John

```py
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 直接 DFS 不行, 还需要把路径记录下来
        def dfs(root):
            if not root:
                return 0
            return max(root.val, dfs(root.left)+dfs(root.right))
        return dfs(root)



```




## By Leetcode

```py
def rob_iii(root):
    cache = {}

    if not root:
        return 0

    if root in cache:
        return cache[root]

    # Rob the root node.
    money = root.val
    if root.left:
        money += self.rob(root.left.right) + self.rob(root.left.left)
    if root.right:
        money += self.rob(root.right.left) + self.rob(root.right.right)

    # Do not rob the root node.
    cache[root] = max(money, self.rob(
        root.left) + self.rob(root.right))
    return cache[root]
```









