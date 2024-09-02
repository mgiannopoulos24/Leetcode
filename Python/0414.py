from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Use a set to get distinct values
        distinct_nums = set(nums)
        
        # Convert the set to a sorted list in descending order
        sorted_nums = sorted(distinct_nums, reverse=True)
        
        # Check if there are at least three distinct numbers
        if len(sorted_nums) >= 3:
            return sorted_nums[2]
        else:
            return sorted_nums[0]