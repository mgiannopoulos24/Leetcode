class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][c] represents the number of ways to build an array of length i,
        # with maximum element j, and search cost c
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Base case: for arrays of length 1, the maximum value is j and search cost is 1
        for j in range(1, m + 1):
            dp[1][j][1] = 1
        
        # Fill the dp table
        for i in range(2, n + 1):  # Length of the array
            for j in range(1, m + 1):  # Maximum value in the array
                for c in range(1, k + 1):  # Current search cost
                    # Case 1: Add a number <= j, so the search cost does not increase
                    dp[i][j][c] = (dp[i][j][c] + dp[i - 1][j][c] * j) % MOD
                    
                    # Case 2: Add a number > j, so the search cost increases by 1
                    if c > 1:
                        for p in range(1, j):  # Iterate over all possible smaller numbers
                            dp[i][j][c] = (dp[i][j][c] + dp[i - 1][p][c - 1]) % MOD
        
        # Final result is the sum of all arrays of length n with search cost k
        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD
        
        return result