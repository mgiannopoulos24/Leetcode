# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal
        def in_order(node):
            if node:
                in_order(node.left)
                nodes.append(node)
                in_order(node.right)
        
        nodes = []
        in_order(root)
        
        # Create a new tree based on the nodes list
        dummy = TreeNode(0)
        current = dummy
        
        for node in nodes:
            node.left = None
            current.right = node
            current = node
        
        return dummy.right