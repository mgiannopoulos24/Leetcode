# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # Helper function to calculate the height of the tree
        def getHeight(node):
            if not node:
                return -1
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            return max(left_height, right_height) + 1
        
        # Helper function to fill the matrix with tree values
        def fillMatrix(node, row, col, height):
            if not node:
                return
            matrix[row][col] = str(node.val)
            offset = 2 ** (height - row - 1)
            if node.left:
                fillMatrix(node.left, row + 1, col - offset, height)
            if node.right:
                fillMatrix(node.right, row + 1, col + offset, height)
        
        # Determine the height of the tree
        height = getHeight(root)
        m = height + 1
        n = 2 ** (height + 1) - 1
        
        # Initialize the matrix with empty strings
        matrix = [[""] * n for _ in range(m)]
        
        # Start filling the matrix
        fillMatrix(root, 0, (n - 1) // 2, height)
        
        return matrix