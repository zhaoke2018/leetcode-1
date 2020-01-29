

## Intro

- 房子连成一个环, 相邻的房子不能抢, 求最大收益
  - https://leetcode.com/problems/house-robber-ii/
  - [思路] 如何让首尾不同时被抢呢? 要么算头[1, n-1], 要么算尾[2, n] 就可以保证了.


## DP Transform

- 思路步骤
1. 奇偶数的思考太麻烦, 不到万一不考虑
2. 由于首尾相连, 所以只需要避免第一个和最后一个同时 rob 就行了. 所以要么取[0, n-2] 要么 [1, n-1]
3. 由于主体程序中涉及到众多 i-1

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        numlen = len(nums)
        if numlen == 0:
            return 0
        if numlen == 1:
            return nums[0]

        dp1 = [0 for i in range(numlen)]
        dp2 = [0 for i in range(numlen)]

        # 通过 for 循环来控制范围比较方便
        for i in range(numlen-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        for i in range(1, numlen):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
            
        return max(dp1[-2], dp2[-1])

```



## DP 万精油


DFS + memo



