# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate sum of left leaves
        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            if node is None:
                return 0
            # If it's a leaf node and it's a left child
            if node.left is None and node.right is None:
                if is_left:
                    return node.val
                else:
                    return 0
            # Recursively find left leaves in both subtrees
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)