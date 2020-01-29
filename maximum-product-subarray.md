

- 找到一个contiguous(连续) subarray,使其乘积最大. https://leetcode.com/problems/maximum-product-subarray/
  - https://www.cnblogs.com/grandyang/p/4028713.html

```py
def maxProduct(nums):
    numsLen = len(nums)
    dp = [0 for i in xrange(numsLen)]
    for i in xrange(2, numsLen):
        current_max = max(dp[i], nums[i-1]* nums[i])
```
