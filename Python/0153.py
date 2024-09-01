from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If middle element is greater than the rightmost element,
            # the minimum element must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum element is in the left half or is the mid element
                right = mid
        
        # At the end of the loop, left == right and points to the minimum element
        return nums[left]
