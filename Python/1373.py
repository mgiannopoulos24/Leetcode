# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # This will store the maximum sum of a valid BST found
        self.max_sum = 0
        
        # Helper function that returns a tuple:
        # (is_bst, subtree_sum, min_val, max_val)
        def post_order(node):
            if not node:
                # An empty node is a valid BST with sum = 0, and arbitrary min/max values
                return (True, 0, float('inf'), float('-inf'))
            
            # Recursively process the left and right subtrees
            left_is_bst, left_sum, left_min, left_max = post_order(node.left)
            right_is_bst, right_sum, right_min, right_max = post_order(node.right)
            
            # Check if the current subtree is a valid BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                # This is a valid BST
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                
                # Return the updated values for this subtree
                return (True, current_sum, min(left_min, node.val), max(right_max, node.val))
            else:
                # If it's not a valid BST, we return False for is_bst and ignore the sum
                return (False, 0, 0, 0)
        
        # Start the post-order traversal from the root
        post_order(root)
        
        return self.max_sum
