# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            # Toggle the bit corresponding to the current node's value
            path ^= (1 << node.val)
            
            # If we're at a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                # Check if at most one bit is set in the path bitmask
                if path & (path - 1) == 0:
                    return 1
                else:
                    return 0
            
            # Recur for left and right children
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)
