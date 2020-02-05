- [Intro](#intro)
- [Topics](#topics)
- [Math](#math)

## Intro

- https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



## Topics

- `Linked List`
- `Math`



## Math


- 两个链表数字, 相加 https://leetcode.com/problems/add-two-numbers/
- [点评分析] 本题为了简化, 都把数字逆序了, 所以考点就只剩下模拟进位了.
- 考点1: 模拟加法中的进位问题
- 考点2: 链表的基本操作
- [follow-up] 如果链表没有逆序怎么办? 我目前的想法是先 reverse 链表. 应该不能先加再 reverse 吧, 那样数学上会复杂很多.
  - 参考 https://www.geeksforgeeks.org/sum-of-two-linked-lists/


