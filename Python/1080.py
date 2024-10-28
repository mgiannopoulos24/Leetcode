# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # Helper function for postorder traversal
        def helper(node, curr_sum):
            # If node is None, return None (base case)
            if not node:
                return None
            
            # Update the current sum with the current node's value
            curr_sum += node.val
            
            # If it's a leaf node, check if the current sum is sufficient
            if not node.left and not node.right:
                return node if curr_sum >= limit else None
            
            # Recursively process left and right children
            node.left = helper(node.left, curr_sum)
            node.right = helper(node.right, curr_sum)
            
            # After processing children, check if the node should be pruned
            # A node can be pruned if both its left and right children are None
            if not node.left and not node.right:
                return None
            
            return node
        
        # Start postorder traversal from the root with initial sum of 0
        return helper(root, 0)