"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Base case: If the root is None, return an empty list
        if not root:
            return []
        
        # Use a stack for iterative traversal
        stack = [root]
        result = []
        
        # Process nodes in preorder using the stack
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Add children to stack in reverse order
            stack.extend(reversed(node.children))
        
        return result