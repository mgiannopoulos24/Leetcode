from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        result_index = -1
        
        for i, (a, b) in enumerate(points):
            # Check if the point is valid
            if a == x or b == y:
                # Calculate Manhattan distance
                distance = abs(x - a) + abs(y - b)
                
                # Update the minimum distance and result index
                if distance < min_distance:
                    min_distance = distance
                    result_index = i
                elif distance == min_distance and i < result_index:
                    result_index = i
        
        return result_index
