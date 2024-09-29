from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited_mask = (1 << n) - 1
        
        # Initialize the BFS queue
        queue = deque()
        visited = set()
        
        # Initialize the queue with all single-node starting points
        for i in range(n):
            start_mask = 1 << i
            queue.append((i, start_mask, 0))  # (current_node, visited_mask, distance)
            visited.add((i, start_mask))
        
        # Perform BFS
        while queue:
            node, visited_mask, dist = queue.popleft()
            
            # If all nodes are visited
            if visited_mask == all_visited_mask:
                return dist
            
            # Explore all adjacent nodes
            for neighbor in graph[node]:
                new_visited_mask = visited_mask | (1 << neighbor)
                
                if (neighbor, new_visited_mask) not in visited:
                    visited.add((neighbor, new_visited_mask))
                    queue.append((neighbor, new_visited_mask, dist + 1))
        
        return -1  # This return is just a fallback; the problem guarantees a connected graph.
