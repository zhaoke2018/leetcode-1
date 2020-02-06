- [Intro](#intro)
- [Topics](#topics)
- [DP](#dp)
- [Stack](#stack)
- [Two Pointers](#two-pointers)

## Intro

- https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6





## Topics

- `Array`
- `Two Pointers`
- `Stack`
- `Dynamic Programming`

- 哪个是最优解?

## DP

- 思路重点: 每个坑能够装多少水, 取决于左右两边较矮的那一个.
- [WHY] 这也算 DP 吗? Leetcode 是这么算的.

```py
class Solution:
    def trap(self, height: List[int]) -> int:
        hlen = len(height)
        traping = [0 for i in range(hlen)]
        
        # 计算出左右的护栏高度
        left_max, right_max = [0 for i in range(hlen)], [0 for i in range(hlen)] # 如果连等于的话, 会共用一个对象!
        left_max[0], right_max[hlen-1] = height[0], height[hlen-1] # 初始化护栏
        for i in range(hlen):
            left_max[i] = max(left_max[i-1], height[i])
        for j in range(hlen-2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j])
          
        # 对于每一个坑, 通过短板原理min(left, right), 得到每个坑的容量
        for hole in range(1, hlen-1):
            iwater = min(left_max[hole-1], right_max[hole+1]) - height[hole]
            traping[hole] = iwater if iwater > 0 else 0 # 如果护栏不算两端的话, 就不需要这句话了
        
        # print(traping)

        return sum(traping)
```



```cpp
// dynamic programming
int trap(vector<int>& height)
{
	if(height == null)
		  return 0;
  int ans = 0;
  int size = height.size();
  vector<int> left_max(size), right_max(size);
  left_max[0] = height[0];
  for (int i = 1; i < size; i++) {
      left_max[i] = max(height[i], left_max[i - 1]);
  }
  right_max[size - 1] = height[size - 1];
  for (int i = size - 2; i >= 0; i--) {
      right_max[i] = max(height[i], right_max[i + 1]);
  }
  for (int i = 1; i < size - 1; i++) {
      ans += min(left_max[i], right_max[i]) - height[i];
  }
  return ans;
}
```


## Stack





```cpp
// stack
int trap(vector<int>& height)
{
    int ans = 0, current = 0;
    stack<int> st;
    while (current < height.size()) {
        while (!st.empty() && height[current] > height[st.top()]) {
            int top = st.top();
            st.pop();
            if (st.empty())
                break;
            int distance = current - st.top() - 1;
            int bounded_height = min(height[current], height[st.top()]) - height[top];
            ans += distance * bounded_height;
        }
        st.push(current++);
    }
    return ans;
}
```



## Two Pointers

- `Two pointers` 对于i, 只要直到 left_maxHeight 和 right_maxHeight, 就能算出能收集多少雨水了.
- 两边轮流移动, 始终保持两边差不多高.
  - 比如 left=2 的时候, 那么 right=2 以内的坑都可以装水的.
  - Two pointers 时间复杂度跟其他方法一样, 但是空间复杂度最佳.


























