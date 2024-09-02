from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total_sum is odd, it cannot be partitioned into two equal sum subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # Initialize DP array
        dp = [False] * (target + 1)
        dp[0] = True
        
        # Process each number in the array
        for num in nums:
            # Update DP array from right to left
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]