from typing import List
from math import gcd
from functools import lru_cache

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        # Memoization dictionary to store computed states
        memo = {}
        
        def dp(mask: int, operation: int) -> int:
            # Base case: if all pairs are made
            if mask == (1 << len(nums)) - 1:
                return 0
            
            # If this state has already been computed
            if (mask, operation) in memo:
                return memo[(mask, operation)]
            
            max_score = 0
            
            # Try all pairs of elements (i, j)
            for i in range(len(nums)):
                if mask & (1 << i):
                    continue  # i-th element is already used
                
                for j in range(i + 1, len(nums)):
                    if mask & (1 << j):
                        continue  # j-th element is already used
                    
                    # Calculate new mask after picking elements i and j
                    new_mask = mask | (1 << i) | (1 << j)
                    # Score of this operation
                    current_score = operation * gcd(nums[i], nums[j])
                    # Recursively calculate the maximum score
                    max_score = max(max_score, current_score + dp(new_mask, operation + 1))
            
            # Store the result in memoization table
            memo[(mask, operation)] = max_score
            return max_score
        
        # Start recursion with an empty mask and operation 1
        return dp(0, 1)
