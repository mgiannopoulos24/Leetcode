from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()
        
        # Flip the smallest negative values
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        
        # If k is still odd, flip the smallest element again (smallest absolute value)
        if k % 2 == 1:
            nums.sort()  # Sort again to find the smallest element after flipping
            nums[0] = -nums[0]
        
        # Return the sum of the modified array
        return sum(nums)
