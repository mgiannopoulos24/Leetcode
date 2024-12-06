from collections import deque, defaultdict

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()  # Keep track of all unique colors in the grid
        color_boundaries = {}  # Store the boundaries for each color
        
        # Step 1: Identify the boundaries for each color
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                colors.add(color)
                if color not in color_boundaries:
                    color_boundaries[color] = [i, i, j, j]  # [top, bottom, left, right]
                else:
                    top, bottom, left, right = color_boundaries[color]
                    color_boundaries[color] = [
                        min(top, i), max(bottom, i),
                        min(left, j), max(right, j)
                    ]
        
        # Step 2: Build the dependency graph
        in_degree = {color: 0 for color in colors}  # To track incoming edges
        graph = defaultdict(set)  # Adjacency list for graph
        
        for color, (top, bottom, left, right) in color_boundaries.items():
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    if targetGrid[i][j] != color:
                        # If another color is inside this color's rectangle, add an edge
                        other_color = targetGrid[i][j]
                        if other_color not in graph[color]:
                            graph[color].add(other_color)
                            in_degree[other_color] += 1
        
        # Step 3: Perform topological sort (Kahn's Algorithm)
        queue = deque([color for color in colors if in_degree[color] == 0])
        processed_colors = 0
        
        while queue:
            color = queue.popleft()
            processed_colors += 1
            for neighbor in graph[color]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we processed all colors, return True; otherwise, there's a cycle
        return processed_colors == len(colors)
