from collections import Counter
from math import gcd

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # A dictionary to count the frequency of each width-to-height ratio
        ratio_count = Counter()
        
        # Count ratios
        for width, height in rectangles:
            # Reduce the ratio to its simplest form using gcd
            divisor = gcd(width, height)
            ratio = (width // divisor, height // divisor)
            ratio_count[ratio] += 1
        
        # Calculate the number of interchangeable pairs
        interchangeable_pairs = 0
        for count in ratio_count.values():
            if count > 1:
                interchangeable_pairs += count * (count - 1) // 2
        
        return interchangeable_pairs
