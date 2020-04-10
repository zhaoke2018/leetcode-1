- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)
- [Sort](#sort)

## Intro

- https://leetcode.com/problems/top-k-frequent-words

Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:

Try to solve it in O(n log k) time and O(n) extra space.



## Topics

- `Hash Table`
- `Heap`
- `Trie`


## Heap

- [Heap知识点] heapify 是对对象原地建立联系的, 不需要赋值给一个新对象.
- [Python知识点] python min heap. 若要建立最大堆, 只能取相反数.
- [Python知识点] heap 确实会自动处理 tuple 的排序, 包括 -freq 和 word.

```py
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```


## Sort

- [Python知识点] dict_key is not subscriptable, 需要转换成 list 才行.
- [python知识点] sorted 排序的结果需要承接一下.

```py
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys() # 只获取单词, 此时已经按照频率排序了
        candidates = sorted(candidates, key=lambda w: (-count[w], w)) # 这个 (-count[w], w) 的tuple, 就跟上面 heapify 的对象一样.
        res = list(candidates)
        return res[:k]
```
