class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize the DP table
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            # Calculate cumulative sum
            cum_sum = [0] * (k + 1)
            cum_sum[0] = dp[i-1][0]
            for j in range(1, k + 1):
                cum_sum[j] = (cum_sum[j-1] + dp[i-1][j]) % MOD
            
            for j in range(k + 1):
                dp[i][j] = cum_sum[j] % MOD
                if j >= i:
                    dp[i][j] = (dp[i][j] - cum_sum[j-i] + MOD) % MOD
        
        return dp[n][k]
