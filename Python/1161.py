from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left = None
#         self.right = right = None

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')  # Initialize to negative infinity to track max sum
        max_level = 1  # The level with the maximum sum
        current_level = 1  # Track the current level during traversal
        
        # Initialize the queue with the root node (for level-order traversal)
        queue = deque([root])
        
        while queue:
            level_sum = 0  # Initialize the sum for the current level
            level_size = len(queue)  # Number of nodes at the current level
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update the max_sum and the corresponding level if this level has a higher sum
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            # Move to the next level
            current_level += 1
        
        return max_level
