# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Inorder traversal to get the sorted list of values
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Step 2: Convert the sorted list into a balanced BST
        def sorted_list_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_list_to_bst(nums[:mid])
            root.right = sorted_list_to_bst(nums[mid+1:])
            return root
        
        # Perform inorder traversal to get sorted node values
        sorted_values = inorder_traversal(root)
        
        # Convert the sorted values into a balanced BST
        return sorted_list_to_bst(sorted_values)