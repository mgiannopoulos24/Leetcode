from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Unpack rectangles
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # Check if one rectangle is to the left of the other
        if x2 <= x3 or x4 <= x1:
            return False
        
        # Check if one rectangle is below the other
        if y2 <= y3 or y4 <= y1:
            return False
        
        # If none of the non-overlap conditions are true, they must overlap
        return True
