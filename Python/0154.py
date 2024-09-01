from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right element, minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than right element, minimum could be in the left half
            elif nums[mid] < nums[right]:
                right = mid
            # If mid element is equal to right element, we cannot decide the side, so reduce the search space
            else:
                right -= 1
        
        # At the end, left == right and points to the minimum element
        return nums[left]
