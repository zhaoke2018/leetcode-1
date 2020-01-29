




## Intro

- 相邻的房子不能被抢,求最大抢劫收益 https://leetcode.com/problems/house-robber/ easy
  - 解题思路: 假设dp[i]为当前房子最大收益, 那么dp[i] = dp[i-1] or dp[i-2] + value[i]
  - 求一个累加的数字,看上去适合用dp.


## DP By John

```py
def robI(self, nums):
    numLen = len(nums)
    # 边界条件这么多,有什么改进的方法吗
    if numLen == 0:
        return 0
    if numLen <= 1:
        return nums[0]

    # 初始化dp
    dp = [0 for i in xrange(numLen)]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    # 不断按条件累加即可
    for i in xrange(2, numLen):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    return dp[-1]
```



## 记忆化搜素

- https://leetcode.com/problems/house-robber/discuss/246618/di-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-san-chong-fang-shi
- 从大到小, 所以会不断计算小问题.


















