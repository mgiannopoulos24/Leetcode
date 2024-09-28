from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        # Compute prefix sums
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Initialize dp table
        dp = [[0] * n for _ in range(k + 1)]
        
        # Fill dp for 1 partition
        for j in range(n):
            dp[1][j] = (prefix_sum[j + 1] - prefix_sum[0]) / (j + 1)
        
        # Fill dp for partitions from 2 to k
        for i in range(2, k + 1):
            for j in range(i - 1, n):
                for m in range(i - 2, j):
                    current_sum = prefix_sum[j + 1] - prefix_sum[m + 1]
                    current_avg = current_sum / (j - m)
                    dp[i][j] = max(dp[i][j], dp[i - 1][m] + current_avg)
        
        return dp[k][n - 1]

