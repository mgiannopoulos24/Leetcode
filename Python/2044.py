from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Calculate the maximum possible OR
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Step 2: Count the number of subsets with OR equal to max_or
        n = len(nums)
        count = 0
        
        # Using bitmask to generate all possible subsets
        for mask in range(1, 1 << n):
            current_or = 0
            for i in range(n):
                if mask & (1 << i):
                    current_or |= nums[i]
            if current_or == max_or:
                count += 1
        
        return count