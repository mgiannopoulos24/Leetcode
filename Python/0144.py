from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                # Push right child first so that left child is processed first
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return result
