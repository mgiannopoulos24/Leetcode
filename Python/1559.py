class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Visited array to track whether a cell has been visited
        visited = [[False] * n for _ in range(m)]
        
        # DFS helper function
        def dfs(x, y, px, py):
            # Mark the current cell as visited
            visited[x][y] = True
            
            # Possible directions to move: right, left, down, up
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            # Traverse all four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is valid
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                    if not visited[nx][ny]:
                        # If the cell is not visited, continue DFS
                        if dfs(nx, ny, x, y):
                            return True
                    elif (nx, ny) != (px, py):
                        # If we visit a previously visited cell that isn't the parent, we found a cycle
                        return True
            
            return False
        
        # Iterate over all cells in the grid
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    # Start a DFS from every unvisited cell
                    if dfs(i, j, -1, -1):  # Starting point has no parent, so use (-1, -1)
                        return True
        
        return False
