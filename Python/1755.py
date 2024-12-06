from typing import List
from bisect import bisect_left

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # Helper function to get all subset sums of a given list
        def get_subset_sums(arr):
            subset_sums = {0}
            for num in arr:
                subset_sums.update({x + num for x in subset_sums})
            return list(subset_sums)
        
        # Step 1: Split nums into two halves
        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        
        # Step 2: Get all subset sums of both halves
        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)
        
        # Step 3: Sort left_sums for binary search purposes
        left_sums.sort()
        
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        
        # Step 4: For each sum in right_sums, find the closest sum in left_sums
        for right_sum in right_sums:
            target = goal - right_sum
            
            # Binary search in left_sums for the closest value to `target`
            pos = bisect_left(left_sums, target)
            
            # Check the closest sums at position pos and pos - 1
            if pos < len(left_sums):
                min_diff = min(min_diff, abs(target - left_sums[pos]))
            if pos > 0:
                min_diff = min(min_diff, abs(target - left_sums[pos - 1]))
        
        return min_diff
