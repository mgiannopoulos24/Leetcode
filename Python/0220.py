from sortedcontainers import SortedList
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff < 1 or valueDiff < 0:
            return False
        
        sorted_list = SortedList()
        
        for i, num in enumerate(nums):
            # Maintain the sliding window of size <= indexDiff
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            
            # Find the position where `num` could be inserted
            pos = sorted_list.bisect_left(num)
            
            # Check if there's any number in the window within valueDiff
            if pos < len(sorted_list) and sorted_list[pos] <= num + valueDiff:
                return True
            if pos > 0 and sorted_list[pos - 1] >= num - valueDiff:
                return True
            
            # Add current number to the sorted list
            sorted_list.add(num)
        
        return False
