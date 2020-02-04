- [Intro](#intro)
- [Two Pointers](#two-pointers)

## Intro

- https://leetcode.com/problems/binary-search

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 
Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].



## Topics

- `Binary Search`


## Two Pointers


```py
# 虽然有lr显得麻烦,但只有这样才能找到真实下标
def binarySearch(arr, l, r, key):
  if key > arr[-1] or key < arr[0] or l >= r:
    return 'Not in array'
  mid = (r - l) / 2 + l
  print "Searching " + str(key) + " in " + str(arr) + ' ---- mid: ' + str(mid)
  if arr[mid] == key:
    return mid
  elif arr[mid] > key:
    return binarySearch(arr, l, mid-1, key) # 为什么一定要return?
  else:
    return binarySearch(arr, mid+1, r, key) # 这两句可能造成 l >= r, 从而进入死循环

listo = [11,12,13,14,15,16,18,19,110]

print binarySearch(listo, 0, 10, 17)
```


二分查找法
- 先判断刚好找到的情况,因为这样可以减少其他判断直接返回.
- 三个判断搞定之后,再考虑一下边界情况,`if(l<r)`.
- 给定的条件如果仅有一个数组和一个key怎么办呢?在C++里面如何得到subarray呢?

```csharp
// binary search
int binary_search(int[] nums,int l, int r, int key){
    int mid = l + nums.size() / 2;
    if(key == nums[mid]){
        return mid;
    }else if(key > nums[mid]){
        return binary_search(nums, l, mid, key);
    }else{
        return binary_search(nums, mid, r, key);
    }
}
```
