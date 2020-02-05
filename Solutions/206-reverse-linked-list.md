- [Intro](#intro)
- [Topics](#topics)
- [Recursion](#recursion)
- [Iteration](#iteration)

## Intro

- https://leetcode.com/problems/reverse-linked-list

Reverse a singly linked list.
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?


## Topics

- `Linked List`
- `Hard - John`



## Recursion


- [看图理解单链表的反转](http://blog.csdn.net/feliciafay/article/details/6841115)
- 递归需要系统堆栈，所以空间消耗要比非递归代码要大很多.
- 递归的特点是一直往栈里压，然后才从尾到头一步步执行函数体，非常直观。


```csharp
ListNode* reverseList(ListNode* head) {
    if (!head || !head->next) return head; // 先写结束条件,当前节点不存在(?)了,就算转置完了.
    ListNode *p = head;
    head = reverseList(p->next); // 所有递归的关键思路: 这里直接到链表底部!!
    p->next->next = p; // 关键: 下家的next指针指回自己.
    p->next = NULL;
    return head;
}
```




## Iteration



```csharp
ListNode* reverseList(ListNode* head) {
    ListNode *next = NULL; // 这个next和pre是调换前位置的名字.用来固定相对节点,方便指来指去.
    ListNode *pre = NULL; // 这个初始化妙!
    while(head != NULL){
        // 每次循环只需要处理一个->next指向即可,不用两头都处理.
        next = head->next;
        head->next = pre; // 关键一指,将->next指向之前的上家.
        pre = head;
        head = next;
    }
    return pre;
    // 从本题可以总结出一种写程序的方式,先写关键的一个操作,然后根据操作补足条件!
}
```
