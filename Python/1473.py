class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # Initialize constants
        INF = float('inf')

        # DP table dp[i][j][k] means the minimum cost for painting the first i+1 houses,
        # with j+1 being the color of the i-th house, and k+1 neighborhoods.
        dp = [[[INF] * (target + 1) for _ in range(n)] for _ in range(m)]
        
        # Initialize for the first house
        for j in range(n):
            if houses[0] == 0:  # if the first house is not painted, we can paint it
                dp[0][j][1] = cost[0][j]  # cost to paint house 0 with color j+1
            elif houses[0] == j + 1:  # if the first house is already painted with color j+1
                dp[0][j][1] = 0  # no cost if it's already painted with color j+1

        # Process for the rest of the houses
        for i in range(1, m):
            for j in range(n):
                if houses[i] and houses[i] != j + 1:
                    continue  # If the house is painted with another color, skip this color

                for k in range(1, target + 1):
                    # We need to calculate the min cost to paint the i-th house with color j+1,
                    # resulting in exactly k neighborhoods
                    if houses[i] == 0:  # if the house is not painted, we consider the cost
                        cur_cost = cost[i][j]
                    else:  # if the house is painted, no additional cost
                        cur_cost = 0
                    
                    # If the previous house is painted with the same color, no new neighborhood
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k] + cur_cost)
                    
                    # If the previous house is painted with a different color, a new neighborhood is formed
                    for prev_color in range(n):
                        if prev_color != j:
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][prev_color][k-1] + cur_cost)
        
        # Find the answer by looking at the last house, with exactly target neighborhoods
        result = min(dp[m-1][j][target] for j in range(n))
        
        return result if result != INF else -1
