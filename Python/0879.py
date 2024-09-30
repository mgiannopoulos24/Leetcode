from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(group)
        
        # Initialize DP table
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1  # Base case: One way to have 0 profit with 0 members and 0 crimes considered
        
        for i in range(1, m + 1):
            g = group[i - 1]
            p = profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    # Ways to achieve the same state without considering the i-th crime
                    dp[i][j][k] = dp[i - 1][j][k]
                    
                    # Ways to achieve the state by including the i-th crime
                    if j >= g:
                        dp[i][j][k] += dp[i - 1][j - g][max(0, k - p)]
                        dp[i][j][k] %= MOD
        
        # Calculate the result by summing up the schemes that achieve at least minProfit
        result = 0
        for j in range(n + 1):
            result += dp[m][j][minProfit]
            result %= MOD
        
        return result
