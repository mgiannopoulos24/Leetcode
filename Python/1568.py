class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Function to count the number of islands using DFS
        def count_islands(grid):
            visited = [[False] * n for _ in range(m)]
            
            def dfs(i, j):
                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                    return
                visited[i][j] = True
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
            
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)
            return islands
        
        # Step 1: Check if the grid is already disconnected
        if count_islands(grid) != 1:
            return 0
        
        # Step 2: Check if removing one land can disconnect the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Temporarily turn this land into water
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        return 1
                    # Restore the land
                    grid[i][j] = 1
        
        # Step 3: If one change is not enough, return 2
        return 2
