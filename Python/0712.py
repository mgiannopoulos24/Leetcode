class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # Initialize the DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the first row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        # Fill the first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        
        # Fill the rest of the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No deletion needed for these characters
                else:
                    # Choose the minimum cost between deleting from s1 or s2
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))
        
        # The result is the minimum ASCII sum of deletions for s1 and s2
        return dp[m][n]
