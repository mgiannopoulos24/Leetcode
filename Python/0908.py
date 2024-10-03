from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Edge case for single element array
        if len(nums) == 1:
            return 0
        
        min_val = min(nums)
        max_val = max(nums)
        
        # Calculate the minimum possible score
        min_score = max_val - min_val - 2 * k
        
        # Return 0 if the score is negative, otherwise return the computed score
        return max(min_score, 0)