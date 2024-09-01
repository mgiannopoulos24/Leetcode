from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # Calculate the maximum amount for both cases
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

