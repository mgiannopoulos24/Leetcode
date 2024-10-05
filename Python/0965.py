# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, return True (by definition of uni-valued)
        if not root:
            return True
        
        # Helper function to perform DFS and check if all nodes have the same value
        def dfs(node: TreeNode, value: int) -> bool:
            if not node:
                return True
            # Check if the current node's value is different from the expected value
            if node.val != value:
                return False
            # Recursively check left and right subtrees
            return dfs(node.left, value) and dfs(node.right, value)
        
        # Start DFS with the root's value
        return dfs(root, root.val)