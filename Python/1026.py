# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Helper function for DFS traversal
        def dfs(node, current_min, current_max):
            if not node:
                return current_max - current_min
            
            # Update current min and max based on the current node's value
            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)
            
            # Recur for left and right children
            left_diff = dfs(node.left, current_min, current_max)
            right_diff = dfs(node.right, current_min, current_max)
            
            # Return the maximum difference found in the subtree
            return max(left_diff, right_diff)
        
        # Start DFS from the root, using the root's value as both min and max
        return dfs(root, root.val, root.val)