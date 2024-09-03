from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Dictionary to store frequency of each gap position
        gap_count = defaultdict(int)
        
        # Total number of rows
        num_rows = len(wall)
        
        for row in wall:
            cumulative_width = 0
            for width in row[:-1]:  # Ignore the last brick to avoid counting the edge of the wall
                cumulative_width += width
                gap_count[cumulative_width] += 1
        
        # Find the maximum number of rows that have a gap at the same position
        max_gaps = max(gap_count.values(), default=0)
        
        # The minimum number of bricks crossed
        min_bricks = num_rows - max_gaps
        
        return min_bricks
