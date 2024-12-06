# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            
            # Sum for the current node, only if the grandparent is even
            total_sum = 0
            if grandparent is not None and grandparent % 2 == 0:
                total_sum += node.val
            
            # Continue DFS traversal for left and right children
            total_sum += dfs(node.left, node.val, parent)
            total_sum += dfs(node.right, node.val, parent)
            
            return total_sum
        
        # Initial call with no parent and no grandparent
        return dfs(root, None, None)