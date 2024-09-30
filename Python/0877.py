from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j] will be the maximum difference Alice can achieve over Bob from piles[i] to piles[j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: when there's only one pile to pick
        for i in range(n):
            dp[i][i] = piles[i]
        
        # Fill the DP table for subarrays of length 2 to n
        for length in range(2, n + 1):  # length of subarray
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        # If dp[0][n-1] > 0, Alice can guarantee a win
        return dp[0][n-1] > 0
