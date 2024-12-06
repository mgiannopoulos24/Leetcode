# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # A node is good if its value is greater than or equal to max_val on the path
            good = 1 if node.val >= max_val else 0
            
            # Update the maximum value on this path
            max_val = max(max_val, node.val)
            
            # Continue DFS on left and right children
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        # Start DFS with root and initial max_val as root's value
        return dfs(root, root.val)