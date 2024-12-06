# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # Initialize a set to store all recovered node values
        self.values = set()
        
        # Helper function to recover the tree
        def recover(node, value):
            if node:
                node.val = value  # Set the node's value based on the contamination rules
                self.values.add(value)  # Store the value in the set
                recover(node.left, 2 * value + 1)  # Recover the left child
                recover(node.right, 2 * value + 2)  # Recover the right child
        
        # Recover the tree starting from the root with value 0
        recover(root, 0)

    def find(self, target: int) -> bool:
        # Check if the target exists in the set of recovered values
        return target in self.values
