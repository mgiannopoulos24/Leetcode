# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            if pre_start == pre_end:
                return root
            
            # The second element in preorder is the root of the left subtree
            left_root_val = preorder[pre_start + 1]
            
            # Find the boundary in postorder where the left subtree ends
            left_subtree_size = postorder.index(left_root_val) - post_start + 1
            
            # Determine the boundaries for the left and right subtrees in preorder and postorder
            left_pre_start = pre_start + 1
            left_pre_end = pre_start + 1 + left_subtree_size - 1
            left_post_start = post_start
            left_post_end = post_start + left_subtree_size - 1
            
            right_pre_start = left_pre_end + 1
            right_pre_end = pre_end
            right_post_start = left_post_end + 1
            right_post_end = post_end - 1
            
            root.left = build(left_pre_start, left_pre_end, left_post_start, left_post_end)
            root.right = build(right_pre_start, right_pre_end, right_post_start, right_post_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)