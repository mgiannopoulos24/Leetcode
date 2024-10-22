# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the current sum by shifting left and adding the current node's value
            current_sum = (current_sum << 1) | node.val
            
            # If it's a leaf, return the current sum as this is a complete path
            if not node.left and not node.right:
                return current_sum
            
            # Otherwise, continue the DFS traversal for both children
            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)
            
            # Return the sum of both left and right subtree results
            return left_sum + right_sum
        
        # Start DFS from the root with an initial sum of 0
        return dfs(root, 0)