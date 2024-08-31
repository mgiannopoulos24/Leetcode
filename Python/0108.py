# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to build the BST
        def convertListToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Find the middle index
            mid = (left + right) // 2
            
            # Create the root node
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = convertListToBST(left, mid - 1)
            root.right = convertListToBST(mid + 1, right)
            
            return root
        
        # Start the recursive process with the full range of the array
        return convertListToBST(0, len(nums) - 1)