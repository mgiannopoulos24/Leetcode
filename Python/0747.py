from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find the maximum value and its index
        max_value = max(nums)
        max_index = nums.index(max_value)
        
        # Check if the maximum value is at least twice as large as every other value
        for i, num in enumerate(nums):
            if i != max_index and max_value < 2 * num:
                return -1
        
        return max_index
