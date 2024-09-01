from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Edge case: if there are no prices or transactions, profit is 0
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        
        # If k is greater than or equal to n // 2, we can make as many transactions as needed
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        
        # Initialize DP table
        dp = [[0] * n for _ in range(k + 1)]
        
        # Iterate over number of transactions
        for t in range(1, k + 1):
            max_diff = -prices[0]  # The maximum value of dp[t-1][j] - prices[j]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])
        
        # The result is the maximum profit with at most k transactions on the last day
        return dp[k][n - 1]
