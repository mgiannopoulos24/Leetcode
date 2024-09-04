# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)
        
        def dfs(node: TreeNode) -> bool:
            if not node:
                return False
            return isSameTree(node, subRoot) or dfs(node.left) or dfs(node.right)
        
        return dfs(root)