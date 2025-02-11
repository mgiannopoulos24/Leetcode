from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        
        while left < right:
            mid = (left + right) // 2
            total_stores = 0
            
            for q in quantities:
                # Calculate the number of stores needed for this product type
                total_stores += (q + mid - 1) // mid
            
            if total_stores <= n:
                right = mid
            else:
                left = mid + 1
        
        return left