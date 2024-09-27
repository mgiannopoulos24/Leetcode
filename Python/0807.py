from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Find the max heights for each row and each column
        max_row = [max(row) for row in grid]
        max_col = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        # Step 2: Calculate the maximum possible increase for each building
        total_increase = 0
        for r in range(n):
            for c in range(n):
                # Maximum height the building at (r, c) can be increased to
                allowed_height = min(max_row[r], max_col[c])
                # Calculate the increase
                total_increase += allowed_height - grid[r][c]
        
        return total_increase
