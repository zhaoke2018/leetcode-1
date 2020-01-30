- [Intro](#intro)

## Intro

- https://leetcode.com/problems/basic-calculator

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.






## Intro

- https://leetcode.com/problems/basic-calculator/
- [Stack+String_Reversal思路] 由于减号的存在, 因此 string 入栈前, 需要reverse 一下.
- [Stack思路] ...等我练习 stack 的时候再来看...




## Stack + String Reversal


```py
class Solution:

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res       

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':         
                    res = self.evaluate_expr(stack)
                    stack.pop()        

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)
```




## Stack on the go

```py
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand
```


## Others


```py
import re
class Solution:
    def calculate(self, s):
        s = s.replace(" ","")
        
        def rec_nb(s): # when no bracket
            if s.find('+') == -1 and s.find('-') == -1:
                return int(s)
            else:
                if s[0] == '-':
                    s = '0'+s
                num = re.split('\+|\-',s)
                sign_pos = []
                for i in range(len(s)):
                    if s[i] == '+' or s[i] == '-':
                        sign_pos.append((i,s[i]))
                res = int(num[0])
                for i in range(len(sign_pos)):
                    if sign_pos[i][1] == '+':
                        res += int(num[i+1])
                    else:
                        res -= int(num[i+1])
                return res
            
        def rec(s): # when considering bracket
            if s.find(')') == -1:
                return rec_nb(s)
            else:
                r = s.find(')')
                l = r-1
                while(1):
                    if s[l] == '(':
                        break
                    else:
                        l -= 1
                mid = str(rec_nb(s[l+1:r]))
                ls = s[:l]
                if mid[0] == '-' and ls!="" and (ls[-1] == "+" or ls[-1] == '-'):
                    mid = mid[1:]
                    if ls[-1] == '+':
                        ls = ls[:-1]+'-'
                    else:
                        ls = ls[:-1]+'+'
                    
                new_s = ls + mid + s[r+1:]
                return rec(new_s)
                             
        return rec(s)
```