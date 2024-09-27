class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Initialize for single character substrings
        for i in range(n):
            dp[i][i] = 1
        
        # Iterate over substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    low, high = i + 1, j - 1
                    while low <= high and s[low] != s[i]:
                        low += 1
                    while low <= high and s[high] != s[i]:
                        high -= 1
                    
                    if low > high:
                        # Case where s[i] and s[j] are the same and there are no occurrences of s[i] in between
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif low == high:
                        # Case where s[i] and s[j] are the same and there's exactly one s[i] in between
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        # Case where s[i] and s[j] are the same and there are multiple s[i] in between
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
                    
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                
                dp[i][j] = (dp[i][j] + MOD) % MOD
        
        return dp[0][n - 1]
