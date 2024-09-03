from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # Ensure that mid is always the start of a pair
            if mid % 2 == 1:
                mid -= 1
            
            # Check if the single element is in the left or right half
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        
        return nums[left]
