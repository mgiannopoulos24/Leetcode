from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize global minimum and maximum
        global_min = float('inf')
        global_max = float('-inf')
        max_distance = 0
        
        # Iterate through each array
        for array in arrays:
            # Local min and max for the current array
            local_min = array[0]
            local_max = array[-1]
            
            # Update global min and max
            if global_min != float('inf'):
                max_distance = max(max_distance, abs(local_max - global_min), abs(local_min - global_max))
            
            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)
        
        return max_distance
