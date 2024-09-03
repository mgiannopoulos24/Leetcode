from typing import List
import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        stack = []  # Stack to keep track of potential nums[j]
        min_i = -math.inf  # This represents the maximum value of nums[i] seen so far
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if nums[i] < min_i:
                return True  # Found a valid 132 pattern

            # Maintain the stack with decreasing order values for nums[j]
            while stack and stack[-1] < nums[i]:
                min_i = max(min_i, stack.pop())
                
            stack.append(nums[i])
        
        return False
