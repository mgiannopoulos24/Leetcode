from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # Create a DP table with the same dimensions as the dungeon
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Initialize the bottom-right corner
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill the last row (bottom-most row)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        
        # Fill the last column (right-most column)
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        # Fill the rest of the DP table
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                min_health_needed = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_needed - dungeon[i][j])
        
        return dp[0][0]
