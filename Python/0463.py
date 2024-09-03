from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Check each of the four directions
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        # Check if the neighboring cell is out of bounds or water
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                            perimeter += 1
        
        return perimeter
