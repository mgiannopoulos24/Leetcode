class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Helper function to perform DFS and mark visited land cells
        def dfs(r, c):
            # If we go out of bounds or hit water, return False
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1:
                return True
            
            # Mark the current cell as visited by setting it to water
            grid[r][c] = 1
            
            # Explore in all four directions
            top = dfs(r - 1, c)
            bottom = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            # The island is closed if all recursive DFS calls return True
            return top and bottom and left and right

        # First, eliminate any land that touches the boundary
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs(r, c)

        # Now, count the number of closed islands
        closed_island_count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0 and dfs(r, c):
                    closed_island_count += 1

        return closed_island_count
