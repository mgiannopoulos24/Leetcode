class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        # DP array where dp[i][j] represents the number of ways to get a sum of j with i dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Base case: one way to achieve a sum of 0 with 0 dice
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):  # i is the number of dice
            for j in range(1, target + 1):  # j is the sum we are trying to achieve
                # We consider all faces of the dice from 1 to k
                for f in range(1, k + 1):
                    if j >= f:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - f]) % MOD
        
        # The result is the number of ways to achieve the sum "target" with "n" dice
        return dp[n][target]
