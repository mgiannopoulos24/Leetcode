import heapq

class MedianFinder:
    def __init__(self):
        # Max-Heap (simulated with negative numbers)
        self.max_heap = []
        # Min-Heap
        self.min_heap = []
    
    def addNum(self, num: int) -> None:
        # Add to max-heap (simulated with negative values)
        heapq.heappush(self.max_heap, -num)
        
        # Ensure max-heap's root is less than or equal to min-heap's root
        if (self.min_heap and -self.max_heap[0] > self.min_heap[0]):
            value_to_move = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value_to_move)
        
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            value_to_move = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value_to_move)
        elif len(self.min_heap) > len(self.max_heap):
            value_to_move = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value_to_move)
    
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
