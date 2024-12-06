from typing import List

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # Concatenate word1 and word2 to form the combined string s
        s = word1 + word2
        n = len(s)
        len_word1 = len(word1)
        
        # DP array to store the longest palindromic subsequence lengths
        dp = [[0] * n for _ in range(n)]
        
        # Initialize the base case for single characters
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table for substrings of increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # Now look for the maximum length of a palindrome that uses at least
        # one character from both word1 and word2.
        max_len = 0
        for i in range(len_word1):
            for j in range(len_word1, n):
                if s[i] == s[j]:  # Potential palindromic subsequence boundary
                    max_len = max(max_len, dp[i][j])
        
        return max_len
