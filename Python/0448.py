from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark the indices in the array.
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Collect the indices of positive numbers.
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
