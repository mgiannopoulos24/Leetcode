import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        posx, posy = location
        same_location_count = 0
        angles = []
        
        # Step 1: Calculate angles for each point
        for x, y in points:
            if x == posx and y == posy:
                # Point is at the same location as the observer
                same_location_count += 1
            else:
                # Calculate angle in degrees using atan2 (y, x)
                angle_rad = math.atan2(y - posy, x - posx)
                angle_deg = math.degrees(angle_rad)
                angles.append(angle_deg)
        
        # Step 2: Sort angles and handle circularity by appending angles + 360 degrees
        angles.sort()
        angles_extended = angles + [a + 360 for a in angles]
        
        # Step 3: Sliding window to count maximum visible points in any `angle` window
        max_visible = 0
        left = 0
        for right in range(len(angles_extended)):
            # The window is [left, right], and we check if it's within the viewing angle
            while angles_extended[right] - angles_extended[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)
        
        # Return the max visible points, including those at the same location
        return max_visible + same_location_count
