from typing import List
import math
from functools import reduce

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        """
        Determines if the array is good by checking if the GCD of all elements is 1.

        Args:
        nums (List[int]): List of positive integers.

        Returns:
        bool: True if the array is good, False otherwise.
        """
        # Edge Case: Single element
        if len(nums) == 1:
            return nums[0] == 1

        # Compute the GCD of the entire array
        overall_gcd = reduce(math.gcd, nums)
        
        # If the GCD is 1, it's possible to obtain a sum of 1
        return overall_gcd == 1
