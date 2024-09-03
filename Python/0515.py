# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Initialize the queue for BFS
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            max_value = float('-inf')  # Initialize max value for this level
            
            for _ in range(level_size):
                node = queue.popleft()
                # Update max_value for the current level
                max_value = max(max_value, node.val)
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the max value of the current level to the result
            result.append(max_value)
        
        return result