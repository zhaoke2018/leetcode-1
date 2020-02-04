- [Intro](#intro)

## Intro

- https://leetcode.com/problems/brick-wall

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks. 
 
Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

Explanation: 


 
Note:

The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.


- 找出一条路径,使得横穿的bricks最少.输入墙体每行的砖块长度. https://leetcode.com/problems/brick-wall/
  - `外行解法` 想要横穿的bricks最少,那么找到缝隙最多的坐标即可.
    - `step` wall_increment = 以最左为起点,将每行的砖块坐标累加.
    - `step` index_set = 去掉 wall_increment 每行最后一个坐标(因为他们肯定一样),然后统一加入一个set
    - `step` most_frequent_times = 统计 index_set 出现次数最多的下标
    - `step` return len(wall) - most_frequent_times
  - `hash` 将上一个解法中,获取的 wall_increment 都放到一个 hash 中,然后通过 hash 找 most_frequent_times,而不是 counter.


```py
def leastBricks_simple(wall):
    from collections import Counter

    # step 将每行的长度累加
    for i in xrange(len(wall)):
        # optimize 这里只累加到len-1,可以提升4ms
        for j in xrange(1, len(wall[i])-1):
            wall[i][j] += wall[i][j-1]

    # step 每行去掉尾巴,统计所有数字出现最多的次数
    bricks = [brick for line in wall for brick in line[:-1]] 

    # step return 总行数 - 最多次数
    count = Counter(bricks)
    # error 如果每行都只有一个元素的话,上一步会slice掉最后的元素,那这里数组就为空了.
    try:
        most_frequent = count.most_common()[0][1] # note (a, b) a是出现的元素,b是出现的次数
    except IndexError:
        most_frequent = 0
    return len(wall) - most_frequent

def leastBricks_hash(wall):
    pass
```




- 然后领略一下hash table的魅力吧!
  - hashtable 自带统计次数的功能

```py
# 难道这就是python的hashtable????
def leastBricks(self, wall):
    rims = collections.Counter()
    for bricks in wall:
        cnt = 0
        for b in bricks:
            if cnt: rims[cnt] += 1
            cnt += b
    return len(wall) - max(rims.values() or [0])
```





- 顺便欣赏一下c++的hashtable

```csharp
// 形参为什么带&? 因为这是一个引用
int leastBricks(vector<vector<int>>& wall) {
    int mx = 0;
    unordered_map<int, int> m; // CPP的范型对新手来说,略别扭
    for (auto a : wall) { // auto 好像是不管什么类型都可以遍历
        int sum = 0;
        for (int i = 0; i < a.size() - 1; ++i) {
            sum += a[i];
            ++m[sum]; // sum下标的值++,突然发现hashtable好像就是一个 dict 呀!
            mx = max(mx, m[sum]);
        }
    }
    return wall.size() - mx;
}
```


一个对比
- python without hashtable 90ms, faster than 30.96% of Python online submissions for Brick Wall.
- python with hashtable ?
- c++ with hashtable 40ms, faster than 91.96% of C++ online submissions for Brick Wall.


## Topics

- `Hash Table`


