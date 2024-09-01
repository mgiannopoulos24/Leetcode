from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(r: int, c: int):
            # Check boundaries and if the current cell is water or already visited
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited
            grid[r][c] = '0'
            
            # Explore the neighbors (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        num_islands = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
