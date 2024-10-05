from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Define a lambda function to calculate the squared Euclidean distance
        def squared_distance(point):
            x, y = point
            return x * x + y * y
        
        # Sort points by their squared distance from the origin
        points.sort(key=squared_distance)
        
        # Return the first k points
        return points[:k]
