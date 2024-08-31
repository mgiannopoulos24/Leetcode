# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # The root is always the last element in postorder
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder
        root_index = inorder.index(root_val)
        
        # Elements to the left of root_index in inorder are in the left subtree
        # Elements to the right of root_index in inorder are in the right subtree
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        
        # Elements before the last element in postorder are the nodes of the left and right subtrees
        # The number of nodes in the right subtree is len(right_inorder)
        right_postorder = postorder[len(left_inorder):-1]
        left_postorder = postorder[:len(left_inorder)]
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        
        return root