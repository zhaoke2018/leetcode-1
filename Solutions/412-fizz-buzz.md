- [Intro](#intro)
- [Topics](#topics)
- [Naive](#naive)
  - [DRY](#dry)
- [Hash](#hash)

## Intro

- https://leetcode.com/problems/fizz-buzz

Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]



## Topics



- 几种方法的复杂度都是一样的

- https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/

## Naive

- 经验: 先处理苛刻的条件!!!
  - 类似的还有, 先 return 一些奇怪的case.

```py
def fizzbuzz(n):
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append('FizzBuzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res
```

### DRY


- 重复的条件, 都统一表示

```py
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = ''
        for i in range(1, n+1):
            fizz = (i % 3) == 0
            buzz = (i % 5) == 0
            if fizz and buzz: res.append('fizzbuzz')
            elif fizz: res.append('fizz')
            elif buzz: res.append('buzz')
        return res

```

## Hash


```py


```