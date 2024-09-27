from typing import List, Deque
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means uncolored, 0 and 1 will be our two colors
        
        def bfs(start: int) -> bool:
            queue: Deque[int] = deque([start])
            color[start] = 0  # Start coloring with color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If the neighbor hasn't been colored
                        # Color with alternate color
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:  # If neighbor has the same color
                        return False  # Not bipartite
            return True
        
        for i in range(n):
            if color[i] == -1:  # If this node is not yet colored
                if not bfs(i):
                    return False
        
        return True
