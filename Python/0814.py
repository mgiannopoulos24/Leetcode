# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def containsOne(node):
            if not node:
                return False
            
            # Recursively prune left and right subtrees
            left_contains_one = containsOne(node.left)
            right_contains_one = containsOne(node.right)
            
            # If the left subtree doesn't contain 1, prune it
            if not left_contains_one:
                node.left = None
            
            # If the right subtree doesn't contain 1, prune it
            if not right_contains_one:
                node.right = None
            
            # Return True if the current node or any of its subtrees contain 1
            return node.val == 1 or left_contains_one or right_contains_one
        
        return root if containsOne(root) else None