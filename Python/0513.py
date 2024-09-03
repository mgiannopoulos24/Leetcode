# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        # Initialize the queue with the root node and its level
        queue = deque([(root, 0)])
        bottom_left_value = root.val
        current_level = 0
        
        while queue:
            node, level = queue.popleft()
            
            # If we encounter a new level, update the bottom_left_value
            if level > current_level:
                bottom_left_value = node.val
                current_level = level
            
            # Add child nodes to the queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return bottom_left_value