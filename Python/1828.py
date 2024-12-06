from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        
        # Iterate over each query
        for xj, yj, rj in queries:
            count = 0
            radius_squared = rj * rj  # Avoid recalculating r^2 for every point
            
            # Check each point for the current circle
            for xi, yi in points:
                # Calculate the squared distance from the point to the circle's center
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= radius_squared:
                    count += 1
            
            result.append(count)
        
        return result
