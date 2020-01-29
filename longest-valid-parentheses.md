


- https://leetcode.com/problems/longest-valid-parentheses/
  - 给定的字符串中只有"("或")",求左右对应的合法的长度(左右对应的算合法,应该不算嵌套的,而且貌似要连在一起)
  - [stack] 本题用stack是最简单的，遇到左括号就入栈**下标**，右括号就出栈,并计算下标之差即得长度。
  - https://leetcode.com/problems/longest-valid-parentheses/discuss/122694/dp-and-stack-c++-soluiton dp和stack都有
  - https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack 栈解法
