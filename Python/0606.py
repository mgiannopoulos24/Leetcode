# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        # Convert the value of the root to a string
        result = str(root.val)

        # Process the left child
        if root.left or root.right:  # we need to include the left child part even if it's null, when right is not null
            result += f"({self.tree2str(root.left)})"
        
        # Process the right child
        if root.right:
            result += f"({self.tree2str(root.right)})"

        return result