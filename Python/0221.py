from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # On the first row or first column
                        dp[i][j] = 1
                    else:
                        # Minimum of the three neighboring squares + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # Update the maximum side length
                    max_side = max(max_side, dp[i][j])
        
        # Return the area of the largest square
        return max_side * max_side
