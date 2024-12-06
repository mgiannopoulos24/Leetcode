from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # If target is negative, it's impossible to reach x
        if target < 0:
            return -1
        
        # Sliding window to find the longest subarray with sum equal to target
        left = 0
        current_sum = 0
        max_length = -1
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # When current_sum exceeds the target, shrink from the left
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # Check if we found a subarray with the required sum
            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        # If max_length is still -1, it means we did not find such a subarray
        return len(nums) - max_length if max_length != -1 else -1
