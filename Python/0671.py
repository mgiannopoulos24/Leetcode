# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Initialize the smallest and second smallest values
        self.first_min = float('inf')
        self.second_min = float('inf')
        
        # Helper function for DFS traversal
        def dfs(node):
            if not node:
                return
            
            # Update the smallest and second smallest values
            if node.val < self.first_min:
                self.second_min = self.first_min
                self.first_min = node.val
            elif self.first_min < node.val < self.second_min:
                self.second_min = node.val
            
            # Continue DFS traversal
            dfs(node.left)
            dfs(node.right)
        
        # Start DFS traversal from the root
        dfs(root)
        
        # If the second minimum hasn't been updated, return -1
        return self.second_min if self.second_min < float('inf') else -1