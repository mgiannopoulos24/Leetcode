class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)  # number of rows
        n = len(grid[0])  # number of columns
        
        row_count = [0] * m  # to count servers in each row
        col_count = [0] * n  # to count servers in each column
        
        # Step 1: Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Step 2: Count servers that can communicate
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        count += 1
        
        return count
