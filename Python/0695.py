class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        def dfs(r: int, c: int) -> int:
            # Base case: check bounds and whether the cell is land (1)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0
            
            # Start DFS from this cell and count the area
            area = 1  # Current cell
            # Explore all 4 possible directions (right, down, left, up)
            area += dfs(r + 1, c)  # down
            area += dfs(r - 1, c)  # up
            area += dfs(r, c + 1)  # right
            area += dfs(r, c - 1)  # left
            
            return area
        
        max_area = 0
        # Traverse all cells in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # Perform DFS to find the area of the island
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
