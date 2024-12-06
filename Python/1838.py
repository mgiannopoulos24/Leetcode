from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_freq = 0
        
        for right in range(len(nums)):
            # Add the current right element to the total
            total += nums[right]
            
            # Calculate the cost to make all elements in the window equal to nums[right]
            while nums[right] * (right - left + 1) - total > k:
                # If the cost is too high, shrink the window from the left
                total -= nums[left]
                left += 1
            
            # Update the maximum frequency
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
