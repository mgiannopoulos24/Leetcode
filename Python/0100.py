class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are identical
        if not p and not q:
            return True
        
        # If one of the nodes is None, trees are not identical
        if not p or not q:
            return False
        
        # If the current nodes' values differ, trees are not identical
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
