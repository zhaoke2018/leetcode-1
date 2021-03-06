- [Intro](#intro)

## Intro

- https://leetcode.com/problems/super-egg-drop

You are given K eggs, and you have access to a building with N floors from 1 to N. 
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
Your goal is to know with certainty what the value of F is.
What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?
 



Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.


Example 2:

Input: K = 2, N = 6
Output: 3


Example 3:

Input: K = 3, N = 14
Output: 4

 
Note:

1 <= K <= 100
1 <= N <= 10000





- https://leetcode.com/problems/super-egg-drop/ dp+binary search
  - 给egg个鸡蛋,以及floor个楼层,求在哪层F刚好不会坏?
  - Drop Egg. 两个鸡蛋,100层楼,假设鸡蛋在n层以下扔不会碎,在n层以上扔会碎,求出最坏情况下,要扔多少次才能求出n.
    - 假设最多需要扔的次数为r.蛋a用来走大步,蛋b用来走小步,暂定蛋a每隔10楼扔一次,如果碎了再用蛋b找出具体哪一层.所以如果是n<=10,r=10,如果n=100,则r=10+9=19.假设一共n层楼,有m个鸡蛋,怎么办呢?必须上dp了!
    - https://zhuanlan.zhihu.com/p/33898752 各种高级解法,dp只算是二级.
    - http://blog.csdn.net/weixin_40564421/article/details/78988078 史上最详细的dp教程
    - https://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
    - https://www.quora.com/What-is-the-solution-to-the-dropping-eggs-puzzle

  - https://www.cnblogs.com/yunlambert/p/10028865.html
  - https://www.zhihu.com/question/19690210


- https://leetcode.com/problems/regular-expression-matching/
  - 实现`.`,`*`功能,一个匹配任意字符,一个匹配任意次数.
  - 解题思路：



## Topics

- `Math`
- `Binary Search`
- `Dynamic Programming`


