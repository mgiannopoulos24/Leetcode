from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Ensure that all rows start with 1
        for i in range(m):
            if grid[i][0] == 0:
                # Toggle the entire row if it starts with 0
                grid[i] = [1 - x for x in grid[i]]
        
        # Step 2: Optimize each column
        for j in range(n):
            # Count number of 1s in column j
            count_ones = sum(grid[i][j] for i in range(m))
            # If more than half of the values in the column are 0s, toggle the column
            if count_ones < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 3: Calculate the score
        score = 0
        for i in range(m):
            row_value = int(''.join(map(str, grid[i])), 2)
            score += row_value
        
        return score
