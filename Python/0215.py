import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap to keep the top k largest elements
        min_heap = []
        
        # Iterate over each number in the array
        for num in nums:
            # Add the current number to the heap
            heapq.heappush(min_heap, num)
            
            # If the size of the heap exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the min-heap is the kth largest element
        return min_heap[0]
