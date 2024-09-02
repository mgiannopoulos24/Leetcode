class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # Create a 2D DP table initialized with zeros
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Iterate over the length of the ranges
        for length in range(2, n + 1):  # length ranges from 2 to n
            for i in range(1, n - length + 2):  # range starts from 1 to n-length+1
                j = i + length - 1  # end of the range
                dp[i][j] = float('inf')
                
                # Try guessing each number in the current range
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))
        
        # The result for the range [1, n]
        return dp[1][n]
