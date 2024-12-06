class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Step 1: Extract the x-coordinates from the points
        x_coords = sorted([x for x, y in points])
        
        # Step 2: Find the maximum difference between consecutive x-coordinates
        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])
        
        return max_width
