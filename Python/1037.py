from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Extract the points
        (x1, y1), (x2, y2), (x3, y3) = points
        
        # Check if any two points are the same (i.e., not distinct)
        if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
            return False
        
        # Check for collinearity using the cross-product method
        # If the cross product is zero, the points are collinear
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
