- [Intro](#intro)
- [Topics](#topics)
- [Greedy](#greedy)





## Intro

- https://leetcode.com/problems/candy/


There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively. The third child gets 1 candy because it satisfies the above two conditions.





## Topics

- `Greedy`
- `Code Trick`

## Greedy

- 一开始想着从左到右遍历, 遇到大的就+1; 然后再从右到左一遍, 这样都加起来就可以了. 但是遇到 [1, 2, 1] 的山丘会重复计算.
  - 其实, 这样想已经很接近解法了. 只要想办法避免这个重复计算的问题即可.
    - 通过 max() 就可以解决了, 如果`candies[i]`之前已经计算了, 那就肯定比周围的要高.

- [x] 本题难在哪里呢?
- [难点] 小山丘两边会重复计算.
- [解决办法] 第二次遍历的时候, 通过 max() 滤掉重复计算.


```py
class Solution:
    def candy(self, ratings: List[int]) -> int:
        rating_len = len(ratings)
        candies = [1 for i in range(rating_len)]

        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1

        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i]+1, candies[i-1]) # 这一句为什么这么神奇呢?
                # 其实, 这一句跟之前的循环是一样的, 都是遇到更大的数就+1: candies[i-1] = candies[i] + 1
                # 这不过这里用 max 过滤一下, 可以处理小山丘重复计算的问题

        return sum(candies)
```










