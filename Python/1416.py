class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: there's one way to split an empty string
        
        # Iterate over the string, computing valid numbers
        for i in range(1, n + 1):
            num = 0
            # Try to form numbers ending at s[i-1], going backwards up to a valid limit
            for j in range(i, max(i - len(str(k)), 0), -1):  # Limit to avoid overly large numbers
                num = int(s[j-1:i])  # Extract the number from s[j-1:i]
                
                if num > k:  # If the number is greater than k, stop processing this segment
                    break
                
                if s[j-1] != '0':  # We cannot have numbers with leading zeros
                    dp[i] = (dp[i] + dp[j-1]) % MOD
        
        return dp[n]
