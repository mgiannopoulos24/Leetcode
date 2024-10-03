from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] % 2 == 0:
                # If nums[left] is even, move left pointer to the right
                left += 1
            elif nums[right] % 2 == 1:
                # If nums[right] is odd, move right pointer to the left
                right -= 1
            else:
                # If nums[left] is odd and nums[right] is even, swap them
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums