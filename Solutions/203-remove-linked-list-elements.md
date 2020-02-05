- [Intro](#intro)
- [Topics](#topics)
- [Recursion](#recursion)

## Intro

- https://leetcode.com/problems/remove-linked-list-elements

Remove all elements from a linked list of integers that have value val.
Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5



## Topics

- `Linked List`
- `Recursion`


## Recursion


```py
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        head.next = self.removeElements(head.next, val) # 直接递归到底
        
        if head.val == val:
            return head.next
        else:
            return head
```