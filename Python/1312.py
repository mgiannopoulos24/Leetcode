class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the dp table
        for length in range(2, n + 1):  # length is the length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The number of insertions needed is the length of the string minus the length of the longest palindromic subsequence
        return n - dp[0][n - 1]
