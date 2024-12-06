class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # Sort houses for easier distance calculation
        houses.sort()
        n = len(houses)

        # Precompute the cost of placing one mailbox for each subarray
        def calculate_cost():
            cost = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i, n):
                    median = houses[(i + j) // 2]
                    cost[i][j] = sum(abs(houses[t] - median) for t in range(i, j + 1))
            return cost
        
        # Calculate the cost of placing one mailbox in each subarray
        cost = calculate_cost()

        # DP array, dp[i][j] is the min total distance for the first i houses with j mailboxes
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # 0 houses, 0 mailboxes, cost is 0

        # Fill the DP table
        for j in range(1, k + 1):
            for i in range(1, n + 1):
                for x in range(i):
                    dp[i][j] = min(dp[i][j], dp[x][j - 1] + cost[x][i - 1])

        return dp[n][k]
