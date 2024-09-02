from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        from collections import defaultdict

        # Initialize variables to find the bounding rectangle
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        # Variable to store the total area of all rectangles
        total_area = 0
        
        # Dictionary to count the occurrences of each corner
        corner_count = defaultdict(int)
        
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            
            # Update the bounding rectangle coordinates
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            # Compute the area of the current rectangle and add it to the total area
            total_area += (x2 - x1) * (y2 - y1)
            
            # Define the corners of the rectangle
            corners = [
                (x1, y1),
                (x1, y2),
                (x2, y1),
                (x2, y2)
            ]
            
            # Update corner counts
            for corner in corners:
                corner_count[corner] ^= 1  # Toggle between 0 and 1
        
        # Compute the area of the bounding rectangle
        bounding_area = (max_x - min_x) * (max_y - min_y)
        
        # Check if the total area matches the bounding rectangle area
        # and if the set of corners matches exactly the corners of the bounding rectangle
        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }
        
        # Check that exactly 4 corners are present and have the correct count
        return (total_area == bounding_area and
                set(corner for corner, count in corner_count.items() if count) == expected_corners)
