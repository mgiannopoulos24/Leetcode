class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Find the start and the total number of walkable squares
        rows, cols = len(grid), len(grid[0])
        start_x = start_y = end_x = end_y = empty_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_x, start_y = r, c
                elif grid[r][c] == 2:
                    end_x, end_y = r, c
                if grid[r][c] != -1:
                    empty_count += 1
        
        # Initialize the count of valid paths
        self.path_count = 0
        
        # Helper function to perform DFS
        def dfs(x, y, remain):
            # If out of bounds or obstacle, stop
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return
            
            # If it's the end square and we've visited all empty squares
            if grid[x][y] == 2:
                if remain == 1:
                    self.path_count += 1
                return
            
            # Mark the square as visited
            grid[x][y] = -1
            
            # Explore 4 possible directions
            dfs(x + 1, y, remain - 1)
            dfs(x - 1, y, remain - 1)
            dfs(x, y + 1, remain - 1)
            dfs(x, y - 1, remain - 1)
            
            # Unmark the square as visited (backtrack)
            grid[x][y] = 0
            
        # Start DFS from the starting square
        dfs(start_x, start_y, empty_count)
        
        return self.path_count
