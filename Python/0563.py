# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # This will store the total tilt of the entire tree
        total_tilt = 0
        
        def subtree_sum(node: TreeNode) -> int:
            nonlocal total_tilt
            if not node:
                return 0
            
            # Recursively calculate the sum of left and right subtrees
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)
            
            # Calculate the tilt for the current node
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt
            
            # Return the sum of values for the current subtree
            return node.val + left_sum + right_sum
        
        # Start DFS traversal from the root
        subtree_sum(root)
        
        return total_tilt