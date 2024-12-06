from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum = 0, 0  # Track the maximum and minimum subarray sums
        current_max, current_min = 0, 0  # Running sums for max and min subarrays
        
        for num in nums:
            # Calculate the running maximum and minimum subarray sums
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)
            
            # Update max_sum and min_sum
            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)
        
        # The result is the maximum absolute value between max_sum and min_sum
        return max(abs(max_sum), abs(min_sum))
