# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If both trees are empty, return None
        if not root1 and not root2:
            return None
        
        # If one of the trees is empty, return the non-empty tree
        if not root1:
            return root2
        if not root2:
            return root1
        
        # If both trees are non-empty, sum the values of the nodes
        merged_root = TreeNode(root1.val + root2.val)
        
        # Recursively merge the left and right subtrees
        merged_root.left = self.mergeTrees(root1.left, root2.left)
        merged_root.right = self.mergeTrees(root1.right, root2.right)
        
        return merged_root