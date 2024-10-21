# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Index to keep track of the current node in preorder traversal
        self.index = 0
        
        # Helper function to build BST in the given range
        def buildBST(bound: int) -> Optional[TreeNode]:
            # If index is out of range or current value exceeds bound, return None
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None
            
            # Create the current node
            root_val = preorder[self.index]
            root = TreeNode(root_val)
            self.index += 1
            
            # Recursively construct the left and right subtrees
            # Left subtree: all values must be less than root_val
            root.left = buildBST(root_val)
            # Right subtree: all values must be less than bound but greater than root_val
            root.right = buildBST(bound)
            
            return root
        
        # Call the helper function with an initial bound of infinity
        return buildBST(float('inf'))