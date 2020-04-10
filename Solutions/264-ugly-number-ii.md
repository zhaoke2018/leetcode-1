- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)
- [DP](#dp)
- [BiSect](#bisect)

## Intro

- https://leetcode.com/problems/ugly-number-ii

Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.


## Topics

- `Math`
- `Dynamic Programming`
- `Heap`
- `BiSect`



## Heap

```py
class Solution:
    def nthUglyNumber(self, n: int) -> int:
    	N, m, S = [1], 1, set()
    	for _ in range(n):
    		while m in S: m = heapq.heappop(N)
    		S.add(m)
    		for i in [2,3,5]: heapq.heappush(N,i*m)
    	return m
```


## DP

- [主要思路]
```py
class Solution:
    def nthUglyNumber(self, n: int) -> int:
    	N, p, I = [1], [2,3,5], [0]*3
    	for _ in range(n-1):
    		N.append(min([N[I[i]]*p[i] for i in range(3)]))
    		for i in range(3): I[i] += N[I[i]]*p[i] == N[-1]
    	return N[-1]
```
## BiSect

- [什么是bisect]
- [主要思路]


```py
class Solution:
    def nthUglyNumber(self, n: int) -> int:
    	N, I = [1], {2:0, 3:0, 5:0}
    	for _ in range(n-1):
    		I = {i:bisect.bisect(N, N[-1]//i, I[i]) for i in [2,3,5]}
    		N.append(min(N[I[2]]*2,N[I[3]]*3,N[I[5]]*5))
    	return N[-1]
```