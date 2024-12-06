from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Initialize dp with the first row of the grid
        dp = grid[0][:]
        
        for i in range(1, n):
            # Find the smallest and second smallest values in the previous row
            min1 = float('inf')
            min2 = float('inf')
            min1_idx = -1
            for j in range(n):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    min1_idx = j
                elif dp[j] < min2:
                    min2 = dp[j]
            
            # Update dp for the current row
            new_dp = [0] * n
            for j in range(n):
                if j != min1_idx:
                    new_dp[j] = grid[i][j] + min1
                else:
                    new_dp[j] = grid[i][j] + min2
            dp = new_dp  # Move to the next row
        
        # The answer is the minimum value in the last row of dp
        return min(dp)
