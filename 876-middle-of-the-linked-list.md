


- https://leetcode.com/problems/middle-of-the-linked-list/



## 快慢指针


```py
class Solution:
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
```


## 转化为数组


```py
class Solution:
    def middleNode(self, head):
        A = [head] # 存的是节点
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2] # 最后返回的也是节点
```




```py

```