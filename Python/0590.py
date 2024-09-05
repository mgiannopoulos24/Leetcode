from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)  # Visit all children
                result.append(node.val)  # Visit the node itself
        
        traverse(root)
        return result
