class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Get the first two points to calculate the reference slope
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Calculate the differences for the slope
        dx = x1 - x0
        dy = y1 - y0
        
        # Check the slope for all subsequent points
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Use the cross-product to avoid division and compare slopes
            if (y - y0) * dx != (x - x0) * dy:
                return False
        
        return True
