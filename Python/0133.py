from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        
        # Dictionary to store the mapping from original node to its clone
        clones = {}
        
        # Initialize BFS queue
        queue = deque([node])
        
        # Clone the root node and add to dictionary
        clones[node] = Node(node.val)
        
        while queue:
            current = queue.popleft()
            
            # Iterate through each neighbor of the current node
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    # Clone the neighbor and add it to the dictionary
                    clones[neighbor] = Node(neighbor.val)
                    # Add the neighbor to the BFS queue
                    queue.append(neighbor)
                
                # Add the neighbor to the current node's clone's neighbors list
                clones[current].neighbors.append(clones[neighbor])
        
        # Return the clone of the input node
        return clones[node]
