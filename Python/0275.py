from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations) - 1
        n = len(citations)
        
        while low <= high:
            mid = (low + high) // 2
            # Number of papers with at least citations[mid] citations
            num_papers_with_at_least_mid_citations = n - mid
            
            if citations[mid] >= num_papers_with_at_least_mid_citations:
                # This means we have at least num_papers_with_at_least_mid_citations papers with at least citations[mid] citations
                # Try for a higher value of h
                low = mid + 1
            else:
                # citations[mid] is too small, try a smaller value of h
                high = mid - 1
        
        # After exiting the loop, high will be the maximum valid h-index
        return n - high - 1
