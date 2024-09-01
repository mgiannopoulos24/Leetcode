from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case: if amount is 0, no coins are needed
        if amount == 0:
            return 0
        
        # Initialize the DP array with a value greater than any possible result
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: no coins are needed to make amount 0
        
        # Update the DP array
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        # Check if the amount can be made up
        return dp[amount] if dp[amount] != float('inf') else -1
