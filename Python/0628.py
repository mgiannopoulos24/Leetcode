from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the list
        nums.sort()
        
        # Maximum product of three largest numbers
        max1 = nums[-1] * nums[-2] * nums[-3]
        
        # Maximum product of two smallest and the largest number
        max2 = nums[0] * nums[1] * nums[-1]
        
        # Return the maximum of both products
        return max(max1, max2)
