from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        # Initialize DP arrays
        dp1 = [0] * n  # Maximum profit with at most one transaction up to day i
        dp2 = [0] * n  # Maximum profit with at most two transactions up to day i
        
        # Compute dp1: maximum profit with one transaction
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price, prices[i])
            dp1[i] = max(dp1[i - 1] if i > 0 else 0, prices[i] - min_price)
        
        # Compute dp2: maximum profit with two transactions
        max_profit_first_transaction = -float('inf')
        for i in range(n):
            max_profit_first_transaction = max(max_profit_first_transaction, dp1[i] - prices[i])
            dp2[i] = max(dp2[i - 1] if i > 0 else 0, prices[i] + max_profit_first_transaction)
        
        return dp2[-1]

