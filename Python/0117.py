from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        
        # Initialize the queue with the root node
        queue = deque([root])
        
        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            
            # Process each node at the current level
            for i in range(level_size):
                node = queue.popleft()
                
                # If this is not the last node of the current level, set the next pointer
                if i < level_size - 1:
                    node.next = queue[0]
                
                # Enqueue the left and right children of the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
