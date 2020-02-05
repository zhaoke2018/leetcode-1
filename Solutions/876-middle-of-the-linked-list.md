- [Intro](#intro)
- [Topics](#topics)
- [Convert to Array](#convert-to-array)
- [Two Pointers](#two-pointers)

## Intro

- https://leetcode.com/problems/middle-of-the-linked-list

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.


Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

 
Note:

The number of nodes in the given list will be between 1 and 100.






- https://leetcode.com/problems/middle-of-the-linked-list/




## Topics

- `Linked List`
- `Two Pointers`
- `Two Pointers - Fast Slow Pointers`






## Convert to Array

- [分析] 拿到题就要分奇偶两种情况. 通过双指针很容易解决奇数的情况.
- [Trap] 最后为什么返回的是一串链表? 因为数组里面存的就是链表元素
  
- Time=O(N), Space=O(N)


```py
def middleNode(self, head):
    A = [head]
    while A[-1].next:
        A.append(A[-1].next) # 依次把链表节点存入数组
    return A[len(A) / 2]
```



## Two Pointers

- Time=O(N), Space=O(1)


```py
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next: # 为什么不需要判断 next.next? 因为 tail.next 虽然是 None, 但也是存在的, 不会报错.
        slow = slow.next
        fast = fast.next.next
    return slow
```




