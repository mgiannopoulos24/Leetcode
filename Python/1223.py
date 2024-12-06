class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[pos][last][count] means at position 'pos', last die number 'last' appeared 'count' consecutive times.
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n)]
        
        # Initialize for the first roll
        for i in range(6):
            dp[0][i][1] = 1
        
        # Fill DP table for positions 1 to n-1
        for pos in range(1, n):
            for last in range(6):
                for count in range(1, rollMax[last] + 1):
                    if dp[pos-1][last][count] > 0:
                        # Continue with the same 'last' roll if allowed
                        if count < rollMax[last]:
                            dp[pos][last][count + 1] = (dp[pos][last][count + 1] + dp[pos-1][last][count]) % MOD
                        # Switch to a different roll
                        for new_roll in range(6):
                            if new_roll != last:
                                dp[pos][new_roll][1] = (dp[pos][new_roll][1] + dp[pos-1][last][count]) % MOD
        
        # Sum up all the valid sequences of length 'n'
        result = 0
        for last in range(6):
            for count in range(1, rollMax[last] + 1):
                result = (result + dp[n-1][last][count]) % MOD
        
        return result
