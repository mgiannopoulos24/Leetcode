class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        # Traverse through each consecutive pair of points
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            # Calculate the differences in the x and y coordinates
            x_diff = abs(x2 - x1)
            y_diff = abs(y2 - y1)
            
            # The time to travel between two points is the maximum of x_diff and y_diff
            total_time += max(x_diff, y_diff)
        
        return total_time
