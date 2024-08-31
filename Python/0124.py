# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the global maximum path sum
        self.global_max = float('-inf')
        
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Compute the maximum path sum on the left and right subtrees
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # Compute the maximum path sum including the current node
            current_max = node.val + left_max + right_max
            
            # Update the global maximum path sum
            self.global_max = max(self.global_max, current_max)
            
            # Return the maximum path sum that includes the current node
            return node.val + max(left_max, right_max)
        
        # Start DFS from the root
        dfs(root)
        return self.global_max