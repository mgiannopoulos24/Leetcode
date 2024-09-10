# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Helper function to perform recursive insertion
        def insert(node: Optional[TreeNode], val: int) -> TreeNode:
            if node is None:
                return TreeNode(val)  # Create a new node if the current position is empty
            
            if val < node.val:
                node.left = insert(node.left, val)  # Recur on the left subtree
            else:
                node.right = insert(node.right, val)  # Recur on the right subtree
            
            return node  # Return the (potentially modified) node

        return insert(root, val)  # Start the insertion process from the root