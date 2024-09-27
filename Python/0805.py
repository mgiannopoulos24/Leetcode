from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        from functools import lru_cache
        
        total_sum = sum(nums)
        n = len(nums)
        nums.sort()  # Sorting to help with early termination in recursion
        
        # Check if it's possible to find a valid k and corresponding sum
        @lru_cache(None)
        def is_possible(k, target_sum, start):
            # Base cases
            if k == 0:
                return target_sum == 0
            if target_sum < 0 or k + start > n:
                return False
            
            # Recursive case: either pick the current element or skip it
            for i in range(start, n - k + 1):
                # Optimization: Avoid duplicate starting elements in this context
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if is_possible(k - 1, target_sum - nums[i], i + 1):
                    return True
            return False

        # Loop through all possible subset sizes
        for k in range(1, n // 2 + 1):
            if (total_sum * k) % n == 0:
                target_sum = (total_sum * k) // n
                if is_possible(k, target_sum, 0):
                    return True

        return False
