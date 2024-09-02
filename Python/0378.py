import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Min-heap to store the elements along with their positions
        min_heap = []
        
        # Initialize the heap with the first element of each row
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        # Extract the minimum element k times
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                # Add the next element in the same row to the heap
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        return val
