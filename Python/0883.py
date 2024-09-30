from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # XY projection: sum of all non-zero cells
        xy_area = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        
        # YZ projection: max in each column
        yz_area = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        
        # ZX projection: max in each row
        zx_area = sum(max(grid[i]) for i in range(n))
        
        return xy_area + yz_area + zx_area
