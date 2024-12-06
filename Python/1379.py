# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # If original is None, we cannot proceed
        if original is None:
            return None
        
        # If we find the target in the original tree, return the corresponding cloned node
        if original == target:
            return cloned
        
        # Search in the left subtree
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result is not None:
            return left_result
        
        # Search in the right subtree
        return self.getTargetCopy(original.right, cloned.right, target)
