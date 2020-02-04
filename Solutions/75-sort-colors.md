- [Intro](#intro)

## Intro

- https://leetcode.com/problems/sort-colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
	First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?













## Topics

- `Array`
- `Two Pointers`
- `Sort`


## Count


直接统计三种颜色的数量, 然后重写原数组

```py
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = collections.Counter(nums)
        
        step = 0
        for i in range(count[0]):
            nums[step] = 0
            step += 1
        for i in range(count[1]):
            nums[step] = 1
            step += 1
        for i in range(count[2]):
            nums[step] = 2
            step += 1

```