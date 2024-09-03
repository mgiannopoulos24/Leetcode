class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Initialize a 2D DP table
        dp = [[0] * n for _ in range(n)]
        
        # Each single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table
        # len is the length of the current substring being considered
        for length in range(2, n + 1):  # length ranges from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The result is the length of the longest palindromic subsequence in s
        return dp[0][n - 1]
