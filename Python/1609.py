from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # BFS queue storing tuples of (node, level)
        queue = deque([(root, 0)])
        
        while queue:
            level_size = len(queue)
            prev_value = None
            
            for i in range(level_size):
                node, level = queue.popleft()
                val = node.val
                
                # Check for even-indexed levels
                if level % 2 == 0:
                    # Values must be odd and strictly increasing
                    if val % 2 == 0 or (prev_value is not None and val <= prev_value):
                        return False
                # Check for odd-indexed levels
                else:
                    # Values must be even and strictly decreasing
                    if val % 2 != 0 or (prev_value is not None and val >= prev_value):
                        return False
                
                # Update previous value
                prev_value = val
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        
        return True
