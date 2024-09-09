# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to construct the tree recursively
        def buildTree(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            
            # Find the index of the maximum value in the current segment
            max_index = start
            for i in range(start, end + 1):
                if nums[i] > nums[max_index]:
                    max_index = i
            
            # Create the root node with the maximum value
            root = TreeNode(nums[max_index])
            
            # Recursively construct the left and right subtrees
            root.left = buildTree(start, max_index - 1)
            root.right = buildTree(max_index + 1, end)
            
            return root
        
        # Start the recursive tree construction
        return buildTree(0, len(nums) - 1)