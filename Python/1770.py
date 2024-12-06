from typing import List
from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        
        # Memoized recursive DP function
        @lru_cache(None)
        def dp(left: int, i: int) -> int:
            # If we've used all multipliers, return 0
            if i == m:
                return 0
            
            # Option 1: Pick the leftmost available element
            pick_left = multipliers[i] * nums[left] + dp(left + 1, i + 1)
            
            # Option 2: Pick the rightmost available element
            right = n - 1 - (i - left)
            pick_right = multipliers[i] * nums[right] + dp(left, i + 1)
            
            # Return the maximum score possible
            return max(pick_left, pick_right)
        
        # Start the recursion from the beginning
        return dp(0, 0)
