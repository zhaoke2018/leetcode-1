
- n个点,可以排列出多少个不同的BST https://leetcode.com/problems/unique-binary-search-trees/
  - BST: left < root < right
  - 由于树是由左右子树组成的, 因此容易构成DP题 !!!

```py
dp[2] = dp[0] * dp[1] # 1为根的情况，则左子树一定不存在，右子树可以有一个数字
　　　　+ dp[1] * dp[0] # 2为根的情况，则左子树可以有一个数字，右子树一定不存在

dp[3] = dp[0] * dp[2] # 1为根的情况，则左子树一定不存在，右子树可以有两个数字
　　　　+ dp[1] * dp[1] # 2为根的情况，则左右子树都可以各有一个数字
 　　　  + dp[2] * dp[0] # 3为根的情况，则左子树可以有两个数字，右子树一定不存在
```

- 归纳发现, 这是个`卡塔兰数`


```py
def numTrees(self, n: int) -> int:
    pass
```