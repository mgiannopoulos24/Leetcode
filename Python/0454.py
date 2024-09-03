from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Hash map to store sums of pairs from nums1 and nums2
        sum_count = defaultdict(int)
        
        # Compute all possible sums of pairs from nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum_count[num1 + num2] += 1
        
        # Count the number of valid tuples
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in sum_count:
                    count += sum_count[target]
        
        return count
