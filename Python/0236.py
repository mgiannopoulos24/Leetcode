# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the root is null or matches p or q
        if root is None or root == p or root == q:
            return root
        
        # Recursively find LCA in left subtree
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        
        # Recursively find LCA in right subtree
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        
        # If both leftLCA and rightLCA are not None, p and q are found in both subtrees
        if leftLCA is not None and rightLCA is not None:
            return root
        
        # Otherwise, if one of the LCA is None, return the non-None value
        return leftLCA if leftLCA is not None else rightLCA
