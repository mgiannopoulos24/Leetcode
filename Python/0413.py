from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        current_length = 0
        
        # Iterate through the array
        for i in range(2, n):
            # Check if the current subarray is arithmetic
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current_length += 1
                count += current_length
            else:
                current_length = 0
        
        return count