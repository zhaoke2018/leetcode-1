- [Intro](#intro)
- [Iteration By John](#iteration-by-john)

## Intro

- https://leetcode.com/problems/open-the-lock


You have a lock in front of you with 4 circular wheels.  Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.  The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.  Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.

Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1

Note:

The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.





## Topics

- `Breadth-first Search`


## Iteration By John

- Open the Lock 初始组合为0000, 避免一些死锁组合, 最少几步正确开锁?
- [思路] 遍历所有的可能性, 直到找到为止
- [关键点] 有一些死锁组合会挡住遍历, 如何解决这个问题?
- 
- [Python] 不能直接操作 string, 要转换成 list 来更新.
- [Python] deque 可以直接判断 in.
- [python] 新建文件的时候, 根目录 == 运行位置的目录.




- 典型的最短路径问题，当权重都为1时，BFS是最好的方式
- https://leetcode.com/problems/open-the-lock/discuss/110232/Accepted-PythonJava-BFS-+-how-to-avoid-TLE 解法好简单！🔥
- 其实我之前都想到了，无非就是append队列的时候，上一个和下一个都append进来，用一个visited记录就不会有指数增长的问题咯！关键词，visited防止指数增长。


```py

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        Q = collections.deque(["0000"])
        step = 0
        while step<4:
            step += 1
            for i in range(len(Q)):
                cur = Q.popleft()

                for i in range(4):
                    curRotate = self.rotate(cur, i) # 将表盘拨动一格
                    reRotate = self.reRotate(cur, i) # 减一格, 反手勾
                    if reRotate == target:
                        return step
                    if curRotate == target:
                        return step
                    elif curRotate not in deadends: # and curRotate not in Q:
                        Q.append(curRotate)
        return -1
    
    def rotate(self, cur, i):
        curli = list(cur)
        curli[i] = str((int(curli[i]) + 1) % 9) # 将表盘拨动一格
        return ''.join(curli)

    def reRotate(self, cur, i):
        curli = list(cur)
        curli[i] = str((int(curli[i]) - 1) % 9) # 将表盘拨动一格
        return ''.join(curli)
```


 # 将表盘拨动一格
        return ''.join(curli)
```


