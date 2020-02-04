- [Intro](#intro)

## Intro

- https://leetcode.com/problems/frog-jump

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.





## Intro

- https://leetcode.com/problems/frog-jump/


`*代表石头,~代表水流: **~~~~`

- dp记录到达当前位置的速度!
- 试试 python 的 defaultdict!
- 还有一道对比html树的题

```py
def canCrossRiver(river):
	currentSpeed = 1

	Speeds = [[]] * length(river) # 1-d 记录到达当前石头的可能速度
	For i in range(river):
		If river[i] == ‘*”:
			for s in speeds[i]:
				If i+s+1 > length(river):
					return True
				speeds[i+s-1].append(s-1)
speeds[i+s].append(s)
speeds[i+s+1].append(s+1)
	return False
```


Speeds = defaultdict(Set)


## Topics

- `Dynamic Programming`


## DP

```java
public class Solution {
    public boolean canCross(int[] stones) {
        HashMap<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < stones.length; i++) {
            map.put(stones[i], new HashSet<Integer>()); // 每一个石头都有对应一个 hash

        }
        map.get(0).add(0);
        for (int i = 0; i < stones.length; i++) {
            for (int k : map.get(stones[i])) {
                for (int step = k - 1; step <= k + 1; step++) {
                    if (step > 0 && map.containsKey(stones[i] + step)) {
                        map.get(stones[i] + step).add(step);
                    }
                }
            }
        }
        return map.get(stones[stones.length - 1]).size() > 0;
    }
}
```


```py
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp[i] 表示是否能到达第i个石头, 但是这样缺乏步长的信息, 因此, 还需要记录到达i时的步长.
        
```
