from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # Step 1: Find the largest square side length for each rectangle and the global maxLen
        maxLen = 0
        maxLenCount = 0
        
        for length, width in rectangles:
            side_length = min(length, width)
            
            # Update maxLen and count the occurrences of maxLen
            if side_length > maxLen:
                maxLen = side_length
                maxLenCount = 1
            elif side_length == maxLen:
                maxLenCount += 1
        
        return maxLenCount
