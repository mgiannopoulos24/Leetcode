from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Convert each list to a set to remove duplicates within each list
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        
        # Find the intersection of each pair of sets
        intersection1 = set1 & set2  # Values in both nums1 and nums2
        intersection2 = set1 & set3  # Values in both nums1 and nums3
        intersection3 = set2 & set3  # Values in both nums2 and nums3
        
        # Combine all intersections and convert to a set to remove duplicates
        result_set = intersection1 | intersection2 | intersection3
        
        # Convert the set back to a list and return
        return list(result_set)