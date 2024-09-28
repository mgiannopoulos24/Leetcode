import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word
        count = Counter(words)
        
        # Step 2: Use a heap to store the k most frequent words
        # Heap will be sorted by (-frequency, word), so most frequent words come first
        heap = []
        
        for word, freq in count.items():
            # Python's heapq is a min-heap, we store (-freq, word) to simulate max-heap
            heapq.heappush(heap, (-freq, word))
        
        # Step 3: Extract the top k elements from the heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return result
