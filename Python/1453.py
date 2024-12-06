from math import sqrt, isclose

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        def find_circle_centers(p1, p2, r):
            # Distance between p1 and p2
            d = distance(p1, p2)
            if d > 2 * r:
                return []  # No circle can pass through both points
            
            # Midpoint between p1 and p2
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            
            # Distance from the midpoint to the circle centers
            h = sqrt(r ** 2 - (d / 2) ** 2)
            
            # Perpendicular direction from p1 to p2
            dx = p2[1] - p1[1]
            dy = p1[0] - p2[0]
            dist_norm = sqrt(dx ** 2 + dy ** 2)
            dx /= dist_norm
            dy /= dist_norm
            
            # Two possible centers
            center1 = (mid_x + dx * h, mid_y + dy * h)
            center2 = (mid_x - dx * h, mid_y - dy * h)
            
            return [center1, center2]
        
        def count_darts_in_circle(center, darts, r):
            count = 0
            for dart in darts:
                if distance(center, dart) <= r + 1e-7:  # to handle floating-point precision
                    count += 1
            return count
        
        n = len(darts)
        if n == 1:
            return 1
        
        max_darts = 1
        
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = darts[i], darts[j]
                centers = find_circle_centers(p1, p2, r)
                for center in centers:
                    max_darts = max(max_darts, count_darts_in_circle(center, darts, r))
        
        return max_darts
