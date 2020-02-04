- [Intro](#intro)

## Intro

- https://leetcode.com/problems/reconstruct-itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.





## Topics

- `Depth-first Search`
- `Graph`


## Basic

- https://leetcode.com/problems/reconstruct-itinerary/

- [陷阱] JFK 可能飞往多地, 要选一个排序最小的
  - 解决办法: 提前排序.

- https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++

- 直接一个个找就可以了。
- Lexical order 可以通过 排序 来实现。
- 可以通过hash加快查找速度。




## Loop




## Hierholzer's algorithm

+ min heap

- https://leetcode.com/problems/reconstruct-itinerary/discuss/78766/Share-my-solution