- [Intro](#intro)
- [Topics](#topics)
- [Depth-First Search - Inorder - Iteration](#depth-first-search---inorder---iteration)
- [Morris](#morris)

## Intro

- https://leetcode.com/problems/binary-tree-inorder-traversal

Given a binary tree, return the inorder traversal of its nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?



## Topics

- `Hash Table`
- `Stack`
- `Tree`
- `Depth-First Search - Inorder - Iteration`


## Depth-First Search - Inorder - Iteration 

```py
def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    order = []
    cur = root
    
    while cur or len(stack):
        while cur != None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        order.append(cur.val)
        cur = cur.right
    
    return order
```


## Morris

- https://www.educative.io/edpresso/what-is-morris-traversal


```py
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left_node = None
		self.right_node = None

def Morris(root): 
	# Set current to root of binary tree 
	curr = root 
	
	while(curr is not None): 
		
		if curr.left_node is None: 
			print curr.data, 
			curr = curr.right_node 
		else: 
			# Find the previous (prev) of curr 
			prev = curr.left_node 
			while(prev.right_node is not None and prev.right_node != curr): 
				prev = prev.right_node 

			# Make curr as right child of its prev 
			if(prev.right_node is None): 
				prev.right_node = curr 
				curr = curr.left_node 
				
			# fix the right child of prev
			else: 
				prev.right_node = None
				print curr.data, 
				curr = curr.right_node 
			

root = Node(4) 
root.left_node = Node(2) 
root.right_node = Node(5) 
root.left_node.left_node = Node(1) 
root.left_node.right_node = Node(3) 

Morris(root) 
```


