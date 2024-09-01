from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # Initializing dp arrays
        dp = [[0] * 3 for _ in range(n)]
        
        # Base cases
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])  # Cooldown
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # Buy
            dp[i][2] = dp[i-1][1] + prices[i]  # Sell
        
        # Maximum profit would be max(dp[n-1][0], dp[n-1][2])
        return max(dp[n-1][0], dp[n-1][2])
