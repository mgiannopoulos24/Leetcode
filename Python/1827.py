from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0  # To count the number of operations
        
        # Iterate from the second element to the end
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # Calculate the increment needed
                increment = nums[i - 1] - nums[i] + 1
                # Update nums[i] to make it strictly greater than nums[i-1]
                nums[i] += increment
                # Add the increment to the count of operations
                count += increment
        
        return count
