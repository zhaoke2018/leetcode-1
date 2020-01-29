
- https://leetcode.com/problems/evaluate-reverse-polish-notation/
  - 翻译式解题就行,没有涉及到任何算法思想.
  - 需要注意的就是 
    - Python 除法在涉及到负数的时候有个坑.
    - Python 没有 switch case 语句.


- 应用: 实现recursion.
- 特点: 优先处理最近一次记录.


```py
def evalRPN(tokens: List[str]) -> int:
    operators = ['+', '-', '*', '/']
    stack = []
    for token in tokens: # 遍历 tokens
        if token in operators: # 见到运算符, 就 pop 2 from stack
            b = stack.pop()
            a = stack.pop()

            if token is '+': # 运算
                res = a + b
            elif token is '-':
                res = a - b
            elif token is '*':
                res = a * b
            elif token is '/':
                res = int(a / b)

            stack.append(res) # 并将结果存回去
        else: # 见到数字, 就 enstack
            stack.append(int(token))
    return stack[-1]
```
