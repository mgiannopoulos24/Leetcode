# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.left_size = 0
        self.right_size = 0
        
        # Function to count the size of the subtree rooted at the given node
        def count_subtree_size(node):
            if not node:
                return 0
            left_count = count_subtree_size(node.left)
            right_count = count_subtree_size(node.right)
            
            # If the current node is x, record the size of its left and right subtrees
            if node.val == x:
                self.left_size = left_count
                self.right_size = right_count
            
            # Return the total size of the subtree rooted at this node
            return left_count + right_count + 1
        
        # Get the total size of the tree (also calculates the sizes of left and right subtrees of x)
        total_size = count_subtree_size(root)
        
        # The size of the rest of the tree excluding x and its subtrees
        rest_size = n - (self.left_size + self.right_size + 1)
        
        # Check if any of the three regions has more than half of the nodes
        max_blue_can_control = max(self.left_size, self.right_size, rest_size)
        
        return max_blue_can_control > n // 2
