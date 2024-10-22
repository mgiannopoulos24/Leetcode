class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Check if the current cell is out of bounds or not land
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            # Mark the current cell as visited (change land 1 to sea 0)
            grid[r][c] = 0
            # Explore the four possible directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Mark all land cells connected to the boundary
        for i in range(m):
            for j in [0, n - 1]:  # First and last column
                if grid[i][j] == 1:
                    dfs(i, j)
        for j in range(n):
            for i in [0, m - 1]:  # First and last row
                if grid[i][j] == 1:
                    dfs(i, j)
        
        # Step 2: Count all remaining land cells that are not connected to the boundary
        enclave_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    enclave_count += 1
        
        return enclave_count
