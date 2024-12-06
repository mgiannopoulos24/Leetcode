from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        
        # Initialize height matrix with -1 for land cells and 0 for water cells
        height = [[-1 if isWater[i][j] == 0 else 0 for j in range(n)] for i in range(m)]
        
        # Initialize BFS queue with all water cells
        queue = deque([(i, j) for i in range(m) for j in range(n) if isWater[i][j] == 1])
        
        # BFS directions (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS to assign heights to each cell
        while queue:
            x, y = queue.popleft()
            
            # Check all 4 neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and unvisited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        
        return height
