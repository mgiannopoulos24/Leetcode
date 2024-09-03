from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize the dp array with 0s, with dp[0] = 1
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        # Process each coin
        for coin in coins:
            # Update dp table for all amounts from coin to amount
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[amount]
