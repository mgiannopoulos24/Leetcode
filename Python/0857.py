from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Calculate the ratio of wage to quality for each worker and store it with quality
        workers = [(w / q, q) for w, q in zip(wage, quality)]
        
        # Sort workers by the ratio of wage to quality
        workers.sort()
        
        min_cost = float('inf')
        quality_heap = []
        total_quality = 0
        
        # Iterate over sorted workers
        for ratio, q in workers:
            # Add the current worker's quality to the heap
            heapq.heappush(quality_heap, -q)
            total_quality += q
            
            # Ensure we only have at most k workers in the heap
            if len(quality_heap) > k:
                total_quality += heapq.heappop(quality_heap)
            
            # If we have exactly k workers, calculate the cost for this ratio
            if len(quality_heap) == k:
                min_cost = min(min_cost, ratio * total_quality)
        
        return min_cost
