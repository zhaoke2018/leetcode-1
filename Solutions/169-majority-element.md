- [Intro](#intro)
- [Topics](#topics)
- [Hash](#hash)
- [Divide and Conquer](#divide-and-conquer)
- [Boyer Moore Majority Vote algorithm](#boyer-moore-majority-vote-algorithm)

## Intro

- https://leetcode.com/problems/majority-element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2



## Topics

- `Array`
- `Divide and Conquer`
- `Bit Manipulation`
- `Boyer Moore Majority Vote algorithm`
- `Multiple Methods`

- https://leetcode.com/problems/majority-element/discuss/51612/6-Suggested-Solutions-in-C++-with-Explanations

## Hash

```py
def majorityElements(arr):
    counter = collections.Counter(arr)
    return max(counter.keys(), key=counter.get()) # keys 
```


## Divide and Conquer

```py
def majorityElement(nums):
    pass
```

## Boyer Moore Majority Vote algorithm

```py
# 本解法非常通用
def majorityElement_boyerMoore(nums):
    temp,count = 0
    for i in nums:
        if i == 0:
            temp = i
            count = 1
        elif x == temp:
            count += 1
        else:
            count -= 1
    print temp
```

