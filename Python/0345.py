from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a min-heap to keep the top k elements
        # Pair is (frequency, element)
        min_heap = []
        
        # Step 3: Populate the heap
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove the least frequent element
        
        # Step 4: Extract the elements from the heap
        result = [num for freq, num in min_heap]
        
        return result
