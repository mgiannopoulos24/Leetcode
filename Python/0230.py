from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function for in-order traversal
        def in_order_traverse(node):
            if node is None:
                return
            # Traverse the left subtree
            yield from in_order_traverse(node.left)
            # Visit the current node
            yield node.val
            # Traverse the right subtree
            yield from in_order_traverse(node.right)
        
        # Create a generator for in-order traversal
        gen = in_order_traverse(root)
        # Get the k-th smallest element (1-indexed)
        kth_smallest = None
        for _ in range(k):
            kth_smallest = next(gen)
        
        return kth_smallest
