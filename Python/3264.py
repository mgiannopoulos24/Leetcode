from heapq import heappush, heappop
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Initialize a priority queue (min-heap)
        min_heap = []
        
        # Build the initial heap with value and index
        for i in range(len(nums)):
            heappush(min_heap, (nums[i], i))
        
        # Perform k operations
        for _ in range(k):
            # Extract the minimum value and its index
            min_value, idx = heappop(min_heap)
            
            # Update the value in nums
            nums[idx] = min_value * multiplier
            
            # Push the updated value and its index back into the heap
            heappush(min_heap, (nums[idx], idx))
        
        # Return the modified nums array
        return nums
