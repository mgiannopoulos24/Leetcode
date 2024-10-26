# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Initialize a variable to hold the sum of visited nodes
        self.sum_so_far = 0
        
        # Helper function to perform reverse in-order traversal
        def reverse_inorder(node):
            if not node:
                return
            
            # First, recurse on the right subtree
            reverse_inorder(node.right)
            
            # Update the current node's value
            self.sum_so_far += node.val
            node.val = self.sum_so_far
            
            # Then, recurse on the left subtree
            reverse_inorder(node.left)
        
        # Call the helper function starting from the root
        reverse_inorder(root)
        
        return root