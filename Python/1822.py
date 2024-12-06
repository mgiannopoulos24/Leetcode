from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_count = 0
        
        for num in nums:
            if num == 0:
                return 0  # If there's a zero, product is zero
            elif num < 0:
                negative_count += 1
        
        # If the number of negatives is even, the product is positive; otherwise, it's negative
        return 1 if negative_count % 2 == 0 else -1
