# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        # Stack to maintain the path of nodes
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # Determine the depth of the current node by counting dashes
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Parse the value of the node
            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            # Create a new TreeNode with the parsed value
            node = TreeNode(value)
            
            # Ensure the node is inserted at the correct depth
            # If stack length is greater than the current depth, we need to pop to find the parent
            while len(stack) > depth:
                stack.pop()
            
            # If the stack is not empty, the last node in the stack is the parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Push the current node onto the stack
            stack.append(node)
        
        # The first element in the stack is the root of the tree
        return stack[0]