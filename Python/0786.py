from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        
        # Initialize the min-heap with fractions involving the smallest numerator
        for j in range(1, n):
            heapq.heappush(min_heap, (arr[0] / arr[j], 0, j))
        
        # Extract the k-th smallest fraction
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if i + 1 < j:
                # Generate the next fraction with the next numerator
                next_fraction = (arr[i + 1] / arr[j], i + 1, j)
                heapq.heappush(min_heap, next_fraction)
        
        # The k-th smallest fraction
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]
