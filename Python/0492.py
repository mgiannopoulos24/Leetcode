from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        min_diff = float('inf')
        best_pair = []
        
        # Iterate over possible widths W from 1 to sqrt(area)
        for W in range(1, int(math.sqrt(area)) + 1):
            if area % W == 0:
                L = area // W
                # Ensure L >= W
                if L >= W:
                    diff = L - W
                    # Update best_pair if we found a smaller difference
                    if diff < min_diff:
                        min_diff = diff
                        best_pair = [L, W]
        
        return best_pair
