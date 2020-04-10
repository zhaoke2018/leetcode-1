- [Intro](#intro)
- [Topics](#topics)
- [Ordered Map](#ordered-map)
- [Bucket Sort](#bucket-sort)

## Intro

- https://leetcode.com/problems/contains-duplicate-iii

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true


Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true


Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false





## Topics

- `Sort`
- `Ordered Map`


## Ordered Map

- 这个好像涉及一些证明.....

```py
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False
```


## Bucket Sort


- 高赞回答都是 bucket sort.