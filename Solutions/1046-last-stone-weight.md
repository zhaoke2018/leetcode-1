- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)

## Intro

- https://leetcode.com/problems/last-stone-weight

We have a collection of rocks, each rock has a positive integer weight.
Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
 
Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000


## Topics

- `Heap`
- `Greedy`


## Heap

- [Heap] 建立 heap, 每次 pop 最大的两个元素相减, 并且将结果存回 heap, 循环 n-1 次, heap[-1] 就是留下的石头了.


```py
def lastStoneWeight(self, stones: List[int]) -> int:
    A = [-i for i in stones]
    heapq.heapify(A) # 对 list 自身变形?
    for i in range(len(A) - 1):
        x, y = heapq.heappop(A), heapq.heappop(A)
        heapq.heappush(A, -abs(x-y))
    return -A[0]
```




- 为什么注释的解法中, pop 出来的数据不是最大的两个呢? 为什么变为负数之后就正确了呢?
  - 应该是因为 heapq 默认的是最大堆.
  - heapq.heappop() 默认返回的是 `最小值`.

- 为什么是 range(len(pq)-1) 次, 而不是 while(len(pq))

```py
def lastStoneWeight(self, A: List[int]) -> int:
    pq = [-x for x in A]
    heapq.heapify(pq)
    for i in range(len(A) - 1):
        x, y = -heapq.heappop(pq), -heapq.heappop(pq)
        heapq.heappush(pq, -abs(x - y))
        print(x,y,'\n', pq)
    return -pq[0]   
```



