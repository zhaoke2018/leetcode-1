



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
