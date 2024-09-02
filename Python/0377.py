from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize the DP table
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: There's one way to make sum 0 (using no elements)
        
        # Fill the DP table
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]
