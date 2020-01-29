
- https://leetcode.com/problems/most-profit-assigning-work/
1. 任务有两个属性,difficulty[i]和profit[i]
2. 工人有一个属性,ability[i],表示ability[i]>difficulty[i],表示能够胜任.
3. 每个工人只能完成一个任务,而且只能完成任务难度比他能力小的.一个任务可以被多次完成(不是可被合作完成)
- 求最大的profit?

分析
- 根据规则3的限制,即可转化为,求总浪费最少.
- 同时,我们要优先完成profit[i]/difficulty[i]最大的. 👉 可是题目中所有的比率都一样.
- 既然不能合作,那很简单了,每个人遍历一下,找到他能获取的最大profit即可.



```py
# 就是把jobs 和 worker 按照能力从小到大排列,然后依次找每个工人能得到的最大profit而已,这样就能最优了?
# 不! 我在参数列表中举了一个例子,当比率不一样的时候,max_profit = 105
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int] difficulty[2, 4, 6, 8, 10]
        :type profit: List[int] profit = [10, 20, 30, 40, 55]
        :type worker: List[int] [4, 5, 6, 7]
        :rtype: int
        """
        jobs = zip(difficulty, profit) # zip成一个大对象
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker): # sorted() 从小到大
            while i < len(jobs) and skill >= jobs[i][0]: # 每个工人在while中找到他能获取的max_profit
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
```



- 这道题目应该类似 https://www.geeksforgeeks.org/weighted-job-scheduling/


