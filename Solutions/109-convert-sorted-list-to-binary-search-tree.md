- [Intro](#intro)

## Intro

- https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

- [Intro](#intro)
- [Recursion By John](#recursion-by-john)
- [Recursion by Caikehe](#recursion-by-caikehe)





## Intro


```py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 如果给的数组就好了, 直接获取中间, 然后递归
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
```




## Topics

- `Linked List`
- `Depth-first Search`


## Recursion By John

- https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35476/Share-my-JAVA-solution-1ms-very-short-and-concise.


- 高票Java再一次让我惊喜
- 递归里就两步
1. 找到中点
2. 继续递归，限定 head 和 tail


- 以下程序 Debug 过程
- 打印中点, 发现中点一直没变, 然后突然意识到计算中点需要把 tail 也传进去, 不然每次都获取的是整条的中点.


```py
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        self.build_bst(head, None) # 修改: 添加 return
        
    def build_bst(self, head, tail):
        if head == tail:
            return
        mid = self.find_mid(head)
        
        root = TreeNode(mid.val) #一直在这里报错 
        root.left = self.build_bst(head, mid)
        root.right = self.build_bst(mid.next, tail)
        return root
        
    def find_mid(self, head): # 修改: 添加 tail
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('中间就是', slow.val)
        return slow
```


以下是成功的版本

```py
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        return self.build_bst(head, None)
        
    def build_bst(self, head, tail):
        if head == tail:
            return
        mid = self.find_mid(head, tail)
        
        root = TreeNode(mid.val) #一直在这里报错 
        root.left = self.build_bst(head, mid)
        root.right = self.build_bst(mid.next, tail)
        return root
        
    def find_mid(self, head, tail):
        slow = fast = head
        while fast!=tail and fast.next!=tail:
            slow = slow.next
            fast = fast.next.next
        print('中间就是', slow.val)
        return slow
```











## Recursion by Caikehe


```py
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next # 如果fast 不是 next.next 就会导致tmp取不到val
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
```











