from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        # Step 1: Find the left boundary
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        
        # If no such boundary is found, the array is already sorted
        if left == n - 1:
            return 0
        
        # Step 2: Find the right boundary
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        
        # Step 3: Find the min and max within the subarray nums[left:right + 1]
        min_val = min(nums[left:right + 1])
        max_val = max(nums[left:right + 1])
        
        # Step 4: Adjust the left boundary
        while left > 0 and nums[left - 1] > min_val:
            left -= 1
        
        # Step 5: Adjust the right boundary
        while right < n - 1 and nums[right + 1] < max_val:
            right += 1
        
        # Step 6: Calculate the length of the subarray to be sorted
        return right - left + 1
