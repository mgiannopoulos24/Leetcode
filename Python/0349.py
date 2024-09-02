from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert lists to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find intersection of both sets
        intersection = set1 & set2
        
        # Convert the result to a list and return
        return list(intersection)
