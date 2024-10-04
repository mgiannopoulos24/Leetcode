class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] will be the number of distinct subsequences of s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one subsequence (empty string) for the base case
        
        # Dictionary to keep track of the last occurrence of each character
        last_occurrence = {}
        
        for i in range(1, n + 1):
            char = s[i - 1]
            
            # Total distinct subsequences ending at index i-1
            dp[i] = (2 * dp[i - 1]) % MOD
            
            # If the character was seen before, subtract the number of subsequences
            # ending just before its last occurrence
            if char in last_occurrence:
                dp[i] = (dp[i] - dp[last_occurrence[char] - 1] + MOD) % MOD
            
            # Update the last occurrence of the character
            last_occurrence[char] = i
        
        # Subtract 1 to exclude the empty subsequence
        return (dp[n] - 1 + MOD) % MOD
