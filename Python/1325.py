# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Recursive post-order traversal
        if not root:
            return None
        
        # Recursively process the left and right children
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # If the current node is a leaf and its value is the target, delete it
        if not root.left and not root.right and root.val == target:
            return None
        
        return root