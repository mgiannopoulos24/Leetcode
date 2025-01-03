from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # Create a dictionary to store the color changes at each point
        color_changes = defaultdict(int)
        
        # Populate the color_changes dictionary
        for start, end, color in segments:
            color_changes[start] += color
            color_changes[end] -= color
        
        # Sort the event points
        sorted_points = sorted(color_changes.keys())
        
        # Initialize the result list
        painting = []
        
        # Initialize the current color sum and the previous point
        current_sum = 0
        prev_point = None
        
        # Iterate through the sorted points
        for point in sorted_points:
            if prev_point is not None and current_sum != 0:
                painting.append([prev_point, point, current_sum])
            current_sum += color_changes[point]
            prev_point = point
        
        return painting