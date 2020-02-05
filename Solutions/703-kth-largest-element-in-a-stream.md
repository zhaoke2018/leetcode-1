- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)

## Intro

- https://leetcode.com/problems/kth-largest-element-in-a-stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.


## Topics

- `Heap`

## Heap

```py
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.hp = nums
        self.k = k
        heapq.heapify(self.hp)
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        if len(self.hp) < self.k:
            heapq.heappush(self.hp, val) # 初始化可能为空
        elif val > self.hp[0]:
            heapq.heapreplace(self.hp, val)
        return self.hp[0]
```


