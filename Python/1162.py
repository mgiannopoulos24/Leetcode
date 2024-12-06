from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # Step 1: Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        # If there is no land or no water, return -1
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_distance = -1
        
        # Step 2: Perform multi-source BFS
        while queue:
            x, y = queue.popleft()
            
            # Explore all 4 neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If the neighbor is within bounds and is water
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    # Update the water cell to the distance (current + 1)
                    grid[nx][ny] = grid[x][y] + 1
                    # Update max distance
                    max_distance = max(max_distance, grid[nx][ny] - 1)
                    # Add the water cell to the queue
                    queue.append((nx, ny))
        
        return max_distance
