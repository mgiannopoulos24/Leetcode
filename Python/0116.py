from typing import Optional

# Definition for a Node.
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
        
        # Start with the root node
        leftmost = root
        
        while leftmost.left:  # Traverse level by level
            current = leftmost
            while current:
                # Connect the left child to the right child
                current.left.next = current.right
                
                # Connect the right child to the next node's left child if it exists
                if current.next:
                    current.right.next = current.next.left
                
                # Move to the next node in the current level
                current = current.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root