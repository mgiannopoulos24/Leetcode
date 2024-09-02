from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count frequencies of each element in nums1
        count1 = Counter(nums1)
        
        # Prepare the result list
        result = []
        
        # Iterate through nums2 and check if the element is in nums1 with remaining frequency
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
        
        return result
