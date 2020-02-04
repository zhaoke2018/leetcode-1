- [Intro](#intro)

## Intro

- https://leetcode.com/problems/maximum-product-subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


- 找到一个contiguous(连续) subarray,使其乘积最大. https://leetcode.com/problems/maximum-product-subarray/
  - https://www.cnblogs.com/grandyang/p/4028713.html

```py
def maxProduct(nums):
    numsLen = len(nums)
    dp = [0 for i in xrange(numsLen)]
    for i in xrange(2, numsLen):
        current_max = max(dp[i], nums[i-1]* nums[i])
```




## DP?

- 找到一个contiguous(连续) subarray,使其乘积最大. https://leetcode.com/problems/maximum-product-subarray/
  - https://www.cnblogs.com/grandyang/p/4028713.html

```py
def maxProduct(nums):
    numsLen = len(nums)
    dp = [0 for i in xrange(numsLen)]
    for i in xrange(2, numsLen):
        current_max = max(dp[i], nums[i-1]* nums[i])
```


## Topics

- `Array`
- `Dynamic Programming`


