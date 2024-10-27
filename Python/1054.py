from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Step 1: Count the frequency of each barcode
        counter = Counter(barcodes)
        
        # Step 2: Use a max heap to prioritize placing the most frequent barcodes first
        max_heap = [(-count, barcode) for barcode, count in counter.items()]
        heapq.heapify(max_heap)
        
        # Step 3: Result array to store rearranged barcodes
        result = [0] * len(barcodes)
        
        # Step 4: Fill even indices first, then odd indices
        index = 0
        while max_heap:
            count, barcode = heapq.heappop(max_heap)
            count = -count  # Make the count positive
            
            # Place the barcode in the result array at every alternate index
            for _ in range(count):
                result[index] = barcode
                index += 2
                if index >= len(barcodes):
                    index = 1  # Start placing at odd indices if even ones are filled
                
        return result
