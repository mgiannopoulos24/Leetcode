from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Use the sliding window technique to find the maximum sum of any 'k' length subarray
        for i in range(k, len(nums)):
            # Update the current window sum by subtracting the element that is sliding out
            # and adding the element that is sliding in
            current_sum += nums[i] - nums[i - k]
            # Update max_sum if the new window sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Calculate and return the maximum average
        return max_sum / k
