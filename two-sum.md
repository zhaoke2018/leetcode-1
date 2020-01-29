
- 从数组中找到两个数ab,使得a+b==target,返回ab的下标. https://leetcode.com/problems/two-sum/
  - `Hash` x = target - b,然后看 x 是否在数组中.
  - `brute force search`


```py
def twoSum(nums, target):
    # 全量缓存: 先将所有数字都 hash 起来
    cache = {}
    for index, value in enumerate(nums):
        cache[value] = index

    for index, value in enumerate(nums):
        complement = target - value
        if complement in cache and index != cache[complement]: # 注意不能等于本身!
            return [index, cache[complement]]

def twoSum(nums, target):
    # 增量缓存: 暂时没用到的数字才 hash 起来
    cache = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in cache:
            return [cache[complement], index]
        else:
            cache[complement] = index
```

```csharp
vector<int> twoSum(vector<int>& nums, int target) {
    // 本题需要返回下标,所以排序处理肯定不行.还是用经典的hash吧!找差值.
    unordered_map<int,int> map;
    vector<int> res;
    // 将给定的数组存到hashmap里面.
    for(int i=0;i<nums.size();i++){
        map[nums[i]] = i;
    }
    // 从map里面查找差值.
    for(int i=0;i<nums.size();i++){
        int gap = target - nums[i];
        // 找到了&&不是本身 就算一组解
        if(map.find(gap)!=map.end() && map[gap]!=i){
            res.push_back(i);
            res.push_back(map[gap]);
            break; // 题意帮我们限定了只有一组解
        }
    }
    return res;
}
```
