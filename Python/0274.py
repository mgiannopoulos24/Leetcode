from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the list of citations in non-decreasing order
        citations.sort()
        
        n = len(citations)
        
        # Iterate from the highest citation count to the lowest
        for i in range(n):
            # The number of papers with at least citations[i] citations
            # is given by (n - i), where i is the current index in the sorted list
            if citations[i] >= n - i:
                return n - i
        
        # If no h-index found (which theoretically shouldn't happen given the problem constraints)
        return 0
