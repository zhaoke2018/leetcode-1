



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




## Greedy

找到最小评分的, 然后周围的都加

```py
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candi = ratings[:]
        candi[0] = mini = curr = 0 # mini 用来记录最小值
        for i in range(11, len(ratings)):
            if ratings[i] > ratings[i-1]:
                mini += 1
                candi[i] = mini
            elif ratings[i] < ratings[i-1]:
                mini



```

## DP









