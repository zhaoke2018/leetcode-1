- [Intro](#intro)
- [Topics](#topics)
- [Ordered Dict](#ordered-dict)
- [Other](#other)

## Intro

- https://leetcode.com/problems/lru-cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up:
Could you do both operations in O(1) time complexity?
Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

 


## Topics

- `Design`


## Ordered Dict

- Ordered Dict 就像是一个 stack or queue, 只不过存的元素都是 key-value. 因此, 新增一个同名元素并不会覆盖之前的, 而是会再加一个元素.

```py
from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key, last=True) # 用过的数据就移到最后, 看来弹出的都是前面的, 跟队列差不多.
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
```


## Other

- ordered dict 的实现原理是?
- 其他解法是不是就是 ordered dict 的实现原理? https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList