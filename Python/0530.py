# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order_traversal(node: Optional[TreeNode]):
            """Generate the in-order traversal of the BST."""
            if node:
                # Traverse the left subtree
                yield from in_order_traversal(node.left)
                # Yield the current node's value
                yield node.val
                # Traverse the right subtree
                yield from in_order_traversal(node.right)
        
        # Initialize variables to track minimum difference
        prev_value = -1
        min_diff = sys.maxsize
        
        # Traverse the tree in in-order and calculate differences
        for value in in_order_traversal(root):
            if prev_value != -1:
                min_diff = min(min_diff, abs(value - prev_value))
            prev_value = value
        
        return min_diff