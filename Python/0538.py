# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_inorder(node: Optional[TreeNode]) -> None:
            nonlocal total
            if not node:
                return
            
            # Traverse right subtree first
            reverse_inorder(node.right)
            
            # Update the current node's value
            total += node.val
            node.val = total
            
            # Traverse left subtree
            reverse_inorder(node.left)
        
        total = 0
        reverse_inorder(root)
        return root