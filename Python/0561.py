from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Initialize sum
        total_sum = 0
        
        # Iterate over the sorted array in steps of 2
        for i in range(0, len(nums), 2):
            # Add the first element of each pair to the sum
            total_sum += nums[i]
        
        return total_sum
