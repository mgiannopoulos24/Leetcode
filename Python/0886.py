from typing import List
from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create adjacency list for the graph
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize color array; 0 means uncolored, 1 and -1 are two colors
        color = [0] * (n + 1)
        
        def bfs(start):
            queue = deque([start])
            color[start] = 1  # Start coloring with color 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = -current_color
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:  # Not colored
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:  # Conflict
                        return False
            return True
        
        # Check all nodes, as the graph may be disconnected
        for person in range(1, n + 1):
            if color[person] == 0:  # Not yet visited
                if not bfs(person):
                    return False
        
        return True
