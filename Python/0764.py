from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Initialize grid with n (maximum order without any mines)
        grid = [[n] * n for _ in range(n)]
        
        # Place mines in the grid
        for x, y in mines:
            grid[x][y] = 0
        
        # DP arrays for the maximum arm lengths in all four directions
        for r in range(n):
            left = right = up = down = 0
            for c in range(n):
                # Compute from left to right
                if grid[r][c] != 0:
                    left += 1
                else:
                    left = 0
                grid[r][c] = min(grid[r][c], left)
                
                # Compute from top to bottom
                if grid[c][r] != 0:
                    up += 1
                else:
                    up = 0
                grid[c][r] = min(grid[c][r], up)
                
                # Compute from right to left
                if grid[r][n - c - 1] != 0:
                    right += 1
                else:
                    right = 0
                grid[r][n - c - 1] = min(grid[r][n - c - 1], right)
                
                # Compute from bottom to top
                if grid[n - c - 1][r] != 0:
                    down += 1
                else:
                    down = 0
                grid[n - c - 1][r] = min(grid[n - c - 1][r], down)
        
        # Find the maximum order plus sign that can be formed
        max_order = 0
        for r in range(n):
            for c in range(n):
                max_order = max(max_order, grid[r][c])
        
        return max_order
