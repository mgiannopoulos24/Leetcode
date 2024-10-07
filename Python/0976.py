from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in non-decreasing order
        nums.sort()
        
        # Iterate from the end of the list to the beginning
        for i in range(len(nums) - 1, 1, -1):
            # Check if the current triplet forms a valid triangle
            if nums[i-2] + nums[i-1] > nums[i]:
                # If valid, return the perimeter of the triangle
                return nums[i-2] + nums[i-1] + nums[i]
        
        # If no valid triangle found, return 0
        return 0
