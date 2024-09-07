import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the min-heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        min_range = float('inf')
        result = [0, 0]
        
        # Iterate until one of the lists is exhausted
        while len(min_heap) == len(nums):
            current_min, list_index, element_index = heapq.heappop(min_heap)
            
            # Update the minimum range
            if current_max - current_min < min_range:
                min_range = current_max - current_min
                result = [current_min, current_max]
            
            # Move to the next element in the same list
            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                current_max = max(current_max, next_value)
            else:
                break
        
        return result
