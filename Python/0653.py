# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Helper function to perform in-order traversal
        def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Get all the values in sorted order
        values = inorder_traversal(root)
        
        # Use two pointers to find if there exist two numbers that sum up to k
        left, right = 0, len(values) - 1
        
        while left < right:
            current_sum = values[left] + values[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return False