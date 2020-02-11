- [Intro](#intro)
- [Topics](#topics)
- [Queue Monotonous](#queue-monotonous)
- [DP](#dp)
- [Brute Force](#brute-force)

## Intro

- https://leetcode.com/problems/sliding-window-maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
Follow up:
Could you solve it in linear time?

## Topics

- `Heap`
- `Queue - Monotonous`
- `Sliding Window`
- `Dynamic Programming`

- 最优解是?

## Queue Monotonous

- https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/
- faster than 40%
- [核心] 基本思想跟 移动窗口 一样, 只不过利用了一个单调队列来处理最大值.

```py
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        monoq = MonotonousQueue()
        res = []
        for i in range(len(nums)):
            if i < k-1: # 初始化, 放入几个元素
                monoq.append_right(nums[i])
            else: # 然后每更新一次, 就是用单调队列 返回max
                monoq.append_right(nums[i])
                res.append(monoq.max()) # 不能pop出来
                monoq.pop_left(nums[i+1-k]) # 弹出窗口最前面的元素
        return res


class MonotonousQueue:
    def __init__(self):
        self.q = collections.deque()

    def append_right(self, ele): # 单调队列的核心函数: 每次入队的时候, 都保证把之前的小元素都扔掉
        while self.q and ele > self.q[-1]:
            del self.q[-1]

        self.q.append(ele)

    def max(self):
        return self.q[0]

    def pop_left(self, ele):
        if self.q and self.q[0] == ele:
            del self.q[0]
```



## DP

```py
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

```


## Brute Force

- 时间复杂度：O(Nk)。其中 N 为数组中元素个数。
- 空间复杂度：O(N−k+1)，用于输出数组。


```py
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        
        return [max(nums[i:i + k]) for i in range(n - k + 1)]
```

