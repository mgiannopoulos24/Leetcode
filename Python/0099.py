class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Helper function for in-order traversal
        def in_order_traversal(node: Optional[TreeNode]):
            nonlocal first, second, prev
            if not node:
                return
            
            # Traverse the left subtree
            in_order_traversal(node.left)
            
            # Check for swapped nodes
            if prev and node.val < prev.val:
                if not first:
                    # First time encountering an anomaly
                    first = prev
                # Always update the second node
                second = node
            
            # Update previous node
            prev = node
            
            # Traverse the right subtree
            in_order_traversal(node.right)
        
        # Initialize variables
        first = second = prev = None
        
        # Perform in-order traversal to find the two nodes that need to be swapped
        in_order_traversal(root)
        
        # Swap the values of the two nodes
        if first and second:
            first.val, second.val = second.val, first.val
