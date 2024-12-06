class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Step 1: Calculate the minute hand angle
        minute_angle = minutes * 6  # 6 degrees per minute
        
        # Step 2: Calculate the hour hand angle
        hour_angle = (hour % 12) * 30 + (minutes * 0.5)  # 30 degrees per hour and 0.5 degrees per minute
        
        # Step 3: Find the absolute difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # Step 4: Return the smaller angle (either clockwise or counterclockwise)
        return min(angle, 360 - angle)
