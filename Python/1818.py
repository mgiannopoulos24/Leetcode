from typing import List
from bisect import bisect_left

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        
        # Step 1: Calculate the initial sum of absolute differences
        total_diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        
        # Create a sorted version of nums1 for binary search
        sorted_nums1 = sorted(nums1)
        
        # Step 2: Try to find the maximum reduction in absolute sum difference
        max_reduction = 0
        
        for i in range(n):
            current_diff = abs(nums1[i] - nums2[i])
            
            # Binary search for the closest element to nums2[i] in sorted_nums1
            pos = bisect_left(sorted_nums1, nums2[i])
            
            # Check left neighbor (if it exists) and current position
            if pos < n:
                min_diff_with_replacement = abs(sorted_nums1[pos] - nums2[i])
                max_reduction = max(max_reduction, current_diff - min_diff_with_replacement)
            
            if pos > 0:
                min_diff_with_replacement = abs(sorted_nums1[pos - 1] - nums2[i])
                max_reduction = max(max_reduction, current_diff - min_diff_with_replacement)
        
        # Step 3: Apply the maximum reduction found
        result = (total_diff - max_reduction) % MOD
        return result
