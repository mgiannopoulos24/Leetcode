# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # First, find the node to delete
        if key < root.val:
            # Key is in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Key is in the right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found
            if root.left is None:
                # Node with only right child or no child
                return root.right
            elif root.right is None:
                # Node with only left child
                return root.left
            else:
                # Node with two children
                # Find the smallest node in the right subtree (in-order successor)
                min_larger_node = self.findMin(root.right)
                # Copy the value of the in-order successor to this node
                root.val = min_larger_node.val
                # Delete the in-order successor
                root.right = self.deleteNode(root.right, min_larger_node.val)
        
        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        """Find the node with the minimum value in the given subtree."""
        while node.left is not None:
            node = node.left
        return node