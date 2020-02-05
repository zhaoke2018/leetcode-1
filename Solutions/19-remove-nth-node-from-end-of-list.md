- [Intro](#intro)
- [Topics](#topics)
- [Two Pointers](#two-pointers)

## Intro

- https://leetcode.com/problems/remove-nth-node-from-end-of-list

Given a linked list, remove the n-th node from the end of list and return its head.
Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?


## Topics

- `Linked List`
- `Two Pointers`
- `Two Pointers - Fast Slow Pointers`


## Two Pointers

```py
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        statichead = fast = slow = ListNode(0)
        statichead.next = head # 建立 dummy node,初始化
        
        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next # 这不是删除!
        return statichead.next
```