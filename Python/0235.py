class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start from the root node
        current = root
        
        while current:
            # If both nodes are greater than current node, LCA must be in the right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both nodes are smaller than current node, LCA must be in the left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # We have found the split point, or one of p or q is the current node
                return current
