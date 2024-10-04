from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Step 1: Store points in a set for quick lookup
        point_set = set(map(tuple, points))
        min_area = float('inf')
        
        # Step 2: Iterate through all pairs of points
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Check if the two points can form one side of a rectangle
                if x1 != x2 and y1 != y2:
                    # Step 3: Calculate the other two points of the rectangle
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        # Calculate area of the rectangle
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)
        
        # Step 4: Return the result, if no rectangle is found return 0
        return min_area if min_area != float('inf') else 0
