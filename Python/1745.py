class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        # Step 1: Precompute palindromic substrings
        dp = [[False] * n for _ in range(n)]
        
        # Fill the DP table for palindromic checks
        for length in range(1, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

        # Step 2: Try partitioning into three palindromic parts
        for i in range(n - 2):
            if dp[0][i]:  # Check if the first part is a palindrome
                for j in range(i + 1, n - 1):
                    if dp[i + 1][j] and dp[j + 1][n - 1]:  # Check the second and third parts
                        return True
        
        return False
