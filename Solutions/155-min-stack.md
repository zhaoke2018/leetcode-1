- [Intro](#intro)
- [Topics](#topics)
- [Two Stacks](#two-stacks)
- [Linked List By xxx](#linked-list-by-xxx)

## Intro

- https://leetcode.com/problems/min-stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

 
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

 


## Topics

- `Stack`
- `Design`


## Two Stacks

- [思路] 使用两个 stack, 其中一个用来实现普通stack 的功能, 另一个用来记录最小值.
  - 对于每个加入的新元素, 只有在 new < old_min 的时候, 才把 new 加入到 min_stack 中, 否则继续把原来的 min 加入 min_stack 即可.


```py
class MinStack:

    def __init__(self):
        self.stack_element = [] # 支持 stack 的基本功能
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack_element.append(x)

        if not self.min_stack:
            self.min_stack.append(x)
            return
        
        if x <= self.min_stack[-1]: # 新元素比较小, 那最新的 min 就是新元素了
            self.min_stack.append(x)
        else: # 新元素较大, 那就抛弃
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack_element.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack_element[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
```


## Linked List By xxx

- 使用链表实现 https://leetcode.com/problems/min-stack/discuss/49010/Clean-6ms-Java-solution
  - 这种思路也不错, head 就是栈顶, 每个节点新增一个 min 指针, 跟上面一样, 只不过用链表而已.
  - 这种实现有种一一对应的感觉, 很踏实.







