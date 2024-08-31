# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def flattenTree(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Base case: If the node is None, return None
            if not node:
                return None
            
            # Flatten the left and right subtrees
            left_flattened = flattenTree(node.left)
            right_flattened = flattenTree(node.right)
            
            # If there's a left subtree, attach it to the right
            if left_flattened:
                # Find the rightmost node of the flattened left subtree
                last = left_flattened
                while last.right:
                    last = last.right
                
                # Connect the right subtree to the end of the left subtree
                last.right = node.right
                
                # Move the flattened left subtree to the right of the current node
                node.right = left_flattened
                node.left = None
            
            # Return the root of the flattened tree (current node)
            return node
        
        flattenTree(root)