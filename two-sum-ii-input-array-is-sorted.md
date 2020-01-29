
- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
  - 为什么 for 循环会超时?
  - 一个 while 搞定两个 for 循环,推广一下吧!


```py
# 使用两层循环会在数组很大的时候,超时,为什么呢?
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        mi = target - numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] == mi:
                return [i+1, j+1]

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]
```