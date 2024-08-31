from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the array nums in-place to arrange colors (0s, 1s, 2s) in order.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid], then increment both
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move to the next element
                mid += 1
            else:  # nums[mid] == 2
                # Swap nums[mid] and nums[high], then decrement high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1