class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_cells = m * n
        
        # Step 1: Flatten the 2D grid into a 1D list
        flat_grid = []
        for row in grid:
            flat_grid.extend(row)
        
        # Step 2: Calculate effective number of shifts
        k = k % total_cells
        
        # Step 3: Shift the flattened grid
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
        # Step 4: Rebuild the 2D grid from the shifted 1D list
        new_grid = []
        for i in range(0, total_cells, n):
            new_grid.append(flat_grid[i:i + n])
        
        return new_grid
