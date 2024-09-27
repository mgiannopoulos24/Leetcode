from heapq import heappush, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count frequencies of each character
        freq = Counter(s)
        
        # Step 2: Create a max heap based on character frequencies
        max_heap = []
        for char, count in freq.items():
            heappush(max_heap, (-count, char))
        
        # Step 3: Check if rearrangement is possible
        n = len(s)
        if -max_heap[0][0] > (n + 1) // 2:
            return ""
        
        result = []
        prev_count, prev_char = 0, ''
        
        # Step 4: Build the result
        while max_heap:
            count, char = heappop(max_heap)
            result.append(char)
            
            # Push the previous character back if its count is still positive
            if prev_count < 0:
                heappush(max_heap, (prev_count, prev_char))
            
            # Update the previous character
            prev_count, prev_char = count + 1, char
        
        return ''.join(result)
