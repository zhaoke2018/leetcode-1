- [Intro](#intro)

## Intro

- https://leetcode.com/problems/palindrome-linked-list

Given a singly linked list, determine if it is a palindrome.
Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?








## Intro



- 检测单链表是否回文 https://leetcode.com/problems/palindrome-linked-list/
- [分析] 回文必定是两端进行比较的(或者是从中间到两端进行对比), 而单链表必然是单向的. 因此要解决这个矛盾, 就必须将单链表进行处理一下.
  - 要么将前半段转置.
  - 要么利用额外的空间, 将前半段入栈.
- [陷阱] 奇数和偶数节点是否需要分开处理呢?
- [疑问] 是否可以直接转化成数组呢?

- 考点
1. 链表性质与回文的矛盾分析.
2. 链表快慢指针折半处理.
3. 链表转置 or 栈的使用.
  - 转置无需额外空间.
  - 栈写起来简单.





## Topics

- `Linked List`
- `Two Pointers`


