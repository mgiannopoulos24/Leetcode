from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # If there are no balloons, no arrows are needed
        if not points:
            return 0
        
        # Sort balloons by their ending point
        points.sort(key=lambda x: x[1])
        
        # Initialize the count of arrows and the end position of the last arrow shot
        arrows = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            # If the current balloon starts after the end of the last balloon burst
            if points[i][0] > end:
                # Shoot a new arrow and update the end position
                arrows += 1
                end = points[i][1]
        
        return arrows
