from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = nums[0]  # Start with the first element's value
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Ascending condition
                current_sum += nums[i]
            else:
                # Update max_sum if current_sum is greater
                max_sum = max(max_sum, current_sum)
                # Start a new ascending subarray
                current_sum = nums[i]
        
        # Final check for the last ascending subarray
        max_sum = max(max_sum, current_sum)
        
        return max_sum
