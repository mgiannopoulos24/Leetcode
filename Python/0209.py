from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')  # Initialize min_length with infinity
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += nums[right]  # Expand the window by including nums[right]
            
            while current_sum >= target:  # Check if the current window meets the requirement
                min_length = min(min_length, right - left + 1)  # Update min_length
                current_sum -= nums[left]  # Shrink the window from the left
                left += 1
        
        return min_length if min_length != float('inf') else 0
