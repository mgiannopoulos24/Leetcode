class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Initialize DP arrays for max and min products
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        # Initialize the starting point
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # Fill in the first row (can only come from the left)
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
        
        # Fill in the first column (can only come from above)
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        
        # Fill the rest of the dp arrays
        for i in range(1, m):
            for j in range(1, n):
                current_val = grid[i][j]
                
                # Possible previous values from left and top
                candidates = [
                    max_dp[i-1][j] * current_val,  # From top
                    min_dp[i-1][j] * current_val,  # From top
                    max_dp[i][j-1] * current_val,  # From left
                    min_dp[i][j-1] * current_val   # From left
                ]
                
                # The maximum and minimum products at the current position
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
        
        # The answer is the max_dp at the bottom-right corner
        result = max_dp[m-1][n-1]
        if result < 0:
            return -1
        else:
            return result % MOD
