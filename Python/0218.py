import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect all events
        events = []
        for left, right, height in buildings:
            events.append((left, -height))  # Start event
            events.append((right, height))  # End event

        # Sort events
        events.sort()

        # Resultant list of key points
        result = []
        # Max-heap to keep track of heights
        max_heap = [0]  # Initialize with 0 height
        # Previous max height
        prev_max_height = 0

        # Process all events
        for x, height in events:
            if height < 0:  # Start of a building
                heapq.heappush(max_heap, height)
            else:  # End of a building
                # Remove the height from heap (delayed removal)
                max_heap.remove(-height)
                heapq.heapify(max_heap)  # Reorder heap

            # Current max height
            current_max_height = -max_heap[0]

            # If height changes, add a key point
            if current_max_height != prev_max_height:
                result.append([x, current_max_height])
                prev_max_height = current_max_height

        return result
