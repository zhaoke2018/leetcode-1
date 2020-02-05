- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)
- [Divide and Conquer](#divide-and-conquer)
- [Brute Force](#brute-force)

## Intro

- https://leetcode.com/problems/merge-k-sorted-lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6



## Topics

- `Linked List`
- `Divide and Conquer`
- `Heap`



## Heap

- [Heap] 将 (Head value + list) heapify, 然后不断 pop.

```py
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 为什么 priority queue? 将每个 list 整个加入 heap, 首元素会按顺序排列
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l)) # why两个括号? 每次存入 tuple
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node)) # 取出首元素后,把之后的 list 放回 Q 里面
        
        return head.next
```


## Divide and Conquer

- [DivideConquer] 不断将 lists 两两 merge.


```py
class Solution:
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval]) # 注意, 这里将结果存回原list, 用 interval 控制操作对象.
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2): # 这就是一个经典的 merge sort
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
```

## Brute Force

- [BruteForce] 把所有节点都放到一个集合中, 然后排序输出.(空间占用太大)