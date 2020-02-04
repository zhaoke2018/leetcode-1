- [Intro](#intro)

## Intro

- https://leetcode.com/problems/house-robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.






## Intro

- 相邻的房子不能被抢,求最大抢劫收益 https://leetcode.com/problems/house-robber/ easy
  - 解题思路: 假设dp[i]为当前房子最大收益, 那么dp[i] = dp[i-1] or dp[i-2] + value[i]
  - 求一个累加的数字,看上去适合用dp.



## Topics

- `Dynamic Programming`


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


















