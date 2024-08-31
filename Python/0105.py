# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # The root is always the first element in preorder
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder
        root_index = inorder.index(root_val)
        
        # Elements to the left of root_index in inorder are in the left subtree
        # Elements to the right of root_index in inorder are in the right subtree
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        
        # Elements after the root in preorder are the nodes of the left and right subtrees
        # The number of nodes in the left subtree is len(left_inorder)
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root