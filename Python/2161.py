from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Initialize three lists to hold elements less than, equal to, and greater than the pivot
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []
        
        # Iterate through the nums array and separate the elements
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)
        
        # Concatenate the three lists to get the final rearranged array
        return less_than_pivot + equal_to_pivot + greater_than_pivot