# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 1  # Null nodes are covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:
                self.cameras += 1
                return 2  # This node has a camera
            
            if left == 2 or right == 2:
                return 1  # This node is covered by a camera
            
            return 0  # This node is not covered
        
        self.cameras = 0
        if dfs(root) == 0:
            self.cameras += 1  # If the root is not covered, add a camera
        
        return self.cameras