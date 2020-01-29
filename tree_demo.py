# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sumi: int) -> int:
        # store all path 
        def bt(node, stage):
            if not node:
                # TODO 无子节点已经处理过了, 怎么还会走这里呢?
                # print('这句应该只有[]才会用到 gabage path', stage) # 按理说, 只有遍历到叶子, 才会走这个逻辑
                return

            # TODO 为什么结尾的3会计算两次呢?
            if sum(stage)+node.val == sumi:
                stage.append(node.val)
                # print('结束2 - Found path at node!!!:', node.val, stage)
                res.append(stage)
                return
            
            if not node.left and not node.right:
                stage.append(node.val)
                print('结束1 - 没有子节点', stage) # 没错!
                return

            # 开张啦!
            bt(node.left, stage+[node.val])
            bt(node.right, stage+[node.val])
            
            # 给所有节点一个开张的机会
            bt(node.left, [])
            bt(node.right, [])

        res = []
        bt(root, [])
        print(res)
        return len(res)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            sum = int(line);
            
            ret = Solution().pathSum(root, sum)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    # main()
    root = stringToTreeNode('[1,-2,-3,5,3,-6,null,-7]')
    ret = Solution().pathSum(root, 3)