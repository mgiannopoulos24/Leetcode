from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings
        nums_str = list(map(str, nums))
        
        # Custom comparator function for sorting
        def compare(x, y):
            # Compare concatenated results
            if x + y > y + x:
                return -1  # x should come before y
            else:
                return 1  # y should come before x
        
        # Sort the list with the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Edge case: if the largest number is '0', return '0'
        if nums_str[0] == '0':
            return '0'
        
        # Concatenate the sorted strings
        return ''.join(nums_str)
