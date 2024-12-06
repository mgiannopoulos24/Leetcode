import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights) - 1):
            # Calculate the difference in height between the current and next building
            diff = heights[i + 1] - heights[i]
            
            # If the next building is taller
            if diff > 0:
                heapq.heappush(heap, diff)  # Add the difference to the heap
                
                # If the size of the heap exceeds the number of ladders, use bricks
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)  # Use bricks for the smallest jump
                
                # If we run out of bricks, return the current building index
                if bricks < 0:
                    return i
        
        # If we can reach the last building, return the last building index
        return len(heights) - 1
