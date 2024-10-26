import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap by inserting negative values
        heap = [-stone for stone in stones]
        heapq.heapify(heap)  # Transform list into a heap
        
        # Smash stones until there is at most one left
        while len(heap) > 1:
            # Get the two heaviest stones (inverted back to positive)
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            if first != second:
                # If they are not the same, insert the difference back into the heap
                heapq.heappush(heap, -(first - second))
        
        # If there's a stone left, return its weight (invert back to positive)
        return -heap[0] if heap else 0
