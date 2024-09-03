from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Check if (target + total_sum) is even and within bounds
        if (target + total_sum) % 2 != 0 or target > total_sum:
            return 0
        
        # Calculate the subset sum we are looking for
        S1 = (target + total_sum) // 2
        
        # If S1 is negative or exceeds the total sum, it's invalid
        if S1 < 0 or S1 > total_sum:
            return 0
        
        # DP array to store the number of ways to achieve each sum
        dp = [0] * (S1 + 1)
        dp[0] = 1  # There's one way to achieve a sum of 0 (by picking no elements)
        
        for num in nums:
            # Update the dp array from right to left to avoid overwriting results
            for j in range(S1, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[S1]
