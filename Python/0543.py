# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1  # Return -1 for height calculation purposes
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the diameter with the sum of left and right subtree heights
            self.diameter = max(self.diameter, left_height + right_height + 2)
            
            # Return the height of the current node's subtree
            return max(left_height, right_height) + 1
        
        self.diameter = 0
        dfs(root)
        return self.diameter