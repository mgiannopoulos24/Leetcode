# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return (True, 0)
            
            # Check left subtree
            left_balanced, left_height = checkBalance(node.left)
            # Check right subtree
            right_balanced, right_height = checkBalance(node.right)
            
            # The current node is balanced if:
            # 1. Both subtrees are balanced
            # 2. The difference in height is no more than 1
            current_balanced = (
                left_balanced and 
                right_balanced and
                abs(left_height - right_height) <= 1
            )
            
            # The height of the current node is max(left_height, right_height) + 1
            current_height = max(left_height, right_height) + 1
            
            return (current_balanced, current_height)
        
        # Start the check from the root
        balanced, _ = checkBalance(root)
        return balanced