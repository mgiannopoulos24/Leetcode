from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundary balloons with value 1
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create a 2D DP table
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        for length in range(1, n - 1):  # length of the subarray from 1 to n-2
            for left in range(0, n - length - 1):
                right = left + length + 1
                # Find the maximum coins that can be collected between left and right
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right]
                    )
        
        return dp[0][n - 1]

