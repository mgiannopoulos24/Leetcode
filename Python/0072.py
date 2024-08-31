class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a 2D dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the dp array
        for i in range(m + 1):
            dp[i][0] = i  # Need i deletions to make word1[0:i] empty
        
        for j in range(n + 1):
            dp[0][j] = j  # Need j insertions to make empty string to word2[0:j]
        
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No extra cost if characters match
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,   # Cost of deletion
                        dp[i][j - 1] + 1,   # Cost of insertion
                        dp[i - 1][j - 1] + 1  # Cost of replacement
                    )
        
        return dp[m][n]