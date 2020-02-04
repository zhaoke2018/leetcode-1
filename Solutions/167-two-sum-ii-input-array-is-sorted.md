- [Intro](#intro)

## Intro

- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
  - 为什么 for 循环会超时?
  - 一个 while 搞定两个 for 循环,推广一下吧!


```py
# 使用两层循环会在数组很大的时候,超时,为什么呢?
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        mi = target - numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] == mi:
                return [i+1, j+1]

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]
```



## Topics

- `Array`
- `Two Pointers`
- `Binary Search`


## Hashhhhh

- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
  - 为什么 for 循环会超时?
  - 一个 while 搞定两个 for 循环,推广一下吧!


```py
# 使用两层循环会在数组很大的时候,超时,为什么呢?
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        mi = target - numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] == mi:
                return [i+1, j+1]

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]
```