from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current non-zero element with the element at lastNonZeroFoundAt
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                # Move the pointer for the last non-zero position
                lastNonZeroFoundAt += 1
