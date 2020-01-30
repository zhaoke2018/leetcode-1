- [Intro](#intro)

## Intro

- https://leetcode.com/problems/maximum-subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

- 题意: 从数组nums[n]中,选出一段连续的subarray,使得这个subarray之和最大. https://leetcode.com/problems/maximum-subarray/
  - 解题思路[DP]: 以一个浮动窗口window不断计算局部最大的subarray,然后再用一个全局变量对比所有的window,从而得到全局最大.
  - 这道题精华思想就是,将注意力放在局部最优的求法上就可以了.全局只需要多一个变量即可搞定.
  - [x] 为什么以i为核心，而不是以sum为核心？ `max(window_max, window_max+i)` 以window_max为核心，i的加入是可选的，所以永远只有第一段.`Max(i, window_max+i)` 以i为核心，window_max的加入是可选的，所以**永远有另立门户的能力**.
  - [x] global_max为什么不能初始化为0? global_max可能为负.
  - [x] 为什么要两个max？第一个max用来记录current最长，第二个max用来global最长。
  - [x] 第一个max貌似无法处理低谷情形? 可以,注意跟sum+i进行max的是i,而不是sum,所以每一次i(包括低谷)都会计算进来,直到耗尽而另立门户.

```py
def maxSubArray(self, nums):
    global_max, window_max = -sys.maxint, 0
    for i in nums:
        window_max = max(i, window_max+i) # 局部最大
        global_max = max(window_max, global_max) # 全局最大
    return global_max
```

- 解题思路[DivConq]: Brute force,从i(0~n)开始算出当下的max_subarr,然后里面最大的那个即为所求.




## DP

- 题意: 从数组nums[n]中,选出一段连续的subarray,使得这个subarray之和最大. https://leetcode.com/problems/maximum-subarray/
  - 解题思路[DP]: 以一个浮动窗口window不断计算局部最大的subarray,然后再用一个全局变量对比所有的window,从而得到全局最大.
  - 这道题精华思想就是,将注意力放在局部最优的求法上就可以了.全局只需要多一个变量即可搞定.
  - [x] 为什么以i为核心，而不是以sum为核心？ `max(window_max, window_max+i)` 以window_max为核心，i的加入是可选的，所以永远只有第一段.`Max(i, window_max+i)` 以i为核心，window_max的加入是可选的，所以**永远有另立门户的能力**.
  - [x] global_max为什么不能初始化为0? global_max可能为负.
  - [x] 为什么要两个max？第一个max用来记录current最长，第二个max用来global最长。
  - [x] 第一个max貌似无法处理低谷情形? 可以,注意跟sum+i进行max的是i,而不是sum,所以每一次i(包括低谷)都会计算进来,直到耗尽而另立门户.

```py
def maxSubArray(self, nums):
    global_max, window_max = -sys.maxint, 0
    for i in nums:
        window_max = max(i, window_max+i) # 局部最大
        global_max = max(window_max, global_max) # 全局最大
    return global_max
```

- 解题思路[DivConq]: Brute force,从i(0~n)开始算出当下的max_subarr,然后里面最大的那个即为所求.

