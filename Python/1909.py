from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        violation = -1  # To track the index of the first violation
        
        # Check for violations
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                if violation != -1:  # If we already found one violation, return False
                    return False
                violation = i  # Mark the first violation index
        
        # If no violations, the array is already strictly increasing
        if violation == -1:
            return True
        
        # Check if we can remove nums[violation] or nums[violation - 1]
        # Case 1: Remove nums[violation]
        if violation == n - 1 or nums[violation - 1] < nums[violation + 1]:
            return True
        
        # Case 2: Remove nums[violation - 1]
        if violation == 1 or nums[violation - 2] < nums[violation]:
            return True
        
        return False
