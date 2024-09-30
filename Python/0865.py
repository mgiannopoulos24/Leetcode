# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)  # (depth, subtree containing deepest nodes)
            
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_depth + 1, left_subtree)
            elif right_depth > left_depth:
                return (right_depth + 1, right_subtree)
            else:
                return (left_depth + 1, node)
        
        _, result = dfs(root)
        return result