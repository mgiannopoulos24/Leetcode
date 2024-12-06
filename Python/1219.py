class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Directions for moving in the grid: (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Depth-First Search function
        def dfs(x, y):
            # Collect gold in the current cell
            current_gold = grid[x][y]
            max_gold = 0
            
            # Mark this cell as visited by setting its value to 0
            grid[x][y] = 0
            
            # Explore all four directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If the new position is valid and has gold, continue DFS
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0:
                    max_gold = max(max_gold, dfs(nx, ny))
            
            # After exploring, reset the current cell to its original value (backtracking)
            grid[x][y] = current_gold
            
            # Return the total gold collected from this path
            return current_gold + max_gold
        
        # Track the maximum gold collected
        max_gold_collected = 0
        
        # Try starting DFS from every cell that contains gold
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    # Perform DFS from this cell and update max gold
                    max_gold_collected = max(max_gold_collected, dfs(i, j))
        
        return max_gold_collected
