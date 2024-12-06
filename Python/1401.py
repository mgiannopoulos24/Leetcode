class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point on the rectangle to the circle's center
        closest_x = min(max(xCenter, x1), x2)  # Clamp xCenter to [x1, x2]
        closest_y = min(max(yCenter, y1), y2)  # Clamp yCenter to [y1, y2]
        
        # Calculate the distance from the circle center to the closest point
        dx = closest_x - xCenter
        dy = closest_y - yCenter
        
        # If the distance from the circle center to this point is less than or equal to the radius
        return dx * dx + dy * dy <= radius * radius
