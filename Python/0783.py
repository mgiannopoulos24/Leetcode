# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Helper function for in-order traversal
        def in_order(node):
            if not node:
                return []
            return in_order(node.left) + [node.val] + in_order(node.right)
        
        # Get sorted values from in-order traversal
        sorted_values = in_order(root)
        
        # Initialize minimum difference as large number
        min_diff = sys.maxsize
        
        # Compute minimum difference between adjacent nodes
        for i in range(1, len(sorted_values)):
            min_diff = min(min_diff, sorted_values[i] - sorted_values[i - 1])
        
        return min_diff