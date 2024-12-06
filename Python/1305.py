# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(root):
            """Helper function to perform in-order traversal of a binary tree."""
            if not root:
                return []
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

        # Get the sorted lists from both trees
        list1 = inorder_traversal(root1)
        list2 = inorder_traversal(root2)

        # Merge the two sorted lists
        return sorted(list1 + list2)