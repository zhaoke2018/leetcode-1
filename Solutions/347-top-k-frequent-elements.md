- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)

## Intro

- https://leetcode.com/problems/top-k-frequent-elements

Given a non-empty array of integers, return the k most frequent elements.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:

Input: nums = [1], k = 1
Output: [1]

Note: 

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



## Topics

- `Hash Table`
- `Heap`


## Heap


- [通用思路]
  1. count = 统计各个数字出现的频率
  2. heap = heapify(count), 这里需要指定对频率建堆.
  3. 依次弹出 top k

- [Python思路] Python API 可以直接一句话搞定后两步.
  - [API解释] heapq 按照 keys() 来建立堆, 每建立一个元素, 就通过 get 去获取对应的value.

- [那个counter.get是啥]
  - 通过一番调查, 了解 heapify 只能处理 list, 因此第二个参数需要是一个 list.
  - counter 的结果就是一个 dict.
  - python 中的所有 dict 都可以通过 keys() 或者 values() 得到一个 list.
  - 通过 dir(Counter) 得知 get 确实是一个方法.
  - 然后我尝试着给 get() 一个参数, 发现确实可以返回指定的 value!!! (其实我应该看名字就想到作用的)


```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        res = heapq.nlargest(k, counter.keys(), key=counter.get)
        return res
```