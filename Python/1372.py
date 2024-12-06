# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # To keep track of the longest ZigZag path length
        self.max_len = 0
        
        # Helper DFS function
        def dfs(node, direction, length):
            if not node:
                return
            
            # Update the maximum length
            self.max_len = max(self.max_len, length)
            
            # If direction is 0, go left, next we go right
            # If direction is 1, go right, next we go left
            if direction == 0:
                # Go left, and next move will be to the right
                dfs(node.left, 1, length + 1)
                # Start a new path to the right
                dfs(node.right, 0, 1)
            else:
                # Go right, and next move will be to the left
                dfs(node.right, 0, length + 1)
                # Start a new path to the left
                dfs(node.left, 1, 1)
        
        # Start DFS traversal
        dfs(root, 0, 0)  # Start going left
        dfs(root, 1, 0)  # Start going right
        
        return self.max_len
