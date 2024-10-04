# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Helper function to recursively calculate the sum
        def dfs(node):
            if not node:
                return 0
            
            total_sum = 0
            
            # Check if the current node's value is within the range
            if low <= node.val <= high:
                total_sum += node.val
            
            # Traverse the left subtree if there's a possibility of values in the range
            if node.val > low:
                total_sum += dfs(node.left)
            
            # Traverse the right subtree if there's a possibility of values in the range
            if node.val < high:
                total_sum += dfs(node.right)
            
            return total_sum
        
        # Start the DFS from the root
        return dfs(root)