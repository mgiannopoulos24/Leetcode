from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Find the starting element (it will have only one adjacent element)
        start = next(node for node in adj if len(adj[node]) == 1)
        
        # Step 3: Reconstruct the array
        result = []
        visited = set()
        current = start
        
        while current not in visited:
            result.append(current)
            visited.add(current)
            # Move to the next node that hasn't been visited
            for neighbor in adj[current]:
                if neighbor not in visited:
                    current = neighbor
                    break
                    
        return result
