from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Marking presence of positive integers within the range [1, n]
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Finding the smallest missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all integers from 1 to n are present, return n + 1
        return n + 1
