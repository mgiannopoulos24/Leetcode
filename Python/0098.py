class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
            
            # Check if current node's value is within the valid range
            if not (min_val < node.val < max_val):
                return False
            
            # Recursively check the left and right subtrees with updated bounds
            return (isValid(node.left, min_val, node.val) and
                    isValid(node.right, node.val, max_val))
        
        # Start with the full range of possible values
        return isValid(root, float('-inf'), float('inf'))