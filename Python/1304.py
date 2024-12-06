from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        # Add pairs of integers that sum to zero
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        # If n is odd, append 0
        if n % 2 == 1:
            result.append(0)
        
        return result
