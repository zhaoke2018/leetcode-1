- [Intro](#intro)
- [Topics](#topics)
- [Two Pointers](#two-pointers)

## Intro

- https://leetcode.com/problems/partition-list

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5



## Topics

- `Linked List`
- `Two Pointers`


## Two Pointers


- 这两个 pointer 其实只是充当缓存的作用而已, 并没有移动.
- 这个思路跟 quick sort 里的 partition 完全不一样, 不要被带笼子了.

```py
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first = first_head = ListNode(0)
        second = second_head= ListNode(0)
        
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else: # 大于等于的都会都后面去, 所以不用再接x了.
                second.next = head
                second = second.next
            head = head.next
        
        second.next = None
        first.next = second_head.next
        
        return first_head.next
```