class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total_area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Add surface area for current tower
                    total_area += 6 * grid[i][j] - 2 * (grid[i][j] - 1)
                    
                # Subtract the adjacent areas for the next cells
                if i > 0:
                    total_area -= 2 * min(grid[i][j], grid[i-1][j])  # Adjacent in the row above
                if j > 0:
                    total_area -= 2 * min(grid[i][j], grid[i][j-1])  # Adjacent in the previous column

        return total_area
