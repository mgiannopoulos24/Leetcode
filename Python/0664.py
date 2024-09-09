class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # Initialize DP table
        dp = [[float('inf')] * n for _ in range(n)]

        # Base case: single character substrings
        for i in range(n):
            dp[i][i] = 1

        # Fill DP table
        for length in range(2, n+1):  # Length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        
        return dp[0][n-1]
