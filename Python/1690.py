class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Precompute the prefix sum for fast range sum calculations
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        # DP table to store the difference between Alice and Bob's score for subarrays
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        for length in range(2, n + 1):  # Subarray lengths from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                # Total sum of stones between indices i and j
                total_sum = prefix_sum[j + 1] - prefix_sum[i]
                # Alice's choice to maximize the score difference
                dp[i][j] = max(
                    total_sum - stones[i] - dp[i + 1][j],  # Remove the left stone
                    total_sum - stones[j] - dp[i][j - 1]   # Remove the right stone
                )
        
        # Return the maximum difference starting from the entire array
        return dp[0][n-1]
