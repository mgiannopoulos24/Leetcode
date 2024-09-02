from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables to track the first and second smallest elements
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # Found a new smallest number
            elif num <= second:
                second = num  # Found a number greater than 'first' but smaller than 'second'
            else:
                # If we find a number greater than both 'first' and 'second', we found the triplet
                return True
        
        # No increasing triplet was found
        return False