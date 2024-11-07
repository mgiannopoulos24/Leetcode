from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Build the graph as two adjacency lists, one for red edges and one for blue edges
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        # Initialize the result array with -1 (unreachable)
        result = [-1] * n
        
        # BFS queue with (current_node, color of last edge taken, distance)
        # Color: 0 for red, 1 for blue
        queue = deque([(0, 0, 0), (0, 1, 0)])  # Start from node 0, with both red (0) and blue (1)
        
        # To track visited nodes: (node, color) -> True/False
        visited = set()
        
        # Starting node 0 has distance 0
        result[0] = 0
        
        while queue:
            node, color, dist = queue.popleft()
            
            # Get the next edges based on the current color
            if color == 0:  # Last edge was red, so we take blue edges next
                next_graph = blue_graph
                next_color = 1
            else:  # Last edge was blue, so we take red edges next
                next_graph = red_graph
                next_color = 0
            
            # Traverse all neighbors with alternating color
            for neighbor in next_graph[node]:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, next_color, dist + 1))
                    # Update the result if this is the first time visiting the node, or if we found a shorter path
                    if result[neighbor] == -1:
                        result[neighbor] = dist + 1
        
        return result
