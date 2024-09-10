# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # This variable will store the maximum length of the univalue path found
        self.max_length = 0
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the length of the univalue path in the left and right subtrees
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            # Initialize the length of the longest path passing through this node
            left_univalue_path = 0
            right_univalue_path = 0
            
            # If the current node's value matches the left child, extend the path
            if node.left and node.left.val == node.val:
                left_univalue_path = left_length + 1
            
            # If the current node's value matches the right child, extend the path
            if node.right and node.right.val == node.val:
                right_univalue_path = right_length + 1
            
            # Update the global maximum length with the length of the path passing through this node
            self.max_length = max(self.max_length, left_univalue_path + right_univalue_path)
            
            # Return the length of the longest univalue path that can be extended to parent node
            return max(left_univalue_path, right_univalue_path)
        
        # Start DFS from the root
        dfs(root)
        
        return self.max_length