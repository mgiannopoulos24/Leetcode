import math
from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # Initialize the center as the centroid of all points
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        
        epsilon = 1e-7  # Convergence threshold
        max_iter = 10000  # Maximum number of iterations to prevent infinite loops
        
        for _ in range(max_iter):
            numerator_x = 0.0
            numerator_y = 0.0
            denominator = 0.0
            stop = False
            
            for p in positions:
                xi, yi = p
                dist = math.hypot(x - xi, y - yi)
                if dist < epsilon:
                    # Current center coincides with a customer position
                    stop = True
                    break
                weight = 1.0 / dist
                numerator_x += xi * weight
                numerator_y += yi * weight
                denominator += weight
            
            if stop:
                break  # Current center is optimal
            
            new_x = numerator_x / denominator
            new_y = numerator_y / denominator
            
            # Check for convergence
            if math.hypot(new_x - x, new_y - y) < epsilon:
                x, y = new_x, new_y
                break
            
            x, y = new_x, new_y
        
        # Calculate the total sum of distances from the optimal center to all customers
        total_distance = 0.0
        for p in positions:
            total_distance += math.hypot(x - p[0], y - p[1])
        
        return total_distance
