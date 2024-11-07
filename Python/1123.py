# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform postorder traversal and track depths
        def postorder(node):
            if not node:
                return (None, 0)  # No node, depth is 0
            
            # Recurse on left and right subtrees
            left_lca, left_depth = postorder(node.left)
            right_lca, right_depth = postorder(node.right)
            
            # If both left and right have the same depth, current node is the LCA
            if left_depth == right_depth:
                return (node, left_depth + 1)
            # Otherwise, return the subtree with the deeper depth
            elif left_depth > right_depth:
                return (left_lca, left_depth + 1)
            else:
                return (right_lca, right_depth + 1)
        
        # Start postorder traversal from the root
        lca, _ = postorder(root)
        return lca