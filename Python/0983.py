class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Initialize dp array with a size enough to cover all days up to 365
        dp = [0] * 366
        day_set = set(days)  # Convert list to set for O(1) lookup
        
        for i in range(1, 366):
            if i not in day_set:
                # No travel on day i, cost stays the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Travel on day i, calculate the minimum of the three options
                dp[i] = min(
                    dp[i - 1] + costs[0],  # Cost of a 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # Cost of a 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # Cost of a 30-day pass
                )
        
        return dp[365]
