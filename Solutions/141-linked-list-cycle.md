- [Intro](#intro)
- [Topics](#topics)
- [Hash](#hash)
- [Two Pointers](#two-pointers)

## Intro

- https://leetcode.com/problems/linked-list-cycle

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.




Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.




Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.



 
Follow up:
Can you solve it using O(1) (i.e. constant) memory?


## Topics

- `Hash`
- `Linked List`
- `Two Pointers`




- 判断是否有环(判断形状) https://leetcode.com/problems/linked-list-cycle/
  
  - `HashSet` 有环就肯定会走到原地, 那么遍历一圈就知道了. 


## Hash

```py
def hasCycle(self, head: ListNode) -> bool:
    cache = set()
    while head:
        if head in cache:
            return True
        else:
            cache.add(head)
        head = head.next
    return False
```



## Two Pointers

- a每次走一步,b每次走两步.如果链表是个环的话,他们会相遇的.

```py
def hasCycle(self, head: ListNode) -> bool:
    try:
        slow, fast = head, head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
```

