from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        # Traverse through the numbers in the array
        for num in nums:
            index = abs(num) - 1
            # If the value at index is negative, it means we've seen this number before
            if nums[index] < 0:
                result.append(index + 1)
            # Mark the number as seen by making it negative
            else:
                nums[index] = -nums[index]
        
        return result
