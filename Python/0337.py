from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return (0, 0)
            
            # Recursively solve for left and right children
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # If we rob this node, we cannot rob its children
            rob_current = node.val + left_skip + right_skip
            
            # If we do not rob this node, we take the maximum money from children
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_current, skip_current)
        
        # Calculate the result for the root node
        rob_root, skip_root = dfs(root)
        
        # The maximum amount we can rob is the max of robbing or skipping the root
        return max(rob_root, skip_root)
