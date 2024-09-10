# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Base case: if the tree is empty
        if not root:
            return None
        
        # If current node's value is less than low, we only need to consider the right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If current node's value is greater than high, we only need to consider the left subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Recursively trim the left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root