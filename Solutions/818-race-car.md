- [Intro](#intro)

## Intro

- https://leetcode.com/problems/race-car

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)
Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
When you get an instruction "A", your car does the following: position += speed, speed *= 2.
When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)
For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.
Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.


Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.

 
Note: 

1 <= target <= 10000.


- 车在数轴上运动,可以变速,可以倒车,请问到达某个点,最短的指令是几位(不是经过,而是刚好到达) https://leetcode.com/problems/race-car/
- `BFS解析` 每次要么 A 要么 R, 那就记住所有可能的 position 和 speed, 然后在里面选一个指令最短的
- `DP解析` 
  - https://www.cnblogs.com/grandyang/p/10360655.html
- `HeapQ解析` 
  - https://leetcode.com/problems/race-car/discuss/143993/Python-AC-BFS-and-Heapq-Solutions



## Topics

- `Dynamic Programming`
- `Heap`


