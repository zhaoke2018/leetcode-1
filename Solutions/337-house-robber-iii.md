- [Intro](#intro)

## Intro

- https://leetcode.com/problems/house-robber-iii

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.








## Topics

- `Tree`
- `Depth-first Search`


## By John

- 考点: 递归的写法!!

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









