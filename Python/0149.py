from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            
            if dx == 0:
                return (0, 1) if dy > 0 else (0, -1)
            
            g = gcd(dx, dy)
            return (dx // g, dy // g)
        
        max_points = 1
        n = len(points)
        
        for i in range(n):
            slopes = defaultdict(int)
            same_points = 1  # Start with 1 to count the point itself
            
            for j in range(n):
                if i == j:
                    continue
                
                if points[i] == points[j]:
                    same_points += 1
                    continue
                
                s = slope(points[i], points[j])
                slopes[s] += 1
            
            curr_max = max(slopes.values(), default=0) + same_points
            max_points = max(max_points, curr_max)
        
        return max_points
