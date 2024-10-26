from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        
        # Iterate over each element of the array
        for i in range(n):
            max_val = 0
            # Try partitioning from length 1 to length k (or until we reach the start)
            for j in range(1, min(k, i + 1) + 1):
                # Update max_val for the current partition
                max_val = max(max_val, arr[i - j + 1])
                # Calculate the maximum sum using this partition
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + max_val * j)
                else:
                    dp[i] = max(dp[i], max_val * j)
        
        return dp[-1]  # The result is the maximum sum for the whole array
